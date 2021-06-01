class Credential:
    '''
    class to create account credentials, generate passwords and save their information
    '''
    # creating a class Variables
    credentials_list = []
    user_credentials_list = []

    @classmethod
    def check_user(hls, first_name,password):
        '''
        Method that checks if the name and password entered match entries in the users_list
		'''
        current_user = ''
		for user in User.users_list:
			if (user.first_name == first_name and user.password == password):
				current_user = user.first_name
		return current_user

    def __init__(self,user_name,site_name,account_name,password):
        '''
		Method to define the properties for each user object will hold.
		'''
        # instance variables
		self.user_name = user_name
		self.site_name = site_name
		self.account_name = account_name
		self.password = password

        # global users_list
		Credential.credentials_list.append(self)
