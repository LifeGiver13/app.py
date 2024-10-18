# if condition
number = 4

if number == 4:
    print("Number =4 ")

if number > 3:
    print("Number is greter than 3")

if number > 3 and number < 5:
        print("number is 4")



# if-else condition

if number %2 == 0:
     print("This is an even number")
else:
     print("This is an odd number")

''' 
ask user for a number

if number is greater than 10 tell the user it is greater than 10

If the number is less than or equal to

'''

num= int(input('Enter a number'))

if num > 10 :
    print('The number is greater than 10')
else:
     print('Number is less than equal to 10')
if num %3  == 0:
     print('Your number is a multiple of 3')
else:
     print('Your number is not a multiple of 3')

#If else checks multiple conditions

if num %2 ==0:
     print(f"{num} is an even number")
elif num %3 == 0:
     print(f"{num} is a multiple of 3")
else:
     print(f"{num} is neither an even number or a multiple of 3")


# Loops


fruits=[
     'apples',
    'bananas',
    'cherries',
    'dates'

]

for fruit in fruits:
     print(fruit)

for number in range(5):
     print(number)

for number in range(len(fruits)):
     print(f"{number + 1}. {fruits[number]}")

    #default: range (number_of_items)
    #starting position: range(starting_position, number_of_items)

for number in range(2, 7):
    print(number)
    #increment: range(number_of_items, starting_position, increment)
for number in range(2,14,3):
     print(number)
    #Ask a user for a number and output the timestable of that number from 1 to 12

times_tabl= int(input('Enter a number:'))

for num in range(1, 13):
   print(f' {times_tabl} x {num}=', times_tabl * num)

#Display only multipled of 3




