import pyperclip
from credentials import Credential
from user import User


def create_user(fname,lname,password):
	'''
	Function to create a new user account
	'''
	new_user = User(fname,lname,password)
	return new_user