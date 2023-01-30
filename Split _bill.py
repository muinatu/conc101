#PSEUDOCODE
## get the bill from the waiter  (#bill)
## count the number of people to split the bill
## decide the amount of tip to pay:(#Tip)
## add the amount of tip to bill.(#Total_bill)
## divide the total amount of bill by the total number of people to split the bill.(#bill_per_person)



# Amount of bill is assigned to variable x
x = 200.00
# amount of tip is assigned to variable y
y = 20.00
# total number of people is assigned to variable z
z = 8

# Assign Bill to x and Tip to y
Bill = x
Tip = y
# Store the total bill to be paid as Total_bill
Total_bill = Bill + Tip
# number of people splitting the total_bill
no_of_people = z
# amount to be paid by each person
bill_per_person = Total_bill / no_of_people
splitted_bill_in_words = '{0} people splitting a bill of {1:.2f} Euros should be {2:.2f} Euros each.' 

print(splitted_bill_in_words.format(no_of_people, Total_bill,bill_per_person))




