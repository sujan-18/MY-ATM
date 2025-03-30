Balance_path = "Bank_Details/bank_balance.txt"
withdraw_path = "Bank_Details/withdraw.txt"

def withdrew_function():
    while True:
        # Display withdrawal options
        print('  '*20 + "You can withdraw")
        print('  '*20 + "2000                 5000")
        print('  '*20 + "10000                20000")
        
        # Get withdrawal amount
        try:
            withdraw = int(input('  '*20 + "Enter the withdraw amount: "))
        except ValueError:
            print('  '*20 + "Invalid amount! Please enter numbers only.")
            continue
        printing_paper=input('  '*20 + "Do you need printing recept :(YES/NO)")
        
        # Load available withdrawal amounts
        with open(withdraw_path, 'r') as file:
            amounts = [int(num.strip()) for num in file.read().split(',') if num.strip().isdigit()]
            
            # Check if entered amount is valid
            if withdraw not in amounts:
                print('  '*20 + "Invalid amount! Please choose from the options.")
                continue
                
            # Process balance update
            with open(Balance_path, 'r') as f:
                current_balance = int(f.read().strip())
                
                if withdraw > current_balance:
                    print('  '*20 + "Insufficient balance!")
                    continue
                    
                # Update balance
                new_balance = current_balance - withdraw
                
                if printing_paper=="YES":
                   
                 with open(Balance_path, 'w') as f:
                    f.write(str(new_balance))
                    print('  '*20 + f"Withdrawal successful! New balance: {new_balance}")
                else: 
                 
                 with open(Balance_path, 'w') as f:
                    f.write(str(new_balance))

        return  # Exit after successful transaction