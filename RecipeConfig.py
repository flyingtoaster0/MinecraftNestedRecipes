from RecipeTraverser import RecipeTraverser
import yaml


class RecipeConfig:

    def get_config_yaml(self):
        with open("recipes.yml", 'r') as ymlfile:
            config = yaml.load(ymlfile, Loader=yaml.BaseLoader)
            converted_config = {}
            for recipe_name, dict_list in config.items():
                for ingredient_dict in dict_list:
                    ingredient_table = []
                    name = ingredient_dict['name']
                    amount = int(ingredient_dict['amount'])
                    ingredient_table.append((name, amount,),)
                converted_config[recipe_name] = ingredient_table
            return converted_config


    def get_ingredient_config(self):
        return {

            'log': None,
            'wooden_planks': None,
            'stick': None,
            'iron_ingot': None,
            'gold_ingot': None,
            'cobblestone': None,
            'glass': None,

            'redstone': None,
            'diamond': None,
            'glowstone_dust': None,
            'lapis_lazuli': None,


            'iron_pickaxe': (('iron_ingot', 3), ('stick', 2)),
            'chest': (('wooden_planks', 8),),
            'hopper': (('chest', 1), ('iron_ingot', 5)),

            'furnace': (('cobblestone', 8),),

            'bucket': (('iron_ingot', 3),),

            'rubber': None,

# ingots
            'copper_ingot': None,
            'tin_ingot': None,
            'bronze_ingot': None,


# cable
            'tin_cable': None,
            'copper_cable': None,

# insulated cable
            'insulated_tin_cable': None,
            'insulated_copper_cable': None,

# plates
            'iron_plate': None,
            'bronze_plate': None,
            'tin_plate': None,
            'copper_plate': None,

            'basic_machine_casing': (('iron_plate', 8),),

            'tin_item_casing': None,
            'copper_item_casing': None,
            'bronze_item_casing': None,
            'iron_item_casing': None,

# dust
            'coal_dust': None,
            'diamond_dust': None,

# machines

            'generator': (('re_battery', 1), ('basic_machine_casing', 1), ('furnace', 1)),
            'solar_panel': (('electronic_circuit', 2), ('glass', 3), ('coal_dust', 3), ('generator', 1)),
            'ore_washing_plant': (('iron_plate', 3), ('bucket', 2), ('basic_machine_casing', 1), ('electric_motor', 2), ('electronic_circuit', 1)),
            'thermal_centrifuge': (('coil', 2), ('basic_machine_casing', 1), ('electric_motor', 1), ('iron_ingot', 4), ('mining_laser', 1)),



# metal former stuff

            'iron_shaft': (('iron_ingot', 9),),

            're_battery': (('tin_item_casing', 2), ('redstone', 2), ('insulated_tin_cable', 1)),

            'electronic_circuit': (('insulated_copper_cable', 6), ('redstone', 2), ('iron_plate', 1)),

            'electric_motor': (('tin_item_casing', 2), ('coil', 2), ('iron_ingot', 2)),

            'coil': (('copper_cable', 8), ('iron_ingot', 1)),

            'small_power_unit': (('re_battery', 1), ('electric_motor', 1), ('electronic_circuit', 1), ('copper_cable', 2), ('iron_item_casing', 2)),
            'windmeter': (('tin_item_casing', 4), ('bronze_item_casing', 1), ('small_power_unit', 1)),


# wind

            'kinetic_wind_generator': (('basic_machine_casing', 1), ('iron_shaft', 2)),
            'wooden_rotor_blade': (('log', 3), ('wooden_planks', 6)),
            'wooden_kinetic_gearbox_rotor': (('wooden_rotor_blade', 4), ('iron_ingot', 1)),
            'iron_rotor_blade': (('iron_ingot', 3), ('iron_plate', 6)),
            'iron_kinetic_gearbox_rotor': (('iron_rotor_blade', 4), ('iron_ingot', 1)),


# advanced stuff

            'mining_laser': (('redstone', 2), ('energy_crystal', 1), ('advanced_circuit', 2), ('advanced_alloy', 4)),
            'energy_crystal': (('energium_dust', 9),),
            'energium_dust': (('redstone', 5), ('diamond_dust', 4)),
            'advanced_circuit': (('redstone', 4), ('glowstone_dust', 2), ('lapis_lazuli', 2), ('electronic_circuit', 1)),
            'advanced_alloy': (('iron_plate', 3), ('bronze_plate', 3), ('tin_plate', 3)),

        }
