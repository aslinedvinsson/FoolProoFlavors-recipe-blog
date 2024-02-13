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
from .forms import CommentForm, RecipePostForm, RatingForm
import cloudinary

# Code for RecipePostList is taken from the CodeInstitute Walkthrough
# 'I think, therefor I blog'
class RecipePostList(generic.ListView):
    """
    A view that displays a paginated list of published RecipePosts using
    Django's ListView.

    Attributes:
    - queryset: Selects RecipePosts with status=1 (published).
    - template_name: Path to the "blog/index.html" template for
    rendering the list.
    - paginate_by: Number of RecipePosts to display per page, set to 6.

    """
    queryset = RecipePost.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6


def recipepost_detail(request, slug):
    """
    Renders the detail page for a RecipePost with comments, ratings, and
    forms for adding both.

    Context:
    Variables include the RecipePost instance, comments, comment count,
    forms for comments and ratings, and the average rating.

    Template:
    blog/recipepost_detail.html' for rendering.

    Returns an HttpResponse with the rendered page.
    """
    queryset = RecipePost.objects.filter(status=1)
    recipepost = get_object_or_404(queryset, slug=slug)
    comments = recipepost.comments.all().order_by("-created_on")
    comment_count = recipepost.comments.filter(approved=True).count()
    rating_form = RatingForm()
    comment_form = CommentForm()

    if request.method == "POST":
        if 'body' in request.POST:
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.user = request.user
                comment.recipepost = recipepost
                comment.save()
                messages.add_message(request, messages.SUCCESS,
                                     'Comment submitted and awaiting approval')

        elif 'reciperating' in request.POST:
            rating_form = RatingForm(data=request.POST)
            if rating_form.is_valid():
                reciperating = rating_form.cleaned_data['reciperating']

                # Prevent users from rating their own recipes
                if recipepost.user == request.user:
                    messages.error(request, 'You cannot rate your own recipe.')
                else:
                    # Check if the user has already rated the recipe, and
                    # update the rating if they have
                    existing_rating = RecipeRating.objects.filter(
                        user=request.user, recipepost=recipepost).first()
                    if existing_rating:
                        existing_rating.reciperating = reciperating
                        existing_rating.save()
                    else:
                        RecipeRating.objects.create(user=request.user,
                                                    recipepost=recipepost,
                                                    reciperating=reciperating)
                    messages.add_message(request, messages.SUCCESS,
                                         'Rating saved successfully')
                    return redirect(reverse('recipepost_detail',
                                            kwargs={'slug': slug}))

    # Calculate the average rating
    average_rating = RecipeRating.objects.filter(
        recipepost=recipepost).aggregate(Avg(
            'reciperating'))['reciperating__avg'] or 0

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

# Code taken from the CodeInstitute Walkthrough
# 'I think, therefor I blog'
def comment_edit(request, slug, comment_id):
    """
    Edits an existing comment on a RecipePost.

    Validates the comment edit form and updates the comment if the current
    user is the author. Sets the comment's approval status to False
    (pending review) and saves changes. Displays success or error messages.

    Returns:
    - HttpResponseRedirect to the RecipePost detail page after
    processing the comment update.
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
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')
    return HttpResponseRedirect(reverse('recipepost_detail', args=[slug]))

# Code taken from the CodeInstitute Walkthrough
# 'I think, therefor I blog'
def comment_delete(request, slug, comment_id):
    """
    Deletes a comment from a RecipePost if the current user is
    the comment's author.

    Verifies user ownership of the comment before deletion. Displays a success
    message upon deletion or an error message if the user is not the comment's
    author.

    Returns:
    - HttpResponseRedirect to the RecipePost detail page after attempting
    the comment deletion.
    """
    queryset = RecipePost.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)
    if comment.user == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')
    return HttpResponseRedirect(reverse('recipepost_detail', args=[slug]))


def rate_recipe(request, slug):
    """
    Processes the submission of a rating for a RecipePost by the current user.

    Validates the rating form and updates or creates a rating for the
    RecipePost, ensuring users cannot rate their own posts. Displays message
    for success or errors.

    Returns:
    - HttpResponseRedirect to the RecipePost detail page after processing
    the rating.
    """
    if request.method == 'POST' and 'reciperating' in request.POST:
        rating_form = RatingForm(request.POST)
        if rating_form.is_valid():
            reciperating = rating_form.cleaned_data['reciperating']
            recipepost = get_object_or_404(RecipePost, slug=slug)
            # Prevent users from rating their own recipes
            if recipepost.user == request.user:
                messages.error(request, 'You cannot rate your own recipe.')
                return HttpResponseRedirect(reverse('recipepost_detail',
                                                    args=[slug]))
            # Check if the user has already rated the recipe, and update the
            # rating if they have
            existing_rating = RecipeRating.objects.filter(
                user=request.user, recipepost=recipepost).first()
            if existing_rating:
                existing_rating.reciperating = reciperating
                existing_rating.save()
            else:
                RecipeRating.objects.create(
                    user=request.user, recipepost=recipepost,
                    reciperating=reciperating)
            messages.success(request, 'Rating saved successfully')
            return HttpResponseRedirect(reverse('recipepost_detail',
                                                args=[slug]))
    # Redirect back if the request method is not POST
    return HttpResponseRedirect(reverse('recipepost_detail', args=[slug]))


class AddRecipe(CreateView):
    """
    View for adding new RecipePost instances through a form submission.

    Overrides `form_valid` to assign the current user as the author of
    the RecipePost and checks for unique slug based on the title. Displays
    success or error messages.

    Returns:
    - Redirects to 'home' on success or re-renders the form with errors if
    validation fails.
    """
    model = RecipePost
    form_class = RecipePostForm
    template_name = 'blog/add_recipe.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Assign the current user to the user field of the RecipePost instance
        form.instance.user = self.request.user

        # Generate a unique slug based on the title
        slug = slugify(form.cleaned_data['title'])
        if RecipePost.objects.filter(slug=slug).exists():
            messages.error(self.request,
                           'This recipe name already exists. '
                           'Please choose a different one.')
            return self.form_invalid(form)

        # If slug is unique, proceed with form validation
        messages.success(self.request,
                         'Recipe submitted and awaiting approval!')
        return super(AddRecipe, self).form_valid(form)

    def form_invalid(self, form):
        return super(AddRecipe, self).form_invalid(form)


class UpdateRecipe(UpdateView):
    """
    Allows owners to update their RecipePost instances, handling form
    validation, image updates, and redirects on success.

    Methods override default behavior to ensure users can only update their
    own posts, provide a success URL based on the updated object's slug, and
    customize form handling for success or validation failure. Also, extracts
    and handles an image's public ID for cloudinary-hosted images during
    the update process.

    Returns:
    - On GET, renders the form with the instance to update.
    - On POST, validates and updates the instance, redirecting to the detail
    view on success or re-rendering the form on failure.
    """
    model = RecipePost
    form_class = RecipePostForm
    template_name = 'blog/update_recipe.html'

    def get_success_url(self):
        return reverse_lazy('recipepost_detail', kwargs={'slug': self.
                                                         object.slug})

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
            'existing_image_public_id':
                self.extract_public_id(
                    self.object.food_image.url)
                if self.object.food_image else None,
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
            return None


class DeleteRecipe(DeleteView):
    """
    Allows authors to delete their RecipePost instances. It verifies the
    author's identity before deletion and redirects with messages. If the user
    is not the author, an error message is displayed, and the user is
    redirected.

    Returns:
    - HttpResponseRedirect to 'home' after deletion or after handling
    unauthorized deletion attempts.
    """
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
            messages.error(request, 'You can only delete your own recipes!')
            return HttpResponseRedirect(reverse('home'))
