
# run me to see these classes used...
#   by entering on the command line:  'python3 mike_objects_ex1.py'


class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor


class Person:
    def __init__(self, name, email=None, phone=None):
        self.name = name
        self.email = email
        self.phone = phone
        self.accounts = [ ]

    def add_account(self, new_account):
        self.accounts.append(new_account)

    def all_balances(self):
        return [sum(one_account.transactions) for one_account in self.accounts]

    def current_total(self):
        return sum([sum(one_account.transactions) for one_account in self.accounts])


class BankAccount:
    def __init__(self):
        self.transactions = []


class Bowl(object):
    def __init__(self):
        self.scoops = [ ]

    def add_scoops(self, *more_scoops):
        self.scoops += more_scoops

    def flavors(self):
        return ', '.join([one_scoop.flavor for one_scoop in self.scoops])


class ShoppingCart(object):
    def __init__(self):
        self.contents = { }

    def add(self, name, price, add_qty):
        if name in self.contents:
            price, qty = self.contents[name]
            self.contents[name] = (price, qty + add_qty)
        else:
            self.contents[name] = (price, add_qty)
    
    def total(self):
        carttotal = 0
        for item, info in self.contents.items():
            price, qty = info
            #print(item, price, qty)
            carttotal += price * qty
        return f'${carttotal:.2f}'

    def remove(self, name):
        if name in self.contents:
            price, qty = self.contents[name]
            if qty == 1:
                del(self.contents[name])
            else:
                self.contents[name] = (price, qty - 1)


#--------------------------------------------------
if __name__ == '__main__':

    linebreak = "----+" * 10
    # Run examples of each class:
    print('\nHere is the SCOOPS Class example...\n')
    s1 = Scoop('chocolate')
    s2 = Scoop('vanilla')
    s3 = Scoop('coffee\n')
    print('Print the flavor of s1.\n')
    print(s1.flavor)
    print()
    print('Print the flavors of all three scoops\n')
    for one_scoop in [s1, s2, s3]:
        print(one_scoop.flavor)

    print(linebreak)

    print('\nHere is the PERSON Class example...\n')
    p1 = Person("Mike","m@gm.com","505-515-5151")
    p2 = Person('Riley', 'riley@home.com', '404-414-4444')
    p3 = Person('Amy', 'aadams@att.com', '630-224-2421')

    print('NAME\t   PHONE') 
    print('--------------------')
    for one_person in (p1, p2, p3):
        print(f'{one_person.name}\t{one_person.phone}')

    print(f'\nUpdate the email of the second person {p2.name}\n')
    print(f'Before : {p2.email}')
    p2.email = 'new-riley@gmail.com'
    print(f'After  : {p2.email}\n')

    # Accounts
    print(linebreak)
    print('\nACCOUNT Class')

    mychecking = BankAccount()
    mysavings = BankAccount()

    mychecking.transactions.append(1200)
    mychecking.transactions.append(-230)
    mychecking.transactions.append(-650)
    mychecking.transactions.append(1000)
    mychecking.transactions.append(-390)

    mysavings.transactions.append(250)
    mysavings.transactions.append(250)
    mysavings.transactions.append(250)
    mysavings.transactions.append(250)
    mysavings.transactions.append(-490)

    print('\nAccount details:')
    accountnames = ['mychecking', 'mysavings']
    theaccounts = [mychecking, mysavings]
    for indx,theaccount in enumerate(theaccounts):
        print(f'ACCOUNT: {accountnames[indx]}\t \
            BALANCE = ${sum(theaccount.transactions):.2f}     \
                AVERAGE = ${sum(theaccount.transactions) / len(theaccount.transactions):.2f}')