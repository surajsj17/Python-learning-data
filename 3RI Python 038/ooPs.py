
class CarDetails():
    car_name = "McLaren"
    car_model = "750s"
    car_year = 2024
    car_price = "5.6 cores"
    drive_name = "Vin Diesel"
    def driver(self):
        return  f'{self.drive_name} is driving the car'
    def details(self,color):
        return f'The car name is {self.car_name}, the model is {self.car_model}, the year is {self.car_year}, the price is {self.car_price}, and the color is {color}'

cd = CarDetails()
print (cd.driver())
print ("--- The car details ---")
print (cd.details(color = "orange"))



'''
OUTPUT - Vin Diesel is driving the car
--- The car details ---
The car name is McLaren, the model is 750s, the year is 2024, the price is 5.6 cores, and the color is orange
           
'''


# Write the program to for withdrawal the ammount from bank ATM
class AccountDetails:
    account_holder = input("Enter account holder name: ")
    account_no = int(input("Enter account number: "))
    account_type = input("Enter account type: ")
    account_balance = 1000

    @classmethod
    def user_exists(cls):
        existing_accounts = ["suraj", "akash", "pradeep", "sumedh"]
        if cls.account_holder in existing_accounts:
            print("The account holder exists!")
        else:
            print("The account holder does not exist!")
            exit()

class TransactionDetails:
    trid = 12203403
    trid2 = 1220340312
    trid3 = 122034031234
    trid4 = 12203

    @classmethod
    def trd(cls, account_holder):
        if account_holder == "akash":
            print("The transaction ID - ",cls.trid)
        elif account_holder == "pradeep":
            print("The transaction ID - ",cls.trid2)
        elif account_holder == "sumedh":
            print("The transaction ID - ",cls.trid3)
        elif account_holder == "suraj":
            print("The transaction ID - ",cls.trid4)
        else:
            print("No matching transaction ID found.")

    @classmethod
    def withdraw(cls, account, wdAmt):
        print("Transaction Details")
        print("---------------------")
        cls.trd(account.account_holder)
        print("Transaction AccNo  :", account.account_no)
        print("Account Holder Name:", account.account_holder)
        print("Account Type       :", account.account_type)
        print("Transaction Type   : Withdraw")
        print("Withdraw Amount    :", wdAmt)
        try:
            if wdAmt <= account.account_balance:
                account.account_balance -= wdAmt
                print("Total Balance      :", account.account_balance)
                print("Transaction Status : Success")
            else:
                print("Total Balance      :", account.account_balance)
                print("Transaction Status : Failure")
                raise insufficientException ("Reason: Insufficient Funds")
        except insufficientException as e:
            print(e.description)
        finally:
            print("******** Visit Again ********")

class insufficientException(Exception):
    def __init__ (self, description):
        self.description = description

# Run the process
object1 = AccountDetails
object1.user_exists()
withdraw_amount = float(input("Enter amount to withdraw: "))
object2 = TransactionDetails
object2.withdraw(object1, withdraw_amount)

    
'''
OUTPUT:

Enter account holder name: sumedh
Enter account number: 12343
Enter account type: saving
The account holder exists!
Enter amount to withdraw: 1000 
Transaction Details
---------------------
The transaction ID -  122034031234
Transaction AccNo  : 12343
Account Holder Name: sumedh
Account Type       : saving
Transaction Type   : Withdraw
Withdraw Amount    : 1000.0
Total Balance      : 0.0
Transaction Status : Success
******** Visit Again ********
'''






