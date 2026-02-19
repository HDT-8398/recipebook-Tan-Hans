from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient

class RecipeIngredientInLine(admin.TabularInline):
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInLine]

admin.site.register(Recipe)
admin.site.register(RecipeIngredient)
admin.site.register(Ingredient)

