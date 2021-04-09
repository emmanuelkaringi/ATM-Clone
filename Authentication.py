#Register
# - First Name, Last Name, Password, email
# - Generate user account

#Login
# - email and password

#Bank Operation

#Initializing the system

import random

database = {}

def init ():
    isValidOptionSelected =  False
    print("Welcome to KCB Bank")
    import datetime
    e=datetime.datetime.now()
    print(e.strftime("%y - %m - %d . %H : %M"))

    while isValidOptionSelected == False:
        
        haveAccount = int(input("Do you have an Account? 1 (Yes) 2 (No) \n"))
        
        if(haveAccount == 1):
            isValidOptionSelected = True
            login()
        elif (haveAccount == 2):
            isValidOptionSelected = True
            print(register())
        else:
            print("You have selected an invalid option")

def login():
    print("*** Login ***")
    isLoginSuccessful = False

    while isLoginSuccessful == False:
        accountNumberfromUser = int(input("Enter your account number: \n"))
        password = input("Enter your password: \n")

        for accountNumber, userDetails in database.items():
            if (accountNumber == accountNumberfromUser):
                if(userDetails[3] == password):
                    isLoginSuccessful=True

        print("Invalid account or password")
    bankoperation(userDetails)

def register():
    print("**** Register ****")
    email = input("Enter your Email Address here: \n")
    firstname = input("Enter Your First Name: \n")
    lastname = input("Enter Your Last Name: \n")
    password = input("Enter a suitable password \n")
    
    accountNumber = accountNumberGeneration()
    
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