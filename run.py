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