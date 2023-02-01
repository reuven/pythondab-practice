# 10 (1)
class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor
        
s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('coffee')

for one_scoop in [s1, s2, s3]:
    print(one_scoop.flavor)


# 10 (2)
class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def greet(self):
        return f'Hello, {self.name}!'


p1 = Person('Reuven', 'reuven@gmail.com', '14123981239')
p2 = Person('Mike', 'mike@gmail.com', '23123123239')
p3 = Person('Matt', 'matt@gmail.com', '871231231239')

for one_person in [p1, p2, p3]:
    print(one_person.name)

p2.email = 'mikey@gmail.com'

for one_person in [p1, p2, p3]:
    print(one_person.email)


# 10 (3)
class BankAccount:
    def __init__(self):
        self.transactions = []

    def deposit(self, amount):
        self.transactions.append(float(amount))

    def withdraw(self, amount):
        self.transactions.append(float(f'{amount}'))

ba1 = BankAccount()
ba2 = BankAccount()

ba1.deposit(25)
ba1.deposit(100)
ba1.deposit(23.5)
ba1.deposit(143.75)
ba1.withdraw(22.15)

ba2.deposit(250)
ba2.deposit(1000)
ba2.deposit(230.5)
ba2.deposit(1430.75)
ba2.withdraw(220.15)

print(len(ba1.transactions))
print(sum(ba1.transactions)/len(ba1.transactions))

print(len(ba2.transactions))
print(sum(ba2.transactions)/len(ba1.transactions))



# 14 (1)
class Bowl:
    def __init__(self):
        self.flavors_list = []

    def add_scoops(self, *scoops):
        [self.flavors_list.append(scoop.flavor)
        for scoop in scoops]

    def flavors(self):
        return self.flavors_list

b = Bowl()
b.add_scoops(s1, s2)
b.add_scoops(s3)
b.flavors()


# 14 (2)
class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.accounts_list = []

    def add_account(self, *accounts):
        [self.accounts_list.append(account)
        for account in accounts]

    def all_balances(self, *accounts):
        return [sum(account.transactions)
                for account in self.accounts_list]

    def current_total_balance(self):
        return sum(self.all_balances())

    def average_transaction_amount(self):
        return [sum(account.transactions)/len(account.transactions)
                for account in self.accounts_list]

p1 = Person('Reuven', 'reuven@gmail.com', '14123981239')
p1.add_account(ba1,ba2)
p1.all_balances()
p1.current_total_balance()
p1.average_transaction_amount()



# 14 (3)
class ShoppingCart:
    def __init__(self):
       self.shopping_cart = {}

    def add(self, name, ppu, qty):
        if name in self.shopping_cart:
            self.shopping_cart[name]['quantity'] += qty
        else:
            self.shopping_cart[name] = {'price-per-unit':ppu, 'quantity':qty}

    def remove(self, name):
        if name in self.shopping_cart:
            if self.shopping_cart[name]['quantity'] == 1:
                self.shopping_cart.pop(name)
            else:
                self.shopping_cart[name]['quantity'] -= 1

    def total(self):
        return sum([self.shopping_cart[object]['price-per-unit'] * self.shopping_cart[object]['quantity']
                    for object in self.shopping_cart])

sc = ShoppingCart()
sc.add('book', 30, 1)
sc.add('toothbrush', 3, 4)
sc.add('book', 30, 1)

sc.remove('toothbrush')
sc.total()



#19 (1)
class Bowl:
    max_scoops = 3

    def __init__(self):
        self.flavors_list = []

    def add_scoops(self, *scoops):
        self.flavors_list += scoops[:Bowl.max_scoops - len(self.flavors_list)]

    def flavors(self):
        return ', '.join(scoop.flavor
                         for scoop in self.flavors_list)

b = Bowl()
b.add_scoops(s1, s2)
b.add_scoops(s3)
b.add_scoops(s1, s2, s1)
b.flavors()



# 19 (2)
class Loan:
    bank_available_asset = 1000

    def __init__(self, amount):
        self.amount = 0
        if Loan.bank_available_asset < amount:
            raise ValueError('No sufficient funds')
        else :
            Loan.bank_available_asset -= amount
            self.amount += amount

    def repay(self, amount):
        self.amount -= amount
        Loan.bank_available_asset += amount

l1 = Loan(500)
l2 = Loan(200)
l3 = Loan(700)  # raises an exception -- ValueError to indicate no money
l1.repay(500)
l3 = Loan(700)  # now it'll work, because the bank has sufficient funds




# 21 (1)

class VerbosePerson(Person):
    def __init__(self, name, email, phone):
        super().__init__(name, email, phone)

    def greet(self):
        return f'Hello, rather something longer thant that {self.name}'


vp1 = VerbosePerson('name1', 'email1', 902345917)



# 21 (2)
class OnlineShoppingCart(ShoppingCart):
    def __init__(self):
        super().__init__()

    def total(self):
        total_amount = sum([self.shopping_cart[object]['price-per-unit'] * self.shopping_cart[object]['quantity']
                            for object in self.shopping_cart])

        return total_amount + ((5*total_amount)/100) +10

sc = OnlineShoppingCart()
sc.add('book', 30, 1)
sc.add('toothbrush', 3, 4)
sc.add('book', 30, 1)

sc.remove('toothbrush')
sc.total()




# 21 (3)

class BigBowl(Bowl):
    max_scoops = 5

    def __init__(self):
        super().__init__()

    def add_scoops(self, *scoops):
        self.flavors_list += scoops[:BigBowl.max_scoops - len(self.flavors_list)]

b = BigBowl()
b.add_scoops(s1, s2)
b.add_scoops(s3)
b.add_scoops(s1, s2, s1)
b.flavors()
