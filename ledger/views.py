from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Recipe, Profile, RecipeImage

class RecipeListView(ListView):
    model = Recipe
    template_name = "ledger/recipe_list.html"
    context_object_name = "recipes"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "All Recipes"
        return context


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "ledger/recipe_detail.html"
    context_object_name = "recipe"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = f"Recipe Detail | {self.object.name}"
        return context

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ["name"]
    template_name = "ledger/recipe_form.html"

    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user) 
        form.instance.profile = profile
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy("ledger:recipe_detail", kwargs={"pk": self.object.pk})
    
class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    fields = ["image", "description"]
    template_name = "ledger/recipe_update.html"

    def form_valid(self, form):
        recipe = Recipe.objects.get(pk=self.kwargs["pk"])
        form.instance.recipe = recipe
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy("ledger:recipe_detail", kwargs={"pk": self.kwargs["pk"]})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recipe"] = Recipe.objects.get(pk=self.kwargs["pk"])
        return context