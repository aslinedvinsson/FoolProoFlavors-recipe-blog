
urlpatterns = [
     path('', views.RecipePostList.as_view(), name='home'),
     path('<slug:slug>/', views.recipepost_detail, name="recipepost_detail"),
     path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
     path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
     path('<slug:slug>/rate/', views.rate_recipe, name='rate_recipe'),
     path('add_recipe/', views.AddRecipe.as_view(), name='add_recipe'),
     path('<slug:slug>/update_recipe/', views.UpdateRecipe.as_view(), name='update_recipe'),
     path('<slug:slug>/delete_recipe/', views.DeleteRecipe.as_view(), name='delete_recipe'),
]


class UpdateRecipe(UpdateView):
    model = RecipePost
    form_class = RecipePostForm
    template_name = 'blog/update_recipe.html'
    success_url = reverse_lazy('')

    def get_queryset(self):
        return RecipePost.objects.filter(user=self.request.user)






  def get(self, request, *args, **kwargs):
        # Render the template with the form for GET requests
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request, *args, **kwargs):
        # Handle form submission for POST requests
        form = self.form_class(request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            print('Form not valid')
            return render(request, self.template_name, {'form': form})




             <!---- <button class="btn btn-edit" data-recipe_id="{{ recipepost.id }}" data-edit_url="{% url 'update_recipe' slug=recipepost.slug %}">Edit Recipe</button>
  <button class="btn btn-delete-recipe" data-recipe_id="{{ recipepost.id }}" data-delete_url="{% url 'delete_recipe' slug=recipepost.slug %}">Delete Recipe</button>-->