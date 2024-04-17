class Bankomat(self):
    def __init__(self, balance):
        self.balance=balance
    def check_balance(balance):
        print("Your balance: {} sum".format(balance))

    def deposit(balance, amount):
        balance += amount
        print("{} рублей успешно внесена на счет.".format(amount))
        return balance

    def withdraw(balance, amount):
        if balance >= amount:
            balance -= amount
            print("Сумма {} рублей успешно снята со счета.".format(amount))
        else:
            print("На вашем счете недостаточно средств.")
        return balance
        choice = input("Введите номер действия: ")
first=Bankomat()