class Credential:
    """
    Class that will generate new instances of credentials
    """


    credential_detail = []

    def __init__(self,account_name,account_password):

        """
        the __init__method helps us define properties for our objects.
        """


        self.account_name = account_name
        self.account_password = account_password


        """
        arguments for our __init__method will include the following.
        """


    def save_credential(self):
        """Method that saves credential objects into credentials_list"""
        self.credential_detail.append(self)

    def delete_credential(self):
        """Method which deletes a particular credential"""
        Credential.credential_detail.remove(self)

    @classmethod
    def find_by_name(cls, account_name):
        """Method that takes in a name and returns a credential that matches that particular name
        Args:
            name: account_name that has a password
        Returns:
            The account_name and it's corresponding PassWord
        """

        for credential in cls.credential_detail:
            if credential.account_name == account_name:
                return credential

    @classmethod
    def credential_exists(cls, name):
        """Method to check whether a credential exists
        Args:
        name: name of account to search whether it exists
        boolean: True or False depending if the contatc exists
        """

        for credential in cls.credential_detail:
            if credential.account_name == name:
                return True
        return False

    @classmethod
    def display_credential(cls):
        """Method which displays all current credentials"""
        return cls.credential_detail
