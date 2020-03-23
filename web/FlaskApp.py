from flask import Flask

from RecipeConfig import RecipeConfig

import json

from RecipeTraverser import RecipeTraverser

app = Flask(__name__)


@app.route('/list_recipes')
def list_recipes():
    return json.dumps(list(RecipeConfig().get_ingredient_config().keys()))

@app.route('/<recipe>')
def get_recipe(recipe):
    return get_recipe_multiple(recipe, 1)

@app.route('/<recipe>/<multiplier>')
def get_recipe_multiple(recipe, multiplier):
    config = RecipeConfig().get_ingredient_config()
    traverser = RecipeTraverser()
    all_ingredient_dict = traverser.get_ingredients(recipe, config, {}, int(multiplier))
    content = '<h2>Ingredient Tree</h2>' + traverser.get_tree(recipe, config, 0, int(multiplier)) + '<br/><br/>'
    content = content + format_all_ingredient_dict(all_ingredient_dict)

    return content


def format_all_ingredient_dict(all_ingredients):
    lines = '<h2>Total Ingredients</h2>'
    for key, value in all_ingredients.items():
        lines = lines + '{0}: {1}<br/>'.format(value, key)
    return lines

if __name__ == '__main__':
    app.run()