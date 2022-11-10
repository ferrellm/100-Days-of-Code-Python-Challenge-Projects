# Your program should print each number from 1 to 100 in turn.

# When the number is divisible by 3 then instead of printing the number it should print "Fizz"
 
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".

# If the number is divisible by both 3 and 5 e.g. 15 then instead of the nubmer it should print "FizzBuzz"



#Specify the numbers 1 - 100
for number in range(1, 101):
    
    #If the number is divisible by 3, print Fizz, if its divizible by 3 & 5, print FizzBuzz
    if number % 3 == 0:
        if number % 5 == 0:
            number = "FizzBuzz"
        else:
            number = "Fizz"
    
    #If the number is only divisible by 5, print Buzz.
    elif number % 5 == 0:
        number = "Buzz"

    #Print results from 1-100
    print(number)