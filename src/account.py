class Account:

    def __init__(self, number, owner, balance, limit):
        print("Construindo objeto...{}".format(self))
        self.number = number
        self.owner = owner
        self.balance = balance
        self.limit = limit

