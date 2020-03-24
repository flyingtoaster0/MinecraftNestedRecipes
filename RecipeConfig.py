import yaml


class RecipeConfig:

    def get_config_yaml(self):
        with open("recipes.yml", 'r') as ymlfile:
            config = yaml.load(ymlfile, Loader=yaml.BaseLoader)
            converted_config = {}
            for recipe_name, dict_list in config.items():
                ingredient_table = []
                for ingredient_dict in dict_list:
                    name = ingredient_dict['name']
                    amount = int(ingredient_dict['amount'])
                    ingredient_table.append((name, amount,),)
                converted_config[recipe_name] = ingredient_table
            return converted_config
