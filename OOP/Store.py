# My eStore Classes

class User:
    "Store User"
    def __init__(self, email, passwd):
        self._email = email
        self._password = passwd
        self._cart = None

    def get_email(self):
        return self._email

    def open_cart(self):
        self._cart = ShoppingCart(self)

    def get_cart(self):
        return self._cart


class Product:
    "A Product"
    def __init__(self, name, upc):
        self._name = name
        self._upc = upc

    def __str__(self):
        return f"{self.get_name()} ({self.get_upc()})"

    def __repr__(self):
        return str(self)
    
    def get_upc(self):
        return self._upc

    def get_name(self):
        return self._name

    def get_price(self):
        if "GOLD" in self._name.upper():
            return 1000
        else:
            return 100

class ShoppingCart:
    def __init__(self, belongs_to):
        self._belongs_to = belongs_to
        self._items = []

    def __len__(self):
        return len(self._items)
    
    def add_product(self, product):
        self._items.append(product)

    def remove_product(self, product):
        self._items.remove(product)

    def get_items(self):
        newlist = []
        for item in self._items:
            newlist.append(item)
        return newlist

    def __str__(self):
        newstr =  f"Shopping Cart of {self._belongs_to.get_email()}:"
        newstr += "\n"
        for item in self.get_items():
            newstr += str(item) + "\n"
        return newstr
    
    def __repr__(self):
        return str(self)

    def generate_invoice(self):
        return Invoice(self)

class Invoice:
    """An invoice"""
    def __init__(self,cart):
        self._balance = 0
        for product in self._cart.get_items():
            self._balance += product.get_price()

    def get_balance(self):
        return self._balance

    def pay(self,amount):
        self._balance -= amount



class ElectronicProduct(Product):
    """An electronic product"""

    COST_PER_MB = 10.0 # TL/MB
    
    def __init__(self, name, upc, size):
        super().__init__(name, upc)
        self._size = size # size in megabytes

    def get_price(self):
        """Returns price of the eProduct"""
        return ElectronicProduct.COST_PER_MB * self._size

    def get_size(self):
        """Returns the size of the eProduct in MB"""
        return self._size

             
## My Sample Data

userlist = [
    User("ali@example.com","secret"),
    User("acacar@metu.edu.tr","min545"),
    User("pelin@yahoo.com","opensesame")
]
        
catalog = [
    Product("Laptop", 32423488),
    Product("Gold Pen", 98237498),
    Product("PS4", 9283409),
    ElectronicProduct("Call of Duty", 230084802, 32000)
]
    
userlist[0].open_cart()
userlist[0]._cart.add_product(catalog[0])
userlist[0]._cart.add_product(catalog[1])
userlist[0]._cart.add_product(catalog[3])

print("Ali bought:")
for item in userlist[0].get_cart().get_items():
    print(item.get_name() + ": " + str(item.get_price()))
