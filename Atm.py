class Atm(object):
    """
      blueptint of atm
    """

    def __init__(self, cardnumber, pin):
        self.cardnumber = cardnumber 
        self.pin = pin

    def BalanceEnquiry(self):
        print("Your balnce is: $100")

    def CashWithdrawl(self, amount):
        new_amount = 100-amount
        print("You withdrawled: $" + str(amount) + " Your remaining balance : $" + str(new_amount)  )

def main():
        name = input("Hello what is your name ? ")
        print("Hello, " + name)
        cardnumber = input("Enter your card no. :- ")
        pin = input("Enter your pin no :-")
        new_user = Atm(cardnumber, pin)

        print("Choose you choice")
        print("1.BalanceEnqiury")
        print("2.CashWidrawl")
        activity = int(input("Enter your choice :- "))

        if(activity == 1):
            new_user.BalanceEnquiry()
        elif(activity == 2 ):
            amount = int(input("Enter the amount :- $"))
            new_user.CashWithdrawl(amount)

if __name__ == "__main__":
    main()
