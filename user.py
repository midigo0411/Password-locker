class User:
    '''
    Class to Create user accounts and save their information
    '''
    users_list = []
    def __init__(self, first_name,last_name):
        '''
        Method to define the properties for each user object will hold.
        '''
        # instance variables
        self.first_name = first_name
		self.last_name = last_name
		self.password = password
