class Atm:
    def __init__(self):
        self.pin = None
        self.balance = 0
        print('Executed')
        self.menu()


    def menu(self): #funcetion == method 
        user_input = int(input('''
        Hi, How can I help you?.
        1. Press 1 to create pin.
        2. Press 2 to change pin.
        3. Press 3 to check balance.
        4. Press 4 to withdrawl.
        5. Anything else to do.
                               
        Enter Option :-                       
            '''))
        
        if user_input == 1:
            self.create_pin()
        elif user_input == 2:
            self.change_pin()

        elif user_input == 3:
            self.check_Balance()
        elif user_input == 4:
            pass
        else:
            print('Thank you')
            return

    def create_pin(self): #function == method 
        user_pin = int(input('Enter your pin:- '))
        self.pin = user_pin

        user_balance = int(input('Enter your balance:- '))
        self.balance = user_balance

        print('Created Pin succesfully')

        self.menu()

    def change_pin(self):
        user_old_pin = int(input('Enter your old Pin'))
        if user_old_pin == self.pin:
            new_pin = int(input('Enter your new pin'))
            self.pin = new_pin
            print('Your pin is change succesfully')
        else:
            print('Your old pin id incorrect')
        
        self.menu()
    
    def check_Balance(self):
        user_pin = input('Enter your Pin')
        if user_pin == self.pin:
            print('Your balance is', self.balance)
        else:
            print('Please check your PIN')

        self.menu()

    def withdrawl(self):
        user_input = input('Please enter your Pin')
        if user_input == self.pin:
            amount= int(input('Please enter Amount'))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print('Withdrawl sucessfully')
            else:
                print('Insufficent balance')
        else:
            print('Your ATM pin is incorrect')
        self.menu()

obj = Atm()