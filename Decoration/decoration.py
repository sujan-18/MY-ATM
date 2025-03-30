import random
import time
def decoration():
    print()
    print('  '*20 +"Welcome to our ABC bank ATM".upper() + '  '*20)
    print()
    # time.sleep(random.randint(0,4)) It include time range from 0 to 4 with including last value
    time.sleep(random.randrange(0,5))#It never include last value...it always ends before last value 
    print('  '*20 +"Insert your pin number" + '  '*20 )



