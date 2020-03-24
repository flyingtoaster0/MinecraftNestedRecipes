# TODO: Have this return a nicer data structure instead of returning bad HTML

class RecipeTraverser:

    def get_tree(self, title, config, indentation_level=0, multiplier=1):
        space = '&nbsp;&nbsp;&nbsp;&nbsp;'

        indent = ''
        for i in range(indentation_level):
            indent = indent + space

        if title not in config:
            print("Missing recipe for <{0}>".format(title))
            return "Missing recipe for <{0}>".format(title)

        line = indent + '{0}x {1}'.format(multiplier, title) + '<br/>'
        ingredient_list = config[title]

        if ingredient_list is None:
            return line

        lines = line
        for ingredient_name, ingredient_amount in ingredient_list:
            lines = lines + self.get_tree(ingredient_name, config, indentation_level + 1, ingredient_amount * multiplier)
        return lines

    def get_trees(self, items, config):
        tree_list = []
        for item in items:
            tree_list.append(self.get_tree(item[0], config, 0, item[1]))
        return tree_list

    def print_trees(self, items, config):
        for item in items:
            self.print_tree(item[0], config, 0, item[1])
            print()

    def print_tree(self, title, config, indentation_level=0, multiplier=1):
        space = '  '

        indent = ''
        for i in range(indentation_level):
            indent = indent + space

        if title not in config:
            print(indent + '{0}x {1}'.format(multiplier, title))
            return

        print(indent + '{0}x {1}'.format(multiplier, title))
        ingredient_list = config[title]

        if ingredient_list is None:
            return

        for ingredient_name, ingredient_amount in ingredient_list:
            self.print_tree(ingredient_name, config, indentation_level + 1, ingredient_amount * multiplier)


    def get_ingredients_list(self, items, config, result_dict={}):
        for item in items:
            result_dict = self.get_ingredients(item[0], config, result_dict, item[1])
        return result_dict

    def get_ingredients(self, title, config, result_dict={}, multiplier=1):

        if title not in config or config[title] is None:
            new_amount = result_dict.get(title, 0) + multiplier
            result_dict[title] = new_amount
            return result_dict

        ingredient_list = config[title]

        for ingredient_name, ingredient_amount in ingredient_list:
            self.get_ingredients(ingredient_name, config, result_dict, ingredient_amount * multiplier)

        return result_dict
