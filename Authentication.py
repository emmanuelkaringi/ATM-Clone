#Register
# - First Name, Last Name, Password, email
# - Generate user account

#Login
# - email and password

#Bank Operation

#Initializing the system

import random

database = {
    9159786843: ['immah', 'stuart', '1234567890']
}

def init ():
    print("Welcome to KCB Bank")
    
    import datetime
    e=datetime.datetime.now()
    print(e.strftime("%y - %m - %d . %H : %M"))
    
    haveAccount = int(input("Do you have an Account? 1 (Yes) 2 (No) \n"))
    
    if haveAccount == 1:
        
        login()
    
    elif haveAccount == 2:
        
        register()
    
    else:
        
        print("You have selected an invalid option")

def login():
    print("*** Login ***")
    
    accountNumberfromUser = input("Enter your account number: \n")
    
    is_account_number_valid = account_number_validation(accountNumberfromUser)

    if is_account_number_valid:
        password = input("Enter your password: \n")

        for accountNumber, userDetails in database.items():
            if accountNumber == int(accountNumberfromUser):
                if userDetails[3] == password:
                    bankoperation(userDetails)

        print("Invalid account or password")
        login()
    else:
        init()
def account_number_validation(accountNumber):
    #check that account number is not empty
    #check that account number is 10 digits
    #check if account number is an integer
    if accountNumber:

        if len(str(accountNumber)) == 10:
            
            try:
                int(accountNumber)
                return True
                
            except ValueError:
                    print("Invalid Account Number")
                    return False
        
        else:
            print("Account Number should be 10 digits")
            return False
    else:
        print("Account Number cannot be empty")
        return False


def register():
    print("**** Register ****")
    email = input("Enter your Email Address here: \n")
    firstname = input("Enter Your First Name: \n")
    lastname = input("Enter Your Last Name: \n")
    password = input("Enter a suitable password \n")
    
    try:
        accountNumber = accountNumberGeneration()
    except ValueError:
        print("Account Generation Failed. Please Try Again!")
        init()
    database[accountNumber] = [ firstname, lastname, email, password ]
    
    print("Your Acoount has been created succesfully")
    print("Your account Number is: %d" % accountNumber)
    print("Keep it safe")
    print("=== === === === ===")
    
    login()

def bankoperation(user):
    print("Welcome %s %s" % ( user[0], user[1] ))
    
    selectedOption = int(input("What do you want to do? (1) Deposit (2) Withdraw (3) Exit (4) Exit \n"))
    
    if(selectedOption == 1):
        depositoperation()
    elif(selectedOption == 2):
        
        withdrawOperation()
    elif(selectedOption == 3):
        
        login()
    elif(selectedOption == 4):
        exit()
    else:
        print("Invalid option")
        bankoperation(user)

def depositoperation():
    print("deposit")

def withdrawOperation():
    print("withdraw")

def accountNumberGeneration():
    return random.randrange(1111111111,9999999999)

### Actual Banking System ###
init()