# 7. Create a class BankAccount, which contains attributes balance and name, and methods
# deposit() and withdraw(), to add and deposit some money in account.
# the balance should be set to 0 in the constructor, and withdrawal should be allowed only if
# sufficient balance is there. Also overload the str method to allow printing the details directly.

class BankAccount:
    def __init__(self, name, balance=0):
        self._name = name
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance > amount:
            self._balance -= amount
        else:
            print('There is no sufficient amount')

    def __str__(self):
        return "Name: " + self._name + "\n" + "Balance: " + str(self._balance)


if __name__ == "__main__":
    a = BankAccount("Jinal", 100)
    print(a)
    a.deposit(900)
    print(a)
    a.withdraw(200)
    print(a)
