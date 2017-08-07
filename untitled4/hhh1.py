import math
import random

class hhh1:
    def demo(self):


        initial_number_higher=1
        initial_number_lower=100
        new_1=random.randint(1,100)
        print new_1
        while True:
            a=str(raw_input("is this the right number?"))
            if a=="yes":
                print ("game over!")
                break

            elif a=="no":

                b=str(raw_input("is this number higher or lower than your number?"))
                if b=="higher":
                    new_number=random.randint(initial_number_higher,new_1)
                    print new_number
                    new_1=new_number

                    while True:
                        b = str(raw_input("is this number higher or lower than your number?"))
                        if b=="higher":
                            new_number = random.randint(initial_number_higher, new_1)
                            print new_number
                            new_1 = new_number
                            initial_number_lower=new_number
                        else:
                            new_number = random.randint(new_1, initial_number_lower)
                            print new_number
                            new_1 = new_number




                elif b=="lower":
                    new_number=random.randint(new_1,initial_number_lower)
                    print new_number
                    new_1=new_number
                    while True:
                        b = str(raw_input("is this number higher or lower than your number?"))
                        if b=="lower":
                            new_number = random.randint(new_1, initial_number_lower)
                            print new_number
                            new_1 = new_number
                            initial_number_higher=new_number
                        else:
                            new_number = random.randint(initial_number_higher, new_1)
                            print new_number
                            new_1 = new_number


hhh1().demo()