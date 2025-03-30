import time
import random
def pin_successfull():
    time.sleep(random.randrange(0,3))
   
    while True:
        print('  '*20 +"Choose your language type")
        print()
        print('  '*20 +"1. English                 2. Nepali")
        print()
        input_number=input('  '*20).strip()

        if input_number=="1":
    
            print('  '*20+"What do you want to perform from this ATM")
            print()
            print('  '*20+"1. Withdraw                 2. Deposite")
            print()
            print('  '*20+"Enter the number (1/2) for choice")
            choice=input('  '*20)
            if choice=="1":
                from functions.withdrew_function import withdrew_function
                withdrew_function()
                return
            elif choice=="2":
                from Deposite.deposite import deposite
                deposite()
                return
            else:
                print('  '*20+"Invalid choice choose(1/2)")

        elif input_number=="2":
            print('  '*20+"This service is not available right know")
            pin_successfull()

        else:
            print('  '*20+"Out of range!!Input(1/2)")
        return
                



