class Atm:
    # constructor (special function)
    def __init__(self):
        print(id(self))
        self.pin = " "
        self.balance = 0
    def get_balance(self):
        return self.balance
    def set_balance(self, new_value):
        if type(new_value)==int:
            self.balance = new_value
        else:
            print("Invalid Input")
    def menu(self):
        user_input= input("""
        Hi! how can I help you?
        > Press 1 to create pin
        > Press 2 to change pin
        > Press 3 to check balance
        > Press 4 to withdraw
        > Anyhing else to exit
        """)
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.change_pin()
        elif user_input == "3":
            self.get_balance()
        elif user_input == "4":
            self.set_balance()
        else:
            exit()
    def create_pin(self):
        user_pin = input("Enter your pin")
        self.pin = user_pin
        user_balance = int(input("Enter balance"))
        self.balance = user_balance
        print("Pin created successfully")
    def change_pin(self):
        old_pin = input("Enter old pin")
        if old_pin == self.pin:
            new_pin = input("Enter new pin")
            self.pin = new_pin
            print("Pin changed successfully")
        else:
            print("Wrong pin")
    def check_balance(self):
        user_input = input("Enter your pin")
        if user_input == self.pin:
            print("Your balance", self.balance)
        else:
            print("Wrong Pin")
    def withdraw(self):
        user_input = input("Enter your pin")
        if user_input == self.pin:
            amount = int(input("Enter the amount"))
            if amount<=self.balance:
                self.balance -=amount
                print("Withdrawl Successful, Current Balance: ",self.balance)
            else:
                print("Insufficient Balance")
        else:
            print("Invalid Pin")
myAc = Atm()
myAc.create_pin()
