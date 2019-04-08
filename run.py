from user import User
from credential import Credential


def create_account (account_name,user_name,user_password,confirmpassword):


    """
    function to create a new account
    """

    new_user = User(account_name,user_name,user_password,confirmpassword)

    return new_user


    def save_details(user):

    """
    function to save save_details
    """
    user.save_detail()

    def display_all_details():

    """
    function used to return all saved save_details
    """
    return User.display_all_details()

def check_existing_user(username):

    """
    a function that is used to check and return all exissting accounts
    """
    return User.find_by_username(username)

def create_new_credential(account_name, account_password):
    """Function to create a new account and its credentials"""
    new_credential = Credential(account_name, account_password)
    return new_credential


def save_new_credential(credential):
    """Function to save the newly created account and password"""
    credential.save_credential


def find_credential(account_name):
    """Function that finds credentials based on account_name given"""
    return Credential.find_by_name(account_name)


def check_existing_credential(name):
    """Method that checks whether a particular account and its credentials exist based on searched account_name"""
    return Credential.find_by_name(name)


def display_credential():
    """Function which displays all saved credentials"""
    return Credential.display_credential()


def delete_credential(credential):
    """
    Method that deletes credentials
    """
    return Credential.delete_credential(credential)





ef main():

    while True:
        print("Welcome to PassWord Locker.")
        print('\n')
        print("Use these short codes to select an option: Create New User use 'cu': Login to your account use 'lg' or 'ex' to exit password locker")
        short_code = input().lower()
        print('\n')

        if short_code == 'cu':
        

            print("Create a UserName")
            created_user_name = input()

            print("Select a Password")
            created_user_password = input()

            print("Confirm Your Password")
            confirm_password = input()

            while confirm_password != created_user_password:
                print("Sorry your passwords did not match!")
                print("Enter a password")
                created_user_password = input()
                print("Confirm Your Password")
                confirm_password = input()
            else:
                print(f"Congratulations {created_user_name}! You have created your new account.")
                print('\n')
                print("Proceed to Log In to your Account")
                print("Username")
                entered_userName = input()
                print("Your Password")
                entered_password = input()

 while entered_userName != created_user_name or entered_password != created_user_password:
                    print("You entered a wrong username or password")
                    print("Username")
                    entered_userName = input()
                    print("Your Password")
                    entered_password = input()
                else:
                    print(f"Welcome: {entered_userName} to your Account")
                    print('\n')

                    print("Select an option below to continue: Enter 1, 2, 3, 4 or 5")
                    print('\n')

                while True:
                    print("1: View Your saved credentials")
                    print("2: Add new credentials")
                    print("3: Remove credentials")
                    print("4: Search credentials")
                    print("5: Log Out")
                    option = input()

                    if option == '2':
                        while True:
                            print("Continue to add? y/n")