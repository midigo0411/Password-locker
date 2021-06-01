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
