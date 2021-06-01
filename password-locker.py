import random
from user import User

def create_user(fname,lname,password):
	'''
	Function to create a new user account
	'''
	new_user = User(fname,lname,password)
	return new_user

def save_user(user):
	'''
	Function to save a new user account
	'''
	User.save_user(user)


def verify_user(first_name,password):
	'''
	Function that verifies the existance of the user before creating credentials
	'''
	checking_user = Credential.check_user(first_name,password)
	return checking_user

def generate_password():
	'''
	Function to generate a password automatically
	'''
	gen_pass = Credential.generate_password()
	return gen_pass

def create_credential(user_name,site_name,account_name,password):
	'''
	Function to create a new credential
	'''
	new_credential=Credential(user_name,site_name,account_name,password)
	return new_credential

def save_credential(credential):
	'''
	Function to save a newly created credential
	'''
	Credential.save_credentials(credential)

def display_credentials(user_name):
	'''
	Function to display credentials saved by a user
	'''
	return Credential.display_credentials(user_name)
	
def copy_credential(site_name):
	'''
	Function to copy a credentials details to the clipboard
	'''
	return Credential.copy_credential(site_name)


def main():
    while True:
        print("Thank you for joining password locker")
        print('\n')
        print("pick a code to navigate through:to create new user use 'nu':To login into your account 'lg' or 'ex' to exit")
        short_code = input().lower()
        print('\n')
        if short_code == 'nu':
            print('create username')
            created_user_name = input()
            print('create password')
            created_user_password = input()
            print('confirm password')
            confirm_password = input()
            while confirm_password != created_user_password:
                print('invalid password did not match!')
                print('enter your password')
                created_user_password = input()
                print('confirm your password')
                confirm_password = input()
            else:
                print(f"congratulations{created_user_name}!account creation successful")
                print('\n')
                print("proceed to login")
                print("username")
                entered_username = input()
                print("your password")
                entered_password = input()
            while entered_username != created_user_name or entered_password != created_user_password:
                print("invalid username or password")
                print("username")
                entered_username = input()
                print("your password")
                entered_password = input()
            else:
                print(f"welcome: {entered_username} to your account")
                print("\n")
        elif short_code == 'lg':
            print("welcome")
            print("Enter user name")
            default_user_name = input()
            print("Enter password")
            default_user_password =input()
            print('\n')
            while default_user_name != 'testuser' or default_user_password != '09876':
                print("wrong userName or password.Username 'testuser' and password '09876'")
                print("Enter user name")
                default_user_name = input()
                print("Enter password")
                default_user_password = input()
                print("\n")
            else:
                print("login success")
                print('\n')
                print('\n')
        elif short_code == 'ex':
            break
        else:
            print("Enter valid code to continue")
if __name__ == '__main__':
    main()
            
