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
