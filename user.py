
class User:
  """
  class that generates new instances of user
  """

  user_detail = [] # Empty list 

  def __init__(self,account_name,user_name,password , confirm_password):

        self.account_name = account_name 
        self.user_name = user_name
        self.password = password
        self.confirm_password = confirm_password



  def save_detail(self):

        '''
        save_contact method saves contact objects into contact_list
        '''

        User.user_detail.append(self)

  def delete_user(self):

        '''
        delete_user method deletes a saved contact from the contact_list
        '''

        User.user_detail.remove(self)

  @classmethod
  def find_by_username(cls,username):
        '''
        Method that takes in a username and returns a user that matches that username.
       '''
 
        for user in cls.user_detail:
            if user.username == username:
                return user


  @classmethod
  def display_all_details(cls):

        return cls.user_detail             



  @classmethod
  def user_exist(cls,username):

        for user in cls.user_detail:
            if user.username == username:
                    return True   


  @classmethod
  def copy_email(cls,username):
        user_found = User.find_by_username(username)
        pyperclip.copy(user_found.user)            