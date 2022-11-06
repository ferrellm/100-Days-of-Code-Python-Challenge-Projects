# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#Define how many days, weeks & months are in a year
days = 365
weeks = 52
months = 12

#convert age to integer
n_age = int(age)

#How many years left until 90
life = 90 - n_age 

#Output
print(f"You have {days * life} days, {weeks * life} weeks, and {months * life} months left.")