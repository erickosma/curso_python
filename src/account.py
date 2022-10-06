class Account:

    def __init__(self, number, holder, balance, limit):
        print("Construindo objeto ... {}".format(self))
        self.__number = number
        self.__holder = holder
        self.__balance = balance
        self.__limit = limit

    def statement(self):
        return "Saldo de {} do titular {}".format(self.__balance, self.__holder)

    def deposit(self, valor):
        self.__balance += valor

    def take_out(self, valor):
        self.__balance -= valor

    def transfer(self, valor, destino):
        self.take_out(valor)
        destino.deposit(valor)
