"""
Linear search is a search algorithm that sequentially checks whether a given value is an element of specified list by scanning the elements of a list one-by-one until it finds the target value.
"""

# A list of the ingredients for tuna sushi
recipe = ["nori", "tuna", "soy sauce", "sushi rice"]
target_ingredient = "avocado"


def linear_search(search_list, target_value):
    for idx in range(len(search_list)):
        if search_list[idx] == target_value:
            return idx
    raise ValueError("{0} not in list".format(target_value))


print(linear_search(recipe, target_ingredient))
