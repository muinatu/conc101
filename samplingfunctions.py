from time import sleep
print('Waiting 5 seconds')
sleep(5)
print('Done')

#Create an initial shopping list
shopping_list = ["Bread","Milk","Apples","Chocolate"]

# Print each item in the list line by line
for item in shopping_list:
 print(item)

#Define a new function display_list
def my_function():
    print('how are you')

my_function()

'''Define another function with an argument'''
def my_function(fname):
    print(fname + ' Refsnes')

my_function('Emil')
my_function('Tobias')

'''Define another function with 2 argument'''
def my_function(fname,lname):
   print(fname +' '+ lname)

my_function('Emil','Refsnes')

##Practice Function
haiku = ['beneath',
    'leaf mold',
    'stone',
    'cool',
    'stone'] 
def display_line():
   for i in haiku:
      print(i)

display_line()

#Practice Function for height and base of a triangle
def area(height, base):
   print((height * base)/2)

area(6,20)
area(2,14)
area(5,11)

#Create a function that simulates a coin flip. 
# Each time the function is called, 
# it should randomly select either heads or tails and print it out.
import random
coin=[]
def coin_flip(head,tail):
   for x in range(10):
    print(coin.append(random.randint(head,tail)))

coin_flip(1,2)