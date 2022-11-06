# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Combine both names into one variable and convert them to lowercase.
combined_string = name1 + name2
lower_case_string = combined_string.lower()

#Count how many of these letters are in the new string variable
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

#Combine these counts to get a total count of these letters in the phrase
true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")


love = l + o + v + e

#Combine the total value of true and print as a string into the 1st digit and the same for love as the second digit
#Convert the result into a varable.

love_score = int(str(true) + str(love))

#Define the range of results and print with comment.
if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")

elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")

else:
    print(f"Your score is {love_score}.")
