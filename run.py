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

    