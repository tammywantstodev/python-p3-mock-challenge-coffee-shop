class Coffee:
    def __init__(self, name):
        self.name = name
    @property
    def name(self):
        return self._name 
    @name.setter
    def name(self, name):
       if not hasattr(self, '_name'):
          if isinstance(name, str) and 3<=len(name):
              self._name=name
        
    def orders(self):
        return [order for order in Order.all if order.coffee==self]
    
    def customers(self):
        return list(set(order.customer for order in self.orders()))
    
    def num_orders(self):
       return len(self.orders())
       
    def average_price(self):
        orders=self.orders()
        if orders:
            return sum(order.price for order in orders)/len(orders)
        return 0.0

class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name 
    @name.setter
    def name(self, name):
        if isinstance(name,str) and 1<= len(name)<=15:
            self._name=name
        
    def orders(self):
        return[order for order in Order.all if order.customer==self]
    
    def coffees(self):
        return list(set(order.coffee for order in self.orders() ))
    
    def create_order(self, coffee, price):
        new_order=Order(self, coffee, price)
        return new_order
    
class Order:
    all=[]
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
        if not hasattr(self, '_price'):
            if isinstance(price, float) and 1.0<=price<=10.0:
                self._price=price

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