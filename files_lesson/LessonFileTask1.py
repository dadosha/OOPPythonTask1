import os


def parsing_recipes_file(file_path):
    file_path = os.path.join(os.getcwd(), file_path)

    i = 0
    cook_book = {}

    with open(file_path, encoding="UTF-8") as f:
        lines = f.readlines()

    while i < len(lines):
        dish_name = lines[i].strip()
        i += 1

        count_ingredients = int(lines[i].strip())
        i += 1

        list_ingredients =[]

        for _ in range(count_ingredients):
            ingredient_list = lines[i].strip().split("|")
            ingredient = {
                'ingredient_name': ingredient_list[0].strip(),
                'quantity': int(ingredient_list[1].strip()),
                'measure': ingredient_list[2].strip()
            }

            list_ingredients.append(ingredient)
            i += 1

        cook_book[dish_name] = list_ingredients

        if i < len(lines) and lines[i].strip() == '':
            i += 1

    return cook_book


def get_shop_list_by_dishes(dishes_for_cook, count):
    cook_book = parsing_recipes_file('../files/recipes.txt')

    ingredients_list = {}
    for dish, ingredients in cook_book.items():
        if dish in dishes_for_cook:
            for ingredient in ingredients:
                if ingredients_list.get(ingredient['ingredient_name']):
                    ingredients_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * count
                else:
                    ingredient_dict = {
                        'measure': ingredient['measure'],
                        'quantity': ingredient['quantity'] * count
                    }
                    ingredients_list[ingredient['ingredient_name']] = ingredient_dict

    return ingredients_list


def main():
    file_path = '../files/recipes.txt'
    cook_book = parsing_recipes_file(file_path)
    shop_list = get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)

    for dish, ingredients in cook_book.items():
        print(f"{dish}: {ingredients}")

    for ingredient, count in shop_list.items():
        print(f"{ingredient}: {count}")


if __name__ == "__main__":
    main()