from RecipeTraverser import RecipeTraverser
from RecipeConfig import RecipeConfig

config = RecipeConfig().get_config_yaml()
# config = RecipeConfig().get_ingredient_config()

items = (
    ('electric_motor', 1),
)

recipe_traverser = RecipeTraverser()

recipe_traverser.print_trees(items, config)
print("Total Materials")
print(recipe_traverser.get_ingredients_list(items, config))
