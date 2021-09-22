# This code calculates the bill + tip per person

print("Welcome to the tip calculator.\n")
total_bill = float( input("What was the total bill? $") )
percent_tip = int( input("What percentage tip would you like to give? 10, 12, or 15? ") )
people = int( input("How many people to split the bill? ") )

bill_plus_tip = total_bill * (1 + percent_tip / 100)
bill_split = round(bill_plus_tip / people, 2)

print(f"Each person should pay: ${bill_split}")