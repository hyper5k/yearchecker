menu = { "Pizza": 1.99, "Soda":  0.69, "Double Chunk Chocolate Chip Cookie": 2.49}

item_add = int(input("what item do you want to add"))
price_add = int(input("how much should it be"))


def add_item_to_menu(item, price):
    menu[item] = price


add_item_to_menu('item_add', 'price_add')

print(menu)