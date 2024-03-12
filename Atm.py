import random
user_balance = 5000
def login_signup():
    print("Welcome to the ATM")
    print("Press L to LOGIN and S to SIGNUP and E to EXIT")
    choice = input("Enter your choice: ").upper()
    if choice == "L":
        login()
    elif choice == "S":
        signup()
    elif choice == "E":
        print("Thank you for using the ATM")
    else:
        print("Invalid choice")
        login_signup()

def login():
    print("Welcome to the LOGIN page")
    username = input("Enter your username: ")
    pin = int(input("Enter your password: "))
    with open ("User_details.csv","r") as file:
        for line in file:
            details = line.strip().split(",")
            if details[0] == username and int(details[1]) == pin:
                print("Login successful")
                print(f"Welcome {username}")
                transaction(username)
                return
    print("Invalid username or pin")
    login_signup()

def signup():
    print("Welcome to the SIGNUP page")
    username =input("Enter your username: ")
    pin = random.randint(1000,9999)
    with open ("User_details.csv","a") as file:
        file.write(f"{username},{pin},{user_balance}\n")
    print("Your pin is: ",pin)
    print("Signup successful")
    print(f"Welcome {username}")
    return login()


def transaction(username):
    print("Welcome to the TRANSACTION page")
    print("Press 1 for Withdrawal")
    print("Press 2 for Deposit")
    print("Press 3 for Balance Enquiry")
    print("Press 4 for Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        withdrawal(username)
    elif choice == 2:
        deposit(username)
    elif choice == 3:
        balance(username)
    elif choice == 4:
        print("Thank you for using the ATM")
        login_signup()
    else:
        print("Invalid choice")
        transaction(username)

def withdrawal(username):
    print("welcome to Withdrawl window")
    pin = int(input("Enter your pin: "))
    with open ("User_details.csv","r") as file:
        for line in file:
            details = line.strip().split(",")
            if int(details[1]) == pin and details[0] == username:
                user_balance = float(details[2])
                amount = float(input("Enter the amount you want to withdraw: "))
                if amount <= user_balance:
                    user_balance -= amount
                    with open("User_details.csv", "w") as file:
                        file.write(f"{username},{pin},{user_balance}\n")
                    print(f"{amount} is withdrawn from your account")
                    print(f"Your current balance is {user_balance}")
                    transaction(username)
                else:
                    print("Insufficient balance")
                    transaction(username)
    print("Invalid username or pin")
    login_signup()

def deposit(username):
    print("welcome to Deposit window")
    pin = int(input("Enter your pin: "))
    with open ("User_details.csv","r") as file:
        for line in file:
            details = line.strip().split(",")
            if int(details[1]) == pin and details[0] == username:
                user_balance = float(details[2])
                amount = float(input("Enter the amount you want to deposit: "))
                print(f"{amount} is deposited in your account")
                user_balance = user_balance + amount
                with open ("User_details.csv","w") as file:
                    file.write(f"{username},{pin},{user_balance}\n")
                print(f"Your current balance is {user_balance}")
                transaction(username)
    print("Invalid username or pin")
    login_signup()

def balance(username):
    print("welcome to Balance Enquiry window")
    pin = int(input("Enter your pin: "))
    with open ("User_details.csv","r") as file:
        for line in file:
            details = line.strip().split(",")
            if int(details[1]) == pin and details[0] == username:
                user_balance = float(details[2])
                print(f"Your current balance is {user_balance}")
            transaction(username)
    print("Invalid username or pin")
    login_signup()


def main():
    login_signup()

if __name__ =="__main__":
    main()

