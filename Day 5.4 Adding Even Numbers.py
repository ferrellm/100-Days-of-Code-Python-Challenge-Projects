#Accumulator
#Add every number bettween 1 and 100 together
for number in range(1, 101):
    if number % 3 == 0:
        if number % 5 == 0:
            number = "FizzBuzz"
        else:
            number = "Fizz"
    elif number % 5 == 0:
        number = "Buzz"
    print(number)