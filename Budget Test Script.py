#Mike's budget in program form

#Pay periods per year
weekly_pay_period = 52
bi_weekly_pay_period = 26
semimonthly_pay_period = 24
monthly_pay_period = 12

#User's last income (gross)
print("How much money were you given in your last paycheck?")

paycheck= input("Gross pay from last check:")
paycheck = float(paycheck)


##Calculating annual grose pay based on last paycheck and number of pay periods

#User's weekly annual gross pay
weekly_annual_income = paycheck * weekly_pay_period

#User's bi-weekly annual gross pay
bi_weekly_annual_income = paycheck * bi_weekly_pay_period

#User's semimonthly annual gross pay
semimonthly_annual_income = paycheck * semimonthly_pay_period

#User's monthly annual gross pay
monthly_annual_income = paycheck * monthly_pay_period


###Federal income taxes

#Bi Weekly Pay - Annual Taxable income TO BE DEDUCTED***
single_annual_rate_10 = bi_weekly_annual_income * .10
single_annual_rate_12 = (bi_weekly_annual_income - 9950) * .12 + 995
single_annual_rate_22 = (bi_weekly_annual_income - 40525) * .22 + 4664
single_annual_rate_24 = (bi_weekly_annual_income - 86375) * .24 + 14751
single_annual_rate_32 = (bi_weekly_annual_income - 164925) * .32 + 14751
single_annual_rate_35 = (bi_weekly_annual_income - 209425) * .35 + 47843
single_annual_rate_37 = (bi_weekly_annual_income - 523600) * .37 + 157804.25




print ("""How often do you recieve a paycheck?

1 - weekly
2 - bi-weekly
3 - semimonthly
4 - monthly""")

pay_period = input("Please enter a number:")

if pay_period == "1":

    #this will be the weekly pay period category
    print("I will earn "+str(weekly_annual_income)+" this year")

if pay_period == "2":
   
    #this will be the weekly pay period category
    print("I will earn "+str(bi_weekly_annual_income)+" this year")

        #Net income after federal taxes
    if weekly_annual_income <= 9950:
        print(float(weekly_annual_income - single_annual_rate_10))

    elif weekly_annual_income >= 9951 <= 40525:
        print(float(weekly_annual_income - single_annual_rate_12))

    elif weekly_annual_income >= 40526 <= 86375:
        print(float(weekly_annual_income - single_annual_rate_22))

    elif weekly_annual_income >= 86376 <= 164925:
        print(float(weekly_annual_income - single_annual_rate_24))
    
    elif weekly_annual_income >= 164925 <= 209425:
        print(float(weekly_annual_income - single_annual_rate_32))   

    elif weekly_annual_income >= 209425 <= 523600:
       print(float(weekly_annual_income - single_annual_rate_35))   
    
else: 
    print(float(weekly_annual_income - single_annual_rate_37))  

if pay_period == "3":

    #this will be the weekly pay period category
    print("I will earn "+str(semimonthly_annual_income)+" this year")

if pay_period == "4":
   
    #this will be the weekly pay period category
    print("I will earn "+str(monthly_annual_income)+" this year")








