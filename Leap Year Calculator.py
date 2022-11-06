year = int(input("Which year do you want to check? "))

#Every year that is evenly divisible by 4 is a leap year.
if year % 4 == 0:

    #"Except" every year that is evenly devisible by 100.
    if year % 100 == 0: 

        #"Unless" the year is also evenly divisible by 400.
        if year % 400 == 0:
            print*("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")

else:
    print("Not leap year.")