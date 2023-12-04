import re

users = {}

def password_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if re.search(r'[A-Z]', password):
        strength += 1
    if re.search(r'[a-z]', password):
        strength += 1
    if re.search(r'[0-9]', password):
        strength += 1
    if re.search(r'[~!@#$%^&*()_+|\-={}[\]:;<>?/]', password):
        strength += 1
    return strength

def add_user():
    user_id = input("Enter a user ID: ")
    if user_id in users:
        print("Error: User ID already exists.")
        return
    password = input("Enter a password: ")
    while password_strength(password) < 5:
        print(f"This password is weak - {password_strength(password)}")
        password = input("Enter a password: ")
    users[user_id] = password
    print("User Added")

def delete_user():
    user_id = input("Enter a user ID: ")
    if user_id not in users:
        print("Error: User ID does not exist.")
        return
    del users[user_id]
    print("User Deleted")

def change_password():
    user_id = input("Enter a user ID: ")
    if user_id not in users:
        print("Error: User ID does not exist.")
        return
    password = input("Enter a new password: ")
    while password_strength(password) < 5:
        print(f"This password is weak - {password_strength(password)}")
        password = input("Enter a new password: ")
    users[user_id] = password
    print("Password Changed")

def display_users():
    for user_id, password in users.items():
        print(f"User ID: {user_id}, Password: {password}")

def save_to_file():
    with open('Final Project Passwords.txt', 'w') as f:
        for user_id, password in users.items():
            f.write(f"{user_id},{password}\n")
    print("Changes Saved to File")

def menu():
    while True:
        print("1) Add a New User")
        print("2) Delete an Existing User")
        print("3) Change Password on an Existing User")
        print("4) Display All Users")
        print("5) Save Changes to File")
        print("6) Quit")
        selection = input("Enter Selection: ")
        if selection == '1':
            add_user()
        elif selection == '2':
            delete_user()
        elif selection == '3':
            change_password()
        elif selection == '4':
            display_users()
        elif selection == '5':
            save_to_file()
        elif selection == '6':
            break
        else:
            print("Invalid selection. Please try again.")

menu()
