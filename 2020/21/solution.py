import re


def parse_data():
    with open('2020/21/input.txt') as f:
        data = f.read()

    ingredient_allergens = dict()

    ingredients = set()
    allergens = set()

    for ingreds, allers in re.findall(r'(.+) \(contains (.+)\)', data):
        ingreds = tuple(ingreds.split())
        allers = set(allers.split(', '))

        ingredients |= set(ingreds)
        allergens |= allers

        ingredient_allergens[ingreds] = allers

    return ingredients, allergens, ingredient_allergens


def get_allergic_ingredients(ingredients, allergens, ingredient_allergens):
    contains = {allergen: ingredients.copy() for allergen in allergens}

    for ingreds, allers in ingredient_allergens.items():
        for allergen in allers:
            contains[allergen] &= set(ingreds)

    allergic_ingredients = dict()

    while contains:
        for allergen, ingreds in contains.items():
            if len(ingreds) == 1:
                ingredient = next(iter(ingreds))

                for other_ingredients in contains.values():
                    other_ingredients -= {ingredient}

                del contains[allergen]
                allergic_ingredients[ingredient] = allergen
                break

    return allergic_ingredients


def part_one(data):
    non_allergic_ingredients = data[0] - set(get_allergic_ingredients(*data))
    return sum(ingreds.count(ingred) for ingred in non_allergic_ingredients for ingreds in data[2])


def part_two(data):
    allergic_ingredients = sorted(get_allergic_ingredients(*data).items(), key=lambda tup: tup[1])
    return ','.join(ingredient[0] for ingredient in allergic_ingredients)


def main():
    data = parse_data()

    print(f'Day 21 Part 01: {part_one(data)}')
    print(f'Day 21 Part 02: {part_two(data)}')
