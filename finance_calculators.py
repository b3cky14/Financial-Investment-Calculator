import math

# use the input function to decide investment or bond
# use .lower() function so the capitlisation shouldn't effect it being recognised
calc = input('''
Investment - To calculate the amount of interest you'll earn on your investment 
Bond - To calculate the amount you'll have to pay on a home loan
Enter either 'Investment' or 'Bond' from the menu above to proceed: 
''').lower()


# if statement if investment was chosen
if calc == "investment":
    money = int(input("How much money are you depositing? "))
    rate = int(input("What is your interest rate? "))
    time = int(input("How many years do you plan to invest for? "))
    interest = input("Do you want 'simple' or 'compound' interest? ").lower()
    # if statment if simple interest was chosen
    if interest == "simple":
        total = round(money * (1 + (rate/100)*time),2)
        print(f"You will get £{total} after {time} years at an interest rate of {rate}%. ")
    # elif statement if compound interest was chosen
    elif interest == "compound":
        total = round(money * math.pow((1 + (rate/100)),time),2)
        print(f"You will get £{total} after {time} years at an interest rate of {rate}%. ")
    # else statment if neither simple or compound was chosen
    else:
        print("You have not chosen simple or compound correctly, please check your spelling. ")


# elif statement if bond was chosen
elif calc == "bond":
    value = int(input("What is the present value of your house? "))
    rate = int(input("What is your interest rate? "))
    time = int(input("How many months do you plan to repay your bond in? "))
    monthly_rate = (rate/100)/12
    repay = round((monthly_rate * value)/(1 - (1 + monthly_rate)**(-time)),2)
    print(f"You will have to repay £{repay} each month for {time} months. ")


# else statement if neither investment or bond was chosen
else:
    print("You have not chosen investment or bond correctly, please check your spelling. ")
