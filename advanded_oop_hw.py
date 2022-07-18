from datetime import datetime as dt

class User():
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.created_on=dt.utcnow()

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return f'<User | {self.full_name}>'

    def __repr__(self):
        return f'<User | {self.last_name} {self.created_on.strftime("%c")}>'

    def __hash__(self):
        return hash(self.full_name+self.created_on.strftime("%c"))   
    
    def __bool__(self):
        return self.created_on > 0
    
    def __eq__ (self, __o):
        return self.created_on == __o.created_on

    def __lt__(self, __o):
        return self.created_on < __o.created_on
    
    def __gt__(self, __o):
        return self.created_on > __o.created_on

    def __le__(self, __o):
        return self.created_on <= __o.created_on
    
    def __ge__(self, __o):
        return self.created_on >= __o.created_on


class Employee(User):
    def __init__(self, first_name, last_name, email, home_address, security_level, department, e_id):
        super(). __init__(first_name, last_name, email)
        self.home_address = home_address
        self.security_level = security_level
        self.department = department
        self.id = e_id

employee1 = Employee('Alex', 'Collins', 'alexanderacollins@gmail.com', 'abc street 123', 'Red', 'Justice', 'Sucks@coding')
print(employee1)
employee2 = Employee('David', 'Crackerjack', 'crackjack23@gmail.com', 'abc street 245', 'Blue', 'Rubberduck', 'Suddenlyjacked')
print(employee2)
employee3 = Employee('Allen', 'Ripley', 'rippenripley@yahoo.com', 'abc street 456', 'Green', 'Muggle', 'Loverboy69')
print(employee3)

employees = [employee1, employee2, employee3]
employees.sort


    

class Customer(User):
     def __init__(self, first_name, last_name, email, shipping_address, billing_address, purchase_history, c_id):
        super(). __init__(first_name, last_name, email)
        self.shipping_address = shipping_address
        self.billing_address = billing_address
        self.purchase_history = purchase_history
        self.id = c_id

customer1 = Employee('Sally', 'Fields', 'supersally@gmail.com', 'abc street 123', 'abc street 123', 'The Secret', 'sallyfields23')
print(customer1)
customer2 = Employee('Tanner', 'Buntley', 'buntlers@gmail.com', 'abc street 245', 'abc street 234', 'Pack of Jimmy\'s', 'Loverboy96')
print(customer2)
customer3 = Employee('Moses', 'Maron', 'theothermoses@yahoo.com', 'abc street 456', 'abc street 456', 'Clown Shoes', 'Carnie54')
print(customer3)

customers = [customer1, customer2, customer3]
customers.sort