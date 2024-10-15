print ("Welcome to the tip calculator")
Bill = float(input("What was the total bill? £ \n"))
Tip = int(input("What percentage tip would you like to give? 10, 12, 15 \n "))
people = int(input("How many people would you like to split the bill between? \n"))
Tip_as_percent = Tip / 100
Total_tip_amount = Bill * Tip_as_percent
Total_bill = Bill + Total_tip_amount 
Bill_per_person = Total_bill / people
Final_amount = round(Bill_per_person, 2) 
print(f"Each person should pay: ${Final_amount}")