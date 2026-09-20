# ATM-style banking app with dummy user data
# This app is designed for learning and practice.

accounts = {
    "ali@gmail.com": {
        "name": "Ali Khan",
        "pin": "1234",
        "balance": 25000.0,
        "phone": "0300-1234567",
    },
    "sara@gmail.com": {
        "name": "Sara Ahmed",
        "pin": "4321",
        "balance": 18000.0,
        "phone": "0312-7654321",
    },
}


def login_account():
    print("\n=== ATM LOGIN ===")
    email = input("Enter your email: ").strip().lower()
    pin = input("Enter your 4-digit PIN: ").strip()

    if email in accounts and accounts[email]["pin"] == pin:
        print(f"\nWelcome back, {accounts[email]['name']}!")
        return accounts[email]

    print("Invalid email or PIN. Please try again.")
    return None


def check_balance(account):
    print(f"\nYour current balance is: Rs {account['balance']:.2f}")


def deposit_money(account):
    try:
        amount = float(input("Enter amount to deposit: "))
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        return

    if amount <= 0:
        print("Deposit amount must be greater than zero.")
        return

    account["balance"] += amount
    print(f"Deposit successful. New balance: Rs {account['balance']:.2f}")


def withdraw_money(account):
    try:
        amount = float(input("Enter amount to withdraw: "))
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        return

    if amount <= 0:
        print("Withdrawal amount must be greater than zero.")
        return

    if amount > account["balance"]:
        print("Insufficient balance. You cannot withdraw more than your balance.")
        return

    account["balance"] -= amount
    print(f"Withdrawal successful. New balance: Rs {account['balance']:.2f}")


def show_account_details(account):
    print("\n=== ACCOUNT DETAILS ===")
    print(f"Name: {account['name']}")
    print(f"Phone: {account['phone']}")
    print(f"Balance: Rs {account['balance']:.2f}")


def atm_menu(account):
    while True:
        print("\n=== ATM MENU ===")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Account Details")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            check_balance(account)
        elif choice == "2":
            deposit_money(account)
        elif choice == "3":
            withdraw_money(account)
        elif choice == "4":
            show_account_details(account)
        elif choice == "5":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")


def main():
    print("Welcome to the ATM Machine")
    print("Demo users: ali@gmail.com / 1234")
    print("Demo users: sara@gmail.com / 4321")

    while True:
        print("\n1. Login")
        print("2. Exit")
        option = input("Select an option: ").strip()

        if option == "1":
            user = login_account()
            if user is not None:
                atm_menu(user)
        elif option == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


# if __name__ == "__main__":
main()
