from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import RecipePost
from .forms import CommentForm


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
        {"recipepost": recipepost,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        },
    )