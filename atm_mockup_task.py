# MOCK ATM
import random

from datetime import datetime
now = datetime.now()
date = now.strftime("%d/%m/%y")
time = now.strftime("%X")

database = {}


def init():

   print("Welcome To The Bank Of Hope")
   print(f"current time: {time}, current date: {date}")

   HaveAccount = int(input("Do You Have An Account With Us?  1. (Yes)  2. (No) \n"))

   if(HaveAccount == 1):
      login()

   elif(HaveAccount == 2):
      register()
      
   else:
      print("Invalid Option, Try Again") 
      init()



def login():
    print("*******Login To Your Account*******")

    accountNumberFromUser = int(input("Enter Your Account Number: \n"))
    password = input("Enter Your Password: \n")
    
    for accountNumber,userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[4] == password):
                bankOperations(userDetails)
               
        
    print("Invalid Account Or Password")
    login()


def register():
    print("******Registration*******")
    first_name = input("Enter Your First Name: \n")
    last_name = input("Enter Your Last Name: \n")
    email = input("Enter Your Email: \n")
    password = input("Create Your Password: \n")

    accountNumber = generateAccountNumber()
    accountBalance = 0

    database[accountNumber] = [first_name, last_name, email, accountBalance, password]

    print("Your Account Has Successfully Been Created!!!")
    print('=====  ==============  ===============   ===========')
    print("Your Account Number Is {}".format(accountNumber))
    print("=====  ==============  ===============  ============")

    login()


def bankOperations(user):
    print("Welcome {} {} To The Bank Of Hope".format(user[0], user[1]))

    print("Select An Option")
    print("(1). Withdrawal")
    print("(2). Deposit")
    print("(3). Complaint")
    print("(4) Logout")
    selectedOption = int(input("What Would You Like To Do?: \n "))

    if(selectedOption == 1):
        Withdrawal(user)

    elif(selectedOption == 2): 
        deposit(user)

    elif(selectedOption == 3):
        complain()

    elif(selectedOption == 4):
        logout() 


    else:
        print("Invalid Option, Please Try Again")                       
        bankOperations(user)


def Withdrawal(user):
    
    Withdrawalamount = int(input("How Much Would You Like To Withdraw: \n"))
    if(Withdrawalamount <= user[3]):
        print("Take Your Cash")
    else:
        print("Insufficient Funds, Please Try Again")
        Withdrawal(user)

    print("Would you like To Perform Another Transaction? (1) Yes (2) No, Logout")
    otheroption = int(input("Select Option: \n"))

    if(otheroption == 1):
        bankOperations(user)
    
    elif(otheroption == 2):
        logout()    

    else:
        logout()

def deposit(user):

    Deposit = int(input("How Much Would You Like To Deposit: \n"))
    Currentbalance = Deposit + user[3]
    print("Your Tranaction Was Successful!")
    print("Current Balance Is %s" % Currentbalance)
    
    print("Would you like To Perform Another Transaction? (1) Yes (2) No, Logout ")
    otheroption = int(input("Select Option: \n"))

    if(otheroption == 1):
        bankOperations(user)
    
    if(otheroption == 2):
        logout()

    else:
        logout()


def complain():

    Complaints = input("What Issue Would You Like To Report: \n")
    print("Thank You For Contacting Us")

    print("Would you like To Perform Another Transaction? (1) Yes (2) No")
    otheroption = int(input("Select Option: \n"))

    if(otheroption == 1):
        bankOperations(user)
    
    if(otheroption == 2):
        logout()

    else:
        logout()


def generateAccountNumber():
   
     return random.randrange(2222222222, 7777777777) 


##### BANK OPERATION ######  

def logout():
   login()

init()
