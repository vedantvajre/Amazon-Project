class IMS():
    def __init__(self, admin):
        self.admin_inventory = []
        self.admin = admin

    def add_to_inventory(self, item):
        self.admin_inventory.append(item.admin_item_description)

    def remove_from_inventory(self, item):
        self.admin_inventory.remove(item.admin_item_description)

    def admin_view_inventory(self):
        print('Hello, ' + self.admin + ' admin, here is our inventory: ')
        print(self.admin_inventory)


class Item():
    def __init__(self, name, cost, quantity):
        self.name = name
        self.cost = cost
        self.quantity = quantity
        self.admin_item_description = {'Name: ' + self.name, 'Cost: ' + self.cost, 'Quantity: ' + self.quantity}
        self.user_item_description = {'Name: ' + self.name, 'Cost: ' + self.cost}


class ShoppingProcess():
    def __init__(self, shopper):
        self.shopper = shopper
        self.ShoppingCart = []
        self.Item_list = []
        self.receipt = []

    def add_to_list(self, item):
        self.Item_list.append(item.user_item_description)

    def remove_from_list(self, item):
        self.Item_list.remove(item.user_item_description)

    def user_view_inventory(self):
        print('Here is our inventory of items ' + self.shopper + ': ')
        print(self.Item_list)

    def add_to_shoppingcart(self):
        for dict in self.Item_list:
            item_description = dict
            self.ShoppingCart.append(item_description)
            print('Adding item to Shopping Cart... ')
            print(self.ShoppingCart)

    def print_receipt(self):
        for dict in self.Item_list:
            receipt = dict['Name', 'Cost']
            print(receipt)


Vedant = IMS('Vedant')
Car = Item('Car', '6000$', '3')
Chicken = Item('Chicken', '10$', '14')
Spatula = Item('Spatula', '6$', '200')
Vedant.add_to_inventory(Car)
Vedant.add_to_inventory(Chicken)
Vedant.add_to_inventory(Spatula)
Vedant.admin_view_inventory()

Shopper1 = ShoppingProcess('Bob')
Shopper1.add_to_list(Car)
Shopper1.add_to_list(Chicken)
Shopper1.add_to_list(Spatula)
Shopper1.user_view_inventory()
Shopper1.add_to_shoppingcart()
Shopper1.print_receipt()