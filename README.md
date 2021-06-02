# Password Locker

## Built By [Elvis Midigo](https://github.com/midigo0411/Password-locker/)

## Description
Password Locker is a terminal run python application that allows users to store details i.e. usernames and passwords of their various accounts.

## User Stories
These are the behaviours/features that the application implements for use by a user.

As a user I would like:
* To create an account with my details - log in and password
* Store my existing login credentials
* Generate a password for a new credential/account
* Copy my credentials to the clipboard

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display codes for navigation | **In terminal: $./password_locker.py** | Welcome, choose an option: nu-Create Account, lg-Log In, ex-Exit |
| Display prompt for creating an account | **Enter: nu** | Enter your first name, last name and password |
| Display prompt for login in | **Enter: lg** | Enter your account name and password |
| Display codes for exiting | **Successful login** | Choose an option, ex - exit |


## SetUp / Installation Requirements
### Prerequisites
* python3.6
* pip
* pyperclip


### Cloning
* In your terminal:
        
        $ git clone git@github.com:midigo0411/Password-locker.git
        $ cd Password_Locker

## Running the Application
* To run the application, in your terminal:

        $ chmod +x password_locker.py
        $ ./password_locker.py
        
## Testing the Application
* To run the tests for the class file:

        $ python3.6 user_credentials_test.py
        
## Technologies Used
* Python3.6

## License
MIT &copy;2021 [Elvis Midigo]
