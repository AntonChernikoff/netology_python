from dis import dis
import os
from posixpath import split

def get_file_name_cook_book() -> str:
    BASE_PATH = os.getcwd()
    FILE_DIR = 'netology_python'
    FILE_NAME = 'recipes.txt'
    return os.path.join(BASE_PATH, FILE_DIR, FILE_NAME)

def cook_book_read(file_recipes_name:str) -> dict:
    recipes = dict()
    with open(file_recipes_name, 'rt') as file_recipes:
        while True:
            line = file_recipes.readline().strip()
            if not line:
                break
            dish = line
            recipes[dish] = []
            ingredients_count = int(file_recipes.readline())
            for i in range(ingredients_count):
                ingredient = file_recipes.readline().strip()
                # print(ingredient)
                ing_list = ingredient.split(' | ')
                recipes[dish].append({"ingredient_name":ing_list[0], "quantity":ing_list[1], "measure":ing_list[2]})
            file_recipes.readline().strip()
    return recipes

def cook_book_print(cook_book:dict):
    for cook in cook_book:
        print(f"{cook}: [")
        for ingredient in cook_book[cook]:
            print(f"\t{ingredient}")
        print(f"\t]")

def get_shop_list_by_dishes(dishes:list, person_count:int = 1):
    if len(dishes) == 0:
        print("Список бюд пуст")
    cook_book = cook_book_read(get_file_name_cook_book())
    # формируем список блюд без повторений (кол-во повторов считаем)
    list_dishes_result = dict()
    for dish in dishes:
        if dish in list_dishes_result:
            list_dishes_result[dish] += 1
        else:
            list_dishes_result[dish] = 1
    # формируме результат по ингридиентам
    list_ingredients = dict()
    for dish in list_dishes_result:
        for ingridient in cook_book[dish]:
            if ingridient['ingredient_name'] in list_ingredients:
                list_ingredients[ingridient['ingredient_name']]['quantity'] += int(ingridient['quantity']) * person_count
            else:
                list_ingredients[ingridient['ingredient_name']] = {'measure': ingridient['measure'], 'quantity': int(ingridient['quantity']) * person_count}
    # распечататм список ингредиентов
    for ingredient in list_ingredients:
        print(f"\t{ingredient}: {list_ingredients[ingredient]}")

# Задание - 1
cook_book = cook_book_read(get_file_name_cook_book())
cook_book_print(cook_book)

# Задание - 2
list_dishes = ['Омлет', 'Фахитос']
get_shop_list_by_dishes(list_dishes,3)

