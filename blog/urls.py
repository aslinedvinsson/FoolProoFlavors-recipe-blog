from . import views
from django.urls import path

urlpatterns = [
    path('<slug:slug>/', views.recipepost_detail, name='recipepost_detail'),
    path('', views.RecipePostList.as_view(), name='home'),
]