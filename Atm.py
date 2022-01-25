class Atm:
    def __init__(self,cardNumber,pin):
        self.cardNumber=cardNumber
        self.pin=pin
    def checkBalance(self):
        print("Your balance is $50,000")
    def withdrawal(self,amount):
        newAmount=50000-amount
        print("You have withdrawn "+str(amount)+"Your remaining balance is "+str(newAmount))
def main():
    CardNumber=input("Insert your Card Number ")
    pinNumber=input("Enter the Pin Number")
    newUser=Atm(CardNumber, pinNumber)
    print("1. Balance Inquiry 2. Withdrawal")
    activity=int(input("Enter the activity- "))
    if(activity == 1):
        newUser.checkBalance()
    elif(activity == 2):
        amount=int(input("Enter the amount- "))
        newUser.withdrawal(amount)
    else:
        print("Enter a valid number")

main()