#request input of 2 digits from user
users_numbers = input("Enter a two digit number:\n")

#seperate input into 2 seperate variables
first_digit = users_numbers[0]
second_digit = users_numbers[1]

#convert those variables from string to intiger
results = int(first_digit) + int(second_digit)

#print the addition of those 2 seperate variables
print(results)