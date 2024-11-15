from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe

def home(request):
    recipes = Recipe.objects.all()
    return render(request, 'home.html', {'recipes': recipes})

def add_recipe(request):
    if request.method == 'POST':
        name = request.POST['name']
        ingredients = request.POST['ingredients']
        instructions = request.POST['instructions']
        Recipe.objects.create(name=name, ingredients=ingredients, instructions=instructions)
        return redirect('home')
    return render(request, 'add_recipe.html')

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'detail.html', {'recipe': recipe})

def delete_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    recipe.delete()
    return redirect('home')

def edit_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        recipe.name = request.POST['name']
        recipe.ingredients = request.POST['ingredients']
        recipe.instructions = request.POST['instructions']
        recipe.save()
        return redirect('home')
    return render(request, 'edit_recipe.html', {'recipe': recipe})

# Create your views here.
