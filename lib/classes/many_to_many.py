class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >= 3 and not hasattr(self, '_name'):
            self._name = name
        
    def orders(self):
        return [ order for order in Order.all if order.coffee == self ]
    
    def customers(self):
        customers_list = []
        for order in Order.all:
            if order.customer not in customers_list and order.coffee == self:
                customers_list.append(order.customer)
        return customers_list
    
    def num_orders(self):
        num_ordered = [ order.coffee for order in Order.all if order.coffee == self ]
        return len(num_ordered)
    
    def average_price(self):
        prices = [ order.price for order in Order.all if order.coffee == self ]
        if len(prices) == 0:
            return 0
        else:
            return sum(prices)/len(prices)

class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1<=len(name)<=15:
            self._name = name
        
    def orders(self):
        return [ order for order in Order.all if order.customer == self ]
    
    def coffees(self):
        coffees_list = []
        for order in Order.all:
            if order.customer == self and order.coffee not in coffees_list:
                coffees_list.append(order.coffee)
        return coffees_list
    
    def create_order(self, coffee, price):
        return Order(self,coffee,price)
    
class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)
    
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if isinstance(price, float) and 1.0<=price<=10.0 and not hasattr(self, '_price'):
            self._price = price

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee


