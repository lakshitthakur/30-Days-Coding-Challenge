class BankAccount:
    def __init__(self, account_holder, account_number):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: ${amount}")
        else:
            print("Invalid or insufficient funds!")

    def display(self):
        print("\nAccount Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print(f"Current Balance: ${self.balance}")

def main():
    my_account = BankAccount("Lakshit Thakur", 1001)

    while True:
        print("\n===== Banking System Menu =====")
        print("1. Deposit Money\n2. Withdraw Money\n3. View Account Details\n4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            my_account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            my_account.withdraw(amount)
        elif choice == '3':
            my_account.display()
        elif choice == '4':
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
