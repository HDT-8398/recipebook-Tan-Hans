from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import *

class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInLine]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

class RecipeIngredientInLine(admin.TabularInline):
    model = RecipeIngredient
    extra = 1

class RecipeImageInLine(admin.TabularInline):
    model = RecipeImage
    extra = 1

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInLine, RecipeImageInLine]
    list_display = ("name", "profile", "created_on", "updated_on")

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
admin.site.register(Profile)
