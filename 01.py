class Bankomat:
    def __init__(self, balance):
        self.balance=balance
    def check_balance(self, balance):
        print("Your balance: {} sum".format(self.balance))

    def deposit(self, amount):
        self.balance += amount
        print("{} рублей успешно внесена на счет.".format(amount))
        return self.balance

    def withdraw(self, balance, amount):
        if self.balance >= self.amount:
            self.balance -= self.amount
            print("Сумма {} рублей успешно снята со счета.".format(self.amount))
        else:
            print("На вашем счете недостаточно средств.")
        return balance
        choice = input("Введите номер действия: ")

FirstClient=Bankomat(balance=1000)

print(FirstClient.balance)
print(FirstClient.deposit(2000))
print (FirstClient.balance)