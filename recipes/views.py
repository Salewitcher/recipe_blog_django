from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm
from .models import Recipe
from django.db.models import Q
from django.shortcuts import render

# Create your views here.


@login_required
def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
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
    query = request.GET.get('q')
    if query:
        recipes = Recipe.objects.filter(
         Q(title__icontains=query) | Q(ingredients__icontains=query),
         created_by=request.user
         )
    else:
        recipes = Recipe.objects.filter(created_by=request.user)
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})


@login_required
def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, id=id, created_by=request.user)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})


@login_required
def edit_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id, created_by=request.user)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', id=recipe.id)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipes/recipe_form.html', {'form': form})


@login_required
def delete_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id, created_by=request.user)
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipe_list')
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})


def index(request):
    recipes = Recipe.objects.all()[:6]  # Get the latest 6 recipes
    return render(request, 'recipes/index.html', {'recipes': recipes})
