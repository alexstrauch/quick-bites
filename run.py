import json
import random

class RecipeGenerator:
    def __init__(self, recipe_file):
        """
        Initialize RecipeGenerator with a recipe file.
        """
        self.recipe_file = recipe_file
        self.recipes = self.load_recipes()

    def load_recipes(self):
        """
        Loads recipes from the recipe file specified in self.recipe_file.
        If the file does not exist or is not a valid JSON file, prints an
        error message and returns an empty list.
        """
        try:
            with open(self.recipe_file, 'r') as file:
                recipes = json.load(file)
                return recipes
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading recipes: {e}\n")
            return []

    def save_recipes(self):
        """
        Saves the current recipe list to the
        file specified by self.recipe_file.
        """

        with open(self.recipe_file, 'w') as file:
            json.dump(self.recipes, file, indent=4)

    def add_recipe(self, recipe):
        """
        Adds a recipe to the list of recipes and saves
        the list to the recipe file.
        """
        self.recipes.append(recipe)
        self.save_recipes()

    def get_filtered_recipes(self, meal_type, cuisine_type):
        """
        Returns a list of recipes filtered by meal_type and cuisine_type.
        The filters are case-insensitive.
        """

        return [
            recipe for recipe in self.recipes
            if recipe['meal_type'].lower() == meal_type.lower() and
            recipe['cuisine'].lower() == cuisine_type.lower()
        ]

    def get_random_recipe(self, meal_type, cuisine_type):
        """
        Returns a random recipe from the list of recipes
        filtered by meal_type and cuisine_type.
        If no recipe is found, returns None.
        """
        filtered_recipes = self.get_filtered_recipes(meal_type, cuisine_type)
        if not filtered_recipes:
            return None
        return random.choice(filtered_recipes)

    def display_recipe(self, recipe):
        """
        Displays the selected recipe if found, otherwise displays a message.

        If a recipe is found, it displays the recipe's name, cuisine, diet,
        meal type, ingredients, and instructions.
        If no recipe is found, it displays a message.
        """
        if recipe:
            print(f"\nRecipe: {recipe['name']}\n")
            print(f"Cuisine: {recipe['cuisine']}\n")
            print(f"Diet: {recipe['diet']}\n")
            print(f"Meal Type: {recipe['meal_type']}\n")
            print("Ingredients:")
            for ingredient in recipe['ingredients']:
                print(f"- {ingredient}")
            print(f"\nInstructions: {recipe['instructions']}\n")
        else:
            print("No recipe found for the selected criteria.\n")

def main():
    """
    Main entry point of the Quick Bites recipe generator.

    This function implements a CLI menu to interact with the user.
    The user can select from the following options:
    1. Find a recipe: The user can select a meal type and cuisine type
       and the app will display a random recipe that matches the criteria.
    2. Add a new recipe: The user can enter the details of a new recipe
       and the app will add it to the list of recipes.

    The app will continue to run until the user chooses to quit.
    """
    recipe_file = 'recipes.json'
    generator = RecipeGenerator(recipe_file)

    print("""

▗▖ ▗▖▗▄▄▄▖▗▖    ▗▄▄▖ ▗▄▖ ▗▖  ▗▖▗▄▄▄▖    ▗▄▄▄▖▗▄▖
▐▌ ▐▌▐▌   ▐▌   ▐▌   ▐▌ ▐▌▐▛▚▞▜▌▐▌         █ ▐▌ ▐▌
▐▌ ▐▌▐▛▀▀▘▐▌   ▐▌   ▐▌ ▐▌▐▌  ▐▌▐▛▀▀▘      █ ▐▌ ▐▌
▐▙█▟▌▐▙▄▄▖▐▙▄▄▖▝▚▄▄▖▝▚▄▞▘▐▌  ▐▌▐▙▄▄▖      █ ▝▚▄▞▘


▗▄▄▄▖ ▗▖ ▗▖▗▄▄▄▖ ▗▄▄▖▗▖ ▗▖    ▗▄▄▖ ▗▄▄▄▖▗▄▄▄▖▗▄▄▄▖ ▗▄▄▖
▐▌ ▐▌ ▐▌ ▐▌  █  ▐▌   ▐▌▗▞▘    ▐▌ ▐▌  █    █  ▐▌   ▐▌
▐▌ ▐▌ ▐▌ ▐▌  █  ▐▌   ▐▛▚▖     ▐▛▀▚▖  █    █  ▐▛▀▀▘ ▝▀▚▖
▐▙▄▟▙▖▝▚▄▞▘▗▄█▄▖▝▚▄▄▖▐▌ ▐▌    ▐▙▄▞▘▗▄█▄▖  █  ▐▙▄▄▖▗▄▄▞▘

Welcome to the Quick Bites recipe generator!
Your go-to app for discovering quick and delicious recipes.

""")

    while True:
        print("Please select an option (or type 'q' to quit):")
        print("1. Find a recipe")
        print("2. Add a new recipe")

        choice = input("Enter the number of your choice: \n").strip()

        if choice.lower() == 'q':
            print("Thank you for using Quick Bites. Goodbye!\n")
            return
        
        if choice == '1':
            # Show meal types to the user and ensure valid selection
            meal_types = ("Breakfast", "Lunch", "Dinner", "Dessert")
            while True:
                print("Please select a meal type (or type 'q' to quit):")
                for i, meal in enumerate(meal_types, start=1):
                    print(f"{i}. {meal}")

                meal = input("Enter the number of your choice: \n").strip()

                if meal.lower() == 'q':
                    print("Thank you for using Quick Bites. Goodbye!\n")
                    return

                if meal.isdigit() and 1 <= int(meal) <= len(meal_types):
                    selected_meal = meal_types[int(meal) - 1]
                    break
                else:
                    print("Invalid choice. Please try again.\n")

            # Filter cuisines available for the selected meal type
            cuisines = set(
                recipe['cuisine'] for recipe in generator.recipes
                if recipe['meal_type'] == selected_meal
            )
            if not cuisines:
                print("No cuisines available for the selected meal type.\n")
                continue
            # Allow the user to select a cuisine from the filtered list
            while True:
                print
                (f"\nSelect a cuisine for {selected_meal} (or 'q' to quit):")
                for i, cuisine in enumerate(cuisines, start=1):
                    print(f"{i}. {cuisine}")

                cuisine = input("Enter the number of your choice: \n").strip()

                if cuisine.lower() == 'q':
                    print("Thank you for using Quick Bites. Goodbye!\n")
                    return

                if cuisine.isdigit() and 1 <= int(cuisine) <= len(cuisines):
                    selected_cuisine_type = list(cuisines)[int(cuisine) - 1]
                    break
                else:
                    print("Invalid choice. Please try again.\n")

            # Display a random recipe that matches the user's choices
            recipe = generator.get_random_recipe(
                selected_meal,
                selected_cuisine_type
            )
            generator.display_recipe(recipe)

            # Ask user if they want to continue using the app
            while True:
                continue_input = input(
                    "Feelin' a bit peckish? (yes/no or type 'q' to quit): \n"
                ).strip().lower()

                # If user inputs 'q', exit the app
                if continue_input == 'q':
                    print("Thank you for using Quick Bites. Goodbye!\n")
                    return

                # If user inputs 'yes' or 'y', continue the app loop
                if continue_input in ['yes', 'y']:
                    break

                # If user inputs 'no' or 'n', exit the app
                elif continue_input in ['no', 'n']:
                    print("Thank you for using Quick Bites. Goodbye!\n")
                    return

                # If input is invalid, prompt the user again
                else:
                    print("Invalid. Enter 'yes', 'no', or 'q' to quit.\n")

        elif choice == '2':
            # Add a new recipe
            new_recipe = {}

            # Guide the user through adding a new recipe with instructions
            print("Please enter the following details for the new recipe:\n")

            name = input(
                "Enter the recipe name (e.g., 'Vegan Pancakes') "
                "or type 'q' to quit: \n"
            ).strip()
            if name.lower() == 'q':
                print("Thank you for using Quick Bites. Goodbye!\n")
                return
            new_recipe['name'] = name

            cuisine = input(
                "Enter the cuisine (e.g., 'American', "
                "'Italian', 'Mexican') or type 'q' to quit: \n"
            ).strip()
            if cuisine.lower() == 'q':
                print("Thank you for using Quick Bites. Goodbye!\n")
                return
            new_recipe['cuisine'] = cuisine

            diet = input(
                "Enter the diet type (e.g., 'Vegan', 'Gluten-Free', 'Paleo') "
                "or type 'q' to quit: \n"
            ).strip()
            if diet.lower() == 'q':
                print("Thank you for using Quick Bites. Goodbye!\n")
                return
            new_recipe['diet'] = diet

            meal_type = input(
                "Enter the meal type (e.g., 'Breakfast', 'Lunch', "
                "'Dinner', 'Dessert') or type 'q' to quit: \n"
            ).strip()
            if meal_type.lower() == 'q':
                print("Thank you for using Quick Bites. Goodbye!\n")
                return
            new_recipe['meal_type'] = meal_type

            ingredients = input(
                "Enter the ingredients (comma-separated, e.g., '1 cup flour, "
                "1 tablespoon sugar, 1 cup almond milk') "
                "or type 'q' to quit: \n"
            ).strip()
            if ingredients.lower() == 'q':
                print("Thank you for using Quick Bites. Goodbye!\n")
                return
            new_recipe['ingredients'] = ingredients.split(',')

            instructions = input(
                "Enter the instructions (e.g., 'Mix dry ingredients. "
                "Add wet ingredients and stir until smooth.') "
                "or type 'q' to quit: \n"
            ).strip()
            if instructions.lower() == 'q':
                print("Thank you for using Quick Bites. Goodbye!\n")
                return
            new_recipe['instructions'] = instructions

            # Add the new recipe to the recipe list and save it
            generator.add_recipe(new_recipe)
            print("Recipe added successfully!")

        else:
            # Handle invalid menu option
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()

