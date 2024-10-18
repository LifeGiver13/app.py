# # # defining a simple fxn
# # '''
# # To define a  fxn we use the 'def' keyword, followed by the fxn name and brackets and end with a colon


# # deffxnName():
# #     indented code is executed as part of the fxn
# #     indented code is executed as part of


# # '''
# # def myFunction():
# #     print('This is my first fxn')

# #     '''
# #  To execute a fxn, we type the fxn name follwed by brackets

# #     '''

# # myFunction()
# # '''
# # We can execute the same block of code by calling the fxn multiple times
# # '''

# # myFunction()
# # myFunction()
# # myFunction()

# # #create a fxn called which outputs "Hello, my name is My name"

# # def myName():
# #     print("Hello my name is Fotsing")
# # myName()

# # #Global variable:
# # #Variables defined outside of any fxn are called Global variables
# # #They can be accessed from anywhere in the program
# # name = input("What's your name")

# # def greeting():
# #     print(f"Hello {name}, it's nice to meet you")
# # greeting()

# # # Variable defined inside a fxn are called Local variables
# # #They only exist inside the fxn in which they were defined


# # # yearOfBirth = int(input("What year were you born in?"))

# # # def greeting2():
# # #     age = 2024 - yearOfBirth
# # #     print(f"Hello{name}, you look like you are {age}")
# # # greeting2()

# # # def whatTimeIsIt():
# # #     print(f"The time is current: {currenttime}")

# # # whatTimeIsIt()
# # # currenttime = "7:15"

# # #Using arguments means we don't have rely on globally defined variables for our functions to work

# # # def grreeting3(name):
# # #     print(f"Hello {name}, it's nice to meet you!")

# # # grreeting3("Suhmayah")
# # # grreeting3("Ryan")
# # # grreeting3("Blessing")
# # # grreeting3("Fotsing")
# # # grreeting3("Akika")

# # # grreeting3(input("what is your name?"))

# # #Create a fxn that recieves a name and favourite colour as arguments an outputs:
# # #Hi my name is {name and my favourite color is {color}

# # n= input("Your name is?")
# # fav_color = input("Your favourite color?")

# # def grreeting4():
# #     print(f"Hello am {n}, and my best colour is{fav_color}")

# # myName = "Tancho"
# # myFavColor= "red"

# # grreeting4(myName,myFavColor)


# '''
# 1.create a fxn called calculate_area that takes 2 arguments, lenght and width, and prints the area of a rectangle

# 2. Writ a fxn called find_max that takes three numbers as arguments and returns the llargest of the three
# '''

# # #1
# # lenght= int(input('Enter the lenght of a rectangle'))
# # width= int(input("Enter the width of a rectangle"))


# def calculate_area(lenght, width):
#     area= lenght*width

#     print(f"the area is {area}")

#     calculate_area(7,4)

#     #2
# def find_max(num1, num2, num3):
#    # numbers = [num1, num2, num3]
#     # largest_number = max(number)
#     largest_number=  max(num1, num2, num3)
#     print("The largest number is", largest_number)

# find_max(28,13,15)

# #Named parameters


# def breif_intro(name, age, address):
#     print(f'Hello, my name is{name},I am {age} yr old and live in {address}')


# breif_intro("Life", "12000", "Heaven")
# breif_intro(name='GO', address="Yugiyo", age="34")
# breif_intro(7, 'cike Wu Liu', 'Seven')


# def freindly_greetings(name="freind"):
#     print(f"Hello my name is {name}, nice to meet you")


# freindly_greetings()
# # freindly_greetings('KOki')


# def is_a_prime_number(num_in_question):
#     is_prime = True
#     for num in range(2, num_in_question):
#         if num_in_question % num == 0:
#             is_prime = False
#             break

#     return is_prime


# is_prime = is_a_prime_number(73)
# print(is_prime)

# if is_prime:
#     print("73 is a prime number, you are lucky")
# else:
#     print("73 isn't a prime number")

# if is_a_prime_number(8):
#     print("this fxn is not workinf correctly")
# else:
#     is_a_prime_number(input("8 is not a prime number"))

def area_calculator(length,width):
    area= (0.5)*(length * width)
    return area
  
area1=area_calculator(12, 6)
area2=area_calculator(17, 4)
area3=area_calculator(16, 7)
area4=area_calculator(7, 62)
area5=area_calculator(34, 19)

print(f"The area of the traingle is {area1}")
print(f"The area of the traingle is {area2}")
print(f"The area of the traingle is {area3}")
print(f"The area of the traingle is {area4}")
print(f"The area of the traingle is {area5}")


largestarea= max(area5,area4,area3,area2,area1)

print('\nThe largest area is',largestarea)

#v2

traingles=[
    {'length':12, 'width':6},
{'length':17, 'width':4},
{'length':16, 'width':7},
{'length':7, 'width':62},
{'length':34, 'width':19},
]

traingles_areas=[]

for traingle in traingles:
    traingles_areas.append(area_calculator(length=traingles['length'], width=traingles['width']))
print('\n The largest area is,', max(traingles_areas))
