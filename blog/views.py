from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Avg
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.core.exceptions import PermissionDenied
from .models import RecipePost, Comment, RecipeRating
from .forms import CommentForm, RecipePostForm #RatingForm,
import cloudinary


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
    """
    queryset = RecipePost.objects.filter(status=1)
    recipepost = get_object_or_404(queryset, slug=slug)
    comments = recipepost.comments.all().order_by("-created_on")
    comment_count = recipepost.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.recipepost = recipepost
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()

    return render(
        request,
        "blog/recipepost_detail.html",
        {
            "recipepost": recipepost,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form
        },
    )


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
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
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.user == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('recipepost_detail', args=[slug]))

"""
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
"""

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
    #success_url = reverse_lazy('recipepost_detail')

    def get_success_url(self):
        return reverse_lazy('recipepost_detail', kwargs={'slug': self.object.slug})

    def get_queryset(self):
        return RecipePost.objects.filter(user=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, 'Recipe updated!')
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        context = {
            'form': form,
            'existing_image_public_id': self.extract_public_id(self.object.food_image.url) if self.object.food_image else None,
        }
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def extract_public_id(self, cloudinary_url):
        try:
            parts = cloudinary_url.split('/')
            public_id_with_format = parts[-1].split('.')[0]
            # Extract the public_id from the filename
            public_id = public_id_with_format.split('_')[0]
            return public_id
        except Exception as e:
            print(f"Error extracting public_id: {e}")
            return None


class DeleteRecipe(DeleteView):
    def get(self, request, *args, **kwargs):
        recipe_slug = self.kwargs.get('slug')
        recipepost = get_object_or_404(RecipePost, slug=recipe_slug)

        # Check if the user is the author or has the necessary permissions
        if recipepost.user == request.user:
            recipepost.delete()
            messages.add_message(request, messages.SUCCESS, 'Recipe deleted!')

            return HttpResponseRedirect(reverse('home'))
        else:
            # Handle unauthorized access, maybe show an error page or redirect
            messages.add_message(request, messages.ERROR, 'You can only delete your own recipes!')
            return HttpResponseRedirect(reverse('home'))



