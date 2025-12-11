# Grocery List: Implement a program that prompts the user for items, one per
#       line, until the user inputs control-d. Then output the user's grocery
#       list in all uppercase, sorted alphabetically by item, prefixing each
#       line with the number of times the user inputted that item. No need to
#       pluralize the items. Treat the user's input case-insensitively.


grocery_list = {}

while True:
    try:
        grocery_item = input("").upper()
        if grocery_item in grocery_list:
            grocery_list[grocery_item] += 1
        else:
            grocery_list.update({grocery_item: 1})
    except EOFError:
        sorted_grocery_list = dict(sorted(grocery_list.items()))
        for item in sorted_grocery_list:
            print(sorted_grocery_list[item], item)
        break
