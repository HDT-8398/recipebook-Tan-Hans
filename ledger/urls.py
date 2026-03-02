from django.urls import path
from . import views

urlpatterns = [
    path("recipe/list/", views.RecipeListView.as_view(), name = "recipe_list"),
    path("recipe/<int:pk>/", views.RecipeDetailView.as_view(), name= "recipe_detail"),
]

app_name = "ledger"