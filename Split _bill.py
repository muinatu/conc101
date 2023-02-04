#PSEUDOCODE
## get the bill from the waiter  (#bill)
## count the number of people to split the bill
## decide the amount of tip to pay:(#Tip)
## add the amount of tip to bill.(#Total_bill)
## divide the total amount of bill by the total number of people to split the bill.(#bill_per_person)




Bill = round(float(input('Bill: ')),2)

Tip = float(input('Tip: '))

# Store the total bill to be paid as Total_bill
Total_bill = Bill + Tip

# number of people splitting the total_bill
no_of_people = int(input('number of people splitting the total bill: '))

# amount to be paid by each person
bill_per_person = round(Total_bill / no_of_people, 2)


print(str(no_of_people) + ' people splitting a total bill of ' + str(Total_bill) + ' Euros should be ' + str(bill_per_person) + ' Euros per person')




