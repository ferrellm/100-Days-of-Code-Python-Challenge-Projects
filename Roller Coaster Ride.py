print("Welcome to the rollercoaster!")
#Customer inputs their height to see if they can ride this ride
height = int(input("What is your height in cm?"))

#Cost to ride the ride, varying per age group
bill = 0

#If the customer is 120cm or taller, they can ride this ride
if height >= 120:
    print("You are tall enough to ride.")
    age = int(input("How old are you?"))
    if age <= 12:
        bill = 5
        print("Chlid tickets are $5")
    elif age <=18:
        bill = 7
        print("Youth tickets are $7")
    
    #Company policy: midlife crisis age range is free
    elif age >= 45 and age <= 55:
        bill = 0
        print("Your ticket is free")
    else:
        bill = 12
        print("Adult tickets are $12")
    wants_photo = input("Do you want a photo taken? Y  or N.")

    #Add $3 to ticket cost for photos
    if wants_photo == "Y":
        bill += 3
    print(f"Your final bill is ${bill}") 

else:
    print("You need to be taller to ride this ride.")
