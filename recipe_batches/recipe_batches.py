#!/usr/bin/python

import math


def recipe_batches(recipes, ingredients):
    batches = 0
    for key in recipes:
        if key in ingredients:
            while ingredients[key] > recipes[key]:
                ingredients[key] = ingredients[key] - recipes[key]
                batches += 1
        else:
            return 0

    return math.floor(batches / len(recipes))
    # lowest = None

    # # Loop through the recipe
    # for ing, amt in recipe.items():
    #     # Compare to ingredients
    #     if ing in ingredients:
    #         compare = ingredients[ing] // amt
    #     else:
    #         compare = 0

    #     if (lowest is None) or (compare < lowest):
    #         lowest = compare

    # return lowest


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
