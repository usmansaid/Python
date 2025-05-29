# Password
correctPassword = 12345

# Amount
balance = 100000

# Welcome Screen Method
def welcomeScreen():
    print("======================================")
    print("------- Welcome to ATM System ---------")
    print("======================================")


# Method for Checking Password
def authentication():
    attempts = 3

    while attempts > 0:
        password = int(input("Enter your ATM Password: "))

        if password == correctPassword:
            print("Access Granted!\n")
            return True
        else:
            attempts -= 1
            print(f"Incorrect Password, {attempts} attempts remaining. Try Again")

    print("Access Denied. Account Blocked!") 
    return False    



# Check Balance Method
def checkBalance():
    print(f"Your Current balance is {balance}")


# Deposit method
def deposit():
    global balance

    while True:
        try:
            depositAmount = int(input("Enter the amount for deposit: "))

            if depositAmount <= 0:
                print("Deposit amount must be positive or greater than zero, Try Again")
            else:
                balance += depositAmount
                print(f"An amount of {depositAmount} has successfully deposited, and your new balance is : {balance}")
                break

        except ValueError:
            print("Invalid input, Try Again")



# withdrawal Method
def withdrawal():
    global balance

    while True:
        try:
            withdrawalAmount = int(input("Enter the withdrawal amount: "))

            if withdrawalAmount <= 0:
                print("Deposit amount must be positive or greater than zero, Try Again")
            elif withdrawalAmount > balance:
                print("Insufficient balance!")
            else:
                balance -= withdrawalAmount
                print(f"An amount of {withdrawalAmount} has successfully withdrawn, and your new balance is : {balance}")
                break
        except ValueError:
            print("Invalid Entry, Try Again")



# Method for Menu
def menu():
   while True:
        print("------------------- Main Menu -------------------")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdrawal")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            checkBalance()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdrawal()
        elif choice == 4:
            print("Thanks for using the ATM. Have a good bad Day")
            break
        else:
            print("Invalid Entry, Try Again")


# Main execution
welcomeScreen()

if authentication():
    menu()