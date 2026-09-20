accounts = {}


def create_account():
    print("\n=== Create New Account ===")
    name = input("Enter your name: ").strip()
    email = input("Enter your email: ").strip()
    phone = input("Enter your phone number: ").strip()

    while True:
        pin = input("Create your 4-digit PIN: ").strip()
        if pin.isdigit() and len(pin) == 4:
            break
        print("PIN must be exactly 4 digits.")

    accounts[email] = {
        "name": name,
        "email": email,
        "phone": phone,
        "pin": pin,
        "balance": 0.0,
    }

    print(f"\nAccount created successfully for {name}.")
    print(f"Your email is: {email}")
    return accounts[email]


def login_account():
    print("\n=== Login ===")
    email = input("Enter your email: ").strip()
    pin = input("Enter your PIN: ").strip()

    if email in accounts and accounts[email]["pin"] == pin:
        print(f"\nWelcome back, {accounts[email]['name']}!")
        return accounts[email]

    print("Invalid email or PIN. Please try again.")
    return None


def show_account_details(account):
    print("\n=== Account Details ===")
    print(f"Name: {account['name']}")
    print(f"Email: {account['email']}")
    print(f"Phone: {account['phone']}")
    print(f"Balance: ${account['balance']:.2f}")


def deposit_money(account):
    try:
        amount = float(input("Enter amount to deposit: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    if amount <= 0:
        print("Deposit amount must be greater than 0.")
        return

    account["balance"] += amount
    print(f"Deposit successful. New balance: ${account['balance']:.2f}")


def withdraw_money(account):
    try:
        amount = float(input("Enter amount to withdraw: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    if amount <= 0:
        print("Withdrawal amount must be greater than 0.")
        return

    if amount > account["balance"]:
        print("Insufficient balance. You cannot withdraw more than your balance.")
        return

    account["balance"] -= amount
    print(f"Withdrawal successful. New balance: ${account['balance']:.2f}")


def check_balance(account):
    print(f"\nYour current balance is: ${account['balance']:.2f}")


def bank_menu(account):
    while True:
        print("\n=== BANK MENU ===")
        print("1. View account details")
        print("2. Check balance")
        print("3. Deposit money")
        print("4. Withdraw money")
        print("5. Logout")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_account_details(account)
        elif choice == "2":
            check_balance(account)
        elif choice == "3":
            deposit_money(account)
        elif choice == "4":
            withdraw_money(account)
        elif choice == "5":
            print("You have logged out successfully.")
            break
        else:
            print("Invalid option. Please choose again.")


def main():
    print("Welcome to the Bank System")

    while True:
        print("\n1. Create account")
        print("2. Login")
        print("3. Exit")

        option = input("Select an option: ").strip()

        if option == "1":
            create_account()
        elif option == "2":
            user_account = login_account()
            if user_account is not None:
                bank_menu(user_account)
        elif option == "3":
            print("Thank you for using the Bank System. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
