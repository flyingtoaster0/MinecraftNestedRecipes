from RecipeTraverser import RecipeTraverser
from RecipeConfig import RecipeConfig
import argparse


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('recipe', help='The name of the recipe to parse')
args = parser.parse_args()

recipe_name = args.recipe

config = RecipeConfig().get_config_yaml()

recipe_traverser = RecipeTraverser()

print()
recipe_traverser.print_tree(recipe_name, config)

print()
print("Total Materials")
print(recipe_traverser.get_ingredients(recipe_name, config))
