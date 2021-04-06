cookbook = dict(
        sandwich = {
                'ingredients' : ["ham", "bread", "cheese", "tomatoes"],
                'meal' : "lunch",
                'prep_time' : 10
                   },
        cake = {
                'ingredients' : ["flour", "sugar", "eggs"],
                'meal' : "dessert",
                'prep_time' : 60
               },
        salad = {
                'ingredients' : ["avocado", "arugula", "tomatoes", "spinach"],
                'meal' : "lunch",
                'prep_time' : 15
                }
                )


def Recipe(nrecipe) :
    if nrecipe in cookbook :
        print("\nRecipe for {}:\nIngredients list: {}\nTo be eaten for {}.\nTakes {} minutes of cooking.\n".format(nrecipe, cookbook[nrecipe]['ingredients'], cookbook[nrecipe]['meal'], cookbook[nrecipe]['prep_time']))
    else :
        print("\nrecipe not found...\n")

def Add_new_recipe(nrecipe, ingredients, meal, prep_time) :
    cookbook[nrecipe] = {'ingredients' : ingredients, 'meal' : meal, 'prep_time' : prep_time}

def Del_recipe(nrecipe) :
    if nrecipe in cookbook :
        cookbook.pop(nrecipe)
        print("\n" + nrecipe.capitalize() + " has been deleted!\n")
    else :
        print("recipe not found...\n")

def All_recipe() :
    print("\nrecipes :")
    for recipe in cookbook :
        print("- " + recipe)
    print()
while True :
    action = input("Please select an option by typing the corresponding number:\n 1: Add a recipe\n 2: Delete a recipe\n 3: Print a recipe\n 4: Print the cookbook\n 5: Quit\n>> ")
    if int(action) == 1:
        nrecipe = input("\nPlease enter the recipe name:\n>> ")
        ingredients = input("\nPlease enter the recipe ingredients (separated by spaces):\n>> ").split()
        meal = input("\nPlease enter the meal type:\n>> ")
        prep_time = input("\nPlease enter the preparation time:\n>> ")
        Add_new_recipe(nrecipe, ingredients, meal, prep_time)
        print()
    elif int(action) == 2:
        nrecipe = input("\nPlease enter the recipe's name to delete:\n>> " )
        Del_recipe(nrecipe)
    elif int(action) == 3:
        nrecipe = input("\nPlease enter the recipe's name to get its details:\n>> ")
        Recipe(nrecipe)
    elif int(action) == 4:
        All_recipe()
    elif int(action) == 5:
        print("\nCookbook closed.")
        exit()
    else :
        print("\nError: unknown instuction...\n")

