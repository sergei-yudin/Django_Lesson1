from http.client import responses

from django.http import Http404
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def recipe_view(request, dish):
    serving = request.GET.get('serving', 1)
    try:
        serving = int(serving)
    except ValueError:
        serving = 1

    if dish not in DATA:
        raise Http404('Рецепт не найден')

    base_recipe = DATA[dish]
    recipe = {ingredient: amount * serving for ingredient, amount in base_recipe.items()}

    context = {
        'recipe': recipe
    }

    return render(request, 'calculator/index.html', context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
