from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Avg
from django.urls import reverse_lazy
from django.utils.text import slugify
from .models import RecipePost, Comment, RecipeRating
from .forms import CommentForm, RatingForm, RecipePostForm





class RecipePostList(generic.ListView):
    queryset = RecipePost.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6

def recipepost_detail(request, slug):
    """
    Display an individual :model:`blog.Recipepost`.

    **Context**

    ``recipepost``
        An instance of :model:`blog.RecipePost`.

    **Template:**

    :template:`blog/recipepost_detail.html`
    """
    queryset = RecipePost.objects.filter(status=1)
    recipepost = get_object_or_404(queryset, slug=slug)
    comments = recipepost.comments.filter(approved=True).order_by("-created_on")
    comment_count = recipepost.comments.filter(approved=True).count()


    rating_form = RatingForm()
    comment_form = CommentForm()

    if request.method == "POST":
        if 'comment_form' in request.POST:
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.user = request.user
                comment.recipepost = recipepost
                comment.save()
                messages.add_message(request, messages.SUCCESS,
                'Comment submitted and awaiting approval')


        elif 'rating_form' in request.POST:
            rating_form = RatingForm(data=request.POST)
            if rating_form.is_valid():
                reciperating = rating_form.cleaned_data['reciperating']

                # Prevent users from rating their own recipes
                if recipepost.user == request.user:
                    messages.error(request, 'You cannot rate your own recipe.')
                else:
                    # Check if the user has already rated the recipe, and update the rating if they have
                    existing_rating = RecipeRating.objects.filter(user=request.user, recipepost=recipepost).first()
                    if existing_rating:
                        existing_rating.reciperating = reciperating
                        existing_rating.save()
                    else:
                        RecipeRating.objects.create(user=request.user, recipepost=recipepost, reciperating=reciperating)

                    messages.success(request, 'Rating saved successfully')

    # Calculate the average rating
    average_rating = RecipeRating.objects.filter(recipepost=recipepost).aggregate(Avg('reciperating'))['reciperating__avg'] or 0
    print(average_rating)

    return render(
        request,
        "blog/recipepost_detail.html",
        {
            "recipepost": recipepost,
            "comments": comments,
            "comment_count": comment_count,
            "rating_form": rating_form,
            "average_rating": average_rating,
            "comment_form": comment_form,

        },
    )

def comment_edit(request, slug, comment_id):
    """
    Display an individual comment for edit-
    **Context**
    ``post```
        An instance of :model:`blog.Post`.
    ``comment```
        A single comment related to the post.
    ``comment_form```
        An instance of :form:`blog.CommentForm`.
    """
    if request.method == "POST":

        queryset = RecipePost.objects.filter(status=1)
        recipepost = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.user == request.user:
            comment = comment_form.save(commit=False)
            comment.recipepost = recipepost
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('recipepost_detail', args=[slug]))



def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = RecipePost.objects.filter(status=1)
    recipepost = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.user == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('recipepost_detail', args=[slug]))

def rate_recipe(request, slug):
    if request.method == 'POST' and 'reciperating' in request.POST:
        rating_form = RatingForm(request.POST)
        if rating_form.is_valid():
            reciperating = rating_form.cleaned_data['reciperating']
            recipepost = get_object_or_404(RecipePost, slug=slug)

            # Prevent users from rating their own recipes
            if recipepost.user == request.user:
                messages.error(request, 'You cannot rate your own recipe.')
                return HttpResponseRedirect(reverse('recipepost_detail', args=[slug]))

            # Check if the user has already rated the recipe, and update the rating if they have
            existing_rating = RecipeRating.objects.filter(user=request.user, recipepost=recipepost).first()
            if existing_rating:
                existing_rating.reciperating = reciperating
                existing_rating.save()
            else:
                RecipeRating.objects.create(user=request.user, recipepost=recipepost, reciperating=reciperating)

            messages.success(request, 'Rating saved successfully')
            return HttpResponseRedirect(reverse('recipepost_detail', args=[slug]))

    # Redirect back if the request method is not POST
    return HttpResponseRedirect(reverse('recipepost_detail', args=[slug]))


class AddRecipe(CreateView):
    model = RecipePost
    form_class = RecipePostForm
    template_name = 'blog/add_recipe.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddRecipe, self).form_valid(form)


class UpdateRecipe(UpdateView):
    model = RecipePost
    form_class = RecipePostForm
    template_name = 'blog/update_recipe.html'
    success_url = reverse_lazy('recipepost_detail')

    def get_queryset(self):
        return RecipePost.objects.filter(user=self.request.user)


class DeleteRecipe(DeleteView):
    model = RecipePost
    template_name = 'blog/delete_recipe.html'
    success_url = reverse_lazy('recipepost_list')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if not obj.user == self.request.user:
            raise PermissionDenied("You don't have permission to delete this recipe.")
        return obj


