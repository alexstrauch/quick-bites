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

    