
import unittest
from credential import Credential
class TestCredential(unittest.TestCase):

    """
    Test class that defines test cases for the credential class behaviours,
    the arguments help in creating test cases.
    """

    def setUp(self):

        """
        this method runs before each test case, carries the instrctions of what is to be done
        """

        self.new_credential = Credential("facebook","123456")

    def test_init(self):

        """
        used to test if the objects have been initialized properly
        """

        self.assertEqual(self.new_credential.account_name,"facebook")
        self.assertEqual(self.new_credential.account_password,"123456")


    def test_save_credentials(self):
        """Method that tests whether the new credential created has been saved"""
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_detail), 1)

    def test_save_multiple_credential(self):
        """Method that saves multiple credentials to credentials_list"""
        self.new_credential.save_credential()
        new_test_credential = Credential("Twitter", "56789")
        new_test_credential.save_credential()
        self.assertEqual(len(Credential.credential_detail), 2)

    def tearDown(self):
        """Method that clears the credentials_list after every test to ensure that there is no error"""
        Credential.credential_detail = []

    def test_find_credential_by_name(self):
        """Test to check if we can find credentials and display information"""
        self.new_credential.save_credential()
        new_test_credential = Credential("Twitter", "56789")
        new_test_credential.save_credential()

        found_credential = Credential.find_by_name("Twitter")

        self.assertEqual(found_credential.account_name, new_test_credential.account_name)

    def test_display_all_credential(self):
        """TestCase to test whether all contacts can be displayed"""
        self.assertEqual(Credential.display_credential(), Credential.credential_detail)



if __name__ == '__main__':
    unittest.main()