#Welcome message
print("Welcome to the tip calculator.")

#Input the total cost of dinner
bill = float(input("What was the total bill?"))

#Input desired tip percentage
tip = float(input("What percentage tip would you like to give? 10, 12, or 15?"))

#Convert tip ammount to a percentage
tip_percentage = tip / 100

#Number of people to split the bill between
party_size = int(input("How many people to split the bill?"))

#Total tip ammount
tip_ammount = bill * tip_percentage

#Round tip to 2 decimal places
rounded_tip = round(tip_ammount, 2)
#How much does dinner cost all together + tip
total_bill = bill + tip_ammount

#Divide bill by number of members in party
individual_bill = total_bill / party_size

#Round payment amount to 2 decimal places
final_ammount = round(individual_bill, 2)

#Display how much each party member should pay
print(f"Your tip ammount is {rounded_tip}. Each person should pay: {final_ammount}")

