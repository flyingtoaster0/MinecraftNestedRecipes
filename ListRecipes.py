# TODO: Add this in Main.py

from RecipeConfig import RecipeConfig

config = RecipeConfig().get_config_yaml()

for key in list(config.keys()):
    print(key)
