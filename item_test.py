from classes.SmiteGameClasses import Item


item_param_dict = {
    "name": "Gladiator's Shield",
    "cost": 2800,
    "description": 'test',
    "description": 'longer     test'
}

test_item = Item(**item_param_dict)
test_item.debug_print()