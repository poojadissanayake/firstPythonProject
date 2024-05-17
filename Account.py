class Account:
    @property
    def name(self):
        # returns the value of the private attribute _name
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # __init__ is the constructor
    def __init__(self, name, startingBalance):
        self.name = name
        self.balance = startingBalance

    def print_account(self):
        print("%s $%.2f" % (self.name, self.balance))

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount:.2f} deposited. Balance: ${self.balance:.2f}.")
        else:
            print("Invalid.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"${amount:.2f} withdrawn. Balance: ${self.balance:.2f}.")
        else:
            print("Invalid or insufficient funds.")

    # .....................................................


account_1 = Account("Fred", 100.0)
account_1.print_account()

account_2 = Account("Jane", 80.0)
account_2.print_account()

print()


# def - defines a function
def main():
    # dictionary in Python is a built-in data structure that allows to store and manage data in key-value pairs.
    accounts = {
        "fred": Account("Fred", 100.0),
        "jane": Account("Jane", 80.0)
    }

    while True:
        print("\nUser Interaction Menu:")
        print("1. Print")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Quit")

        try:
            option = int(input("Choose an option: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if option == 4:
            print("Quitting...")
            break
        try:
            # making the user input lowercase using .strip().lower()
            account_name = input("Account name (Fred or Jane): ").strip().lower()
            account = accounts[account_name]
            #  KeyError - exception that is raised when trying to access a key in a dictionary that does not exist
        except KeyError:
            print("Account not found!")
            continue

        if option == 1:
            account.print_account()
        elif option == 2:
            try:
                amount = float(input("Amount to deposit: "))
                # ValueError - correct type but with an invalid value
            except ValueError:
                print("Enter a valid amount.")
                continue
            account.deposit(amount)
        elif option == 3:
            try:
                amount = float(input("Amount to withdraw: "))
            except ValueError:
                print("Enter a valid amount.")
                continue
            account.withdraw(amount)
        else:
            print("Invalid.! Please try again.")


# "if __name__ == "__main__":" - used to ensure that a block of code is executed only when the script is run directly,
# and not when it is imported as a module in another script
if __name__ == "__main__":
    main()
