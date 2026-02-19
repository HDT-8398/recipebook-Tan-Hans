from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe

class RecipeListView(ListView):
    model = Recipe
    template_name = "ledger/recipe_list.html"

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "ledger/recipe_detail.html"

