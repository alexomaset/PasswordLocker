
import unittest # Importing the unittest module
from user import User # Importing the contact class

class TestContact(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("facebook", "amiredin" ,"123456", "123456") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.account_name,"facebook")
        self.assertEqual(self.new_user.user_name,"amiredin")
        self.assertEqual(self.new_user.password,"123456")
        self.assertEqual(self.new_user.confirm_password,"123456")



    def test_save_multiple_detail(self):

        """
        a method to check if we can save multiple user details to our details array
        """

        self.new_user.save_detail()
        test_user = User("Test","user","123456","123456")
        test_user.save_detail()
        self.assertEqual(len(User.user_detail),3)

    def test_delete_user(self):
            '''
            test_delete_user to test if we can remove a user from our user list
            '''
            self.new_user.save_detail()
            test_user = User("Test" ,"user","0712345678","test@user.com") # new contact
            test_user.save_detail()

            self.new_user.delete_user()# Deleting a contact object
            self.assertEqual(len(User.user_detail),1)



    def test_display_all_details(self):

        """
        is a method that returns a list of all details saved
        """

        self.assertEqual(User.display_all_details(),User.user_detail)

  



if __name__ == '__main__':
    unittest.main()