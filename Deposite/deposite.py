Balance_path = "Bank_Details/bank_balance.txt"
def deposite():
    while True:
        print('  '*20+"Enter the amount you want to deposite")
        try:
            amount=int(input('  '*20))
        except ValueError:
            print('  '*20+"Enter the number only")
            continue
        printing_paper=input('  '*20+"Do you want a printing recept (YES/NO): ")

        with open(Balance_path,'r') as f:
            Bank_amount=[int(line)for line in f if line.strip().isdigit() ]
            print('  '*20+f"Available balance is {Bank_amount}")

            with open(Balance_path,'r') as new_file:
                Available_amount=int(new_file.read().strip())

                new_balance=Available_amount + amount
                if printing_paper=="YES":
                    with open(Balance_path,'w') as file:
                        file.write(str(new_balance))
                    print('  '*20+f"Total balance after new deposite is {new_balance}")
                else:
                    with open(Balance_path,'w') as file:
                        file.write(str(new_balance))


        return

