from . import views
from django.urls import path

urlpatterns = [
    path('<slug:slug>/', views.post_detail, name='recipepost_detail'),
    path('', views.RecipePostList.as_view(), name='home'),
]