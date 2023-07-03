# USSD program to withdraw,check balance,send money,buy airtime,
user={
    "Name":"Mike",
    "Agent_no":'4463',
    "Pin":'2342',
    "Balance":1000
}
def menu():
    print(f"Hello {user['Name']}, \n Welcome to Safaricom")
    print("What do you want to do?")
    print("1. Withdraw Money")
    print("2. Check Balance")
    print("3. Send Money")
    print("4. Buy Airtime")
    
def Withdraw(withdraw_amount):
    transaction_fee=30
    menu()

    option=input("Select your Option: ")
    if option =="1":
        # check if the balance is more than the withdraw_amount
        # if user['Balance'] <= withdraw_amount:
        #     print(f"Sorry {user['Name']} \n Insufficient balance!!! ")
        if user['Balance'] < (withdraw_amount + transaction_fee):
            print("Failed \n You must have the transaction fee to complete this request")
        else:
            # prompt user to input agent number
            agent_no=input("Enter Agent number: ")
            if agent_no != user['Agent_no']:
                print("Wrong/ Invalid agent number")
            else:
                pin=input("Enter your pin: ")
                if pin != user['Pin']:
                    print("Wrong pin. \n Try again later")
                    # withdraw_amount(amount)
                else:
                    new_balance=user['Balance'] -(withdraw_amount + transaction_fee)
                    print(f"Withdrawal Successful You have withdrawn {withdraw_amount} from agent number {user['Agent_no']}  \n Your new balance is {new_balance} \n Thank you being Our esteemed Customer")            
    else:
        print("Sorry!!1 Service On Progress")        
    
# Withdraw(900)
        
    
    
    