from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm
from .models import Recipe

# Create your views here.

@login_required
def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.created_by = request.user
            recipe.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'recipes/recipe_form.html', {'form': form})

@login_required
def recipe_list(request):
    recipes = Recipe.objects.filter(created_by=request.user)
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})
