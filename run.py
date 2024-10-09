import json
import random

class RecipeGenerator:
    def __init__(self, recipe_file):
        """
        Initialize RecipeGenerator with a recipe file.
        """
        self.recipe_file = recipe_file
        self.recipes = self.load_recipes()

    