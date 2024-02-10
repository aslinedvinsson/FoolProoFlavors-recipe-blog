from django.urls import path
from . import views

from .views import RecipePostList, AddRecipe, UpdateRecipe, DeleteRecipe



urlpatterns = [
    path('add/', AddRecipe.as_view(), name='add_recipe'),
    path('<slug:slug>/', views.recipepost_detail, name="recipepost_detail"),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
    path('<slug:slug>/rate/', views.rate_recipe, name='rate_recipe'),
    path('<slug:slug>/rate_recipe/', views.rate_recipe, name='rate_recipe'),
    path('update/<slug:slug>/', UpdateRecipe.as_view(), name='update_recipe'),
    path('delete_recipe/<slug:slug>/', DeleteRecipe.as_view(), name='delete_recipe'),
    path('', views.RecipePostList.as_view(), name='home'),
]


###dubbelkolla om path behövs