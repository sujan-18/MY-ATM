
pin_path="Bank_Details/pin_number.txt"
def insert_pin():
    attempt=3
    while attempt>0:
        pin_number=input('  '*20 )
        if len(pin_number)!=4 or not pin_number.isdigit():  #checking the length of pin and make sure user input only digit
            print('  '*20 +"Invalid pin number!!" + '  '*20)
        with open(pin_path,'r') as pin:
            for my_pin in pin:
                if pin_number==my_pin.strip():  #remove new line characters
                    print('  '*20 + "Successfully logged in" + '  '*20)
                    from Accept_pin.pin_successfull import pin_successfull
                    pin_successfull()
                    return #exit function on success
                
            #if pin doesnot match with our pin then it came into this line
                attempt-=1
            
                print('  '*20 + f"Now you have {attempt} attempt remaining!!" + '  '*20)
    if attempt==0:
        print('  '*20 + "Maximum attempt..Please inform your nearest branch!!" + '  '*20)
        exit()



    

