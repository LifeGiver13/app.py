#1

for numeven in range(1,50):
    if numeven %2 == 0:
        print(numeven)



#2 Determining wether a number is a prime nimber
num= int(input('Enter a number:'))

if num %2 != 0:
    print(f'{num}is  a Prime number')
else:
    print(f"{num} is not a Prime number")

is_prime=True

for run in range(2,num):
    
    if(num)% run==0:
        is_prime =False
        break

if is_prime:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
           
#3
total=0

for num in range(1, 13):
    
    if num%3 == 0:
        total+=num
        
        print(total)





#lnum =input('Enter a number')
#4
'''
number=[]
for i in range(5):
    number = int(input(f'Enter a number {i + 1}'))
    number.append(number)
highest_number =max(number)
print(highest_number)

#5
sentence = input("Enter a string to find out how many vowels it counts:")

vowels=('a','e','i','o','u')


vowel_count = 0

for letter in sentence:
    if letter in vowel_count:
        vowel_count += 1
print (f"There are {vowel_count} vowels in the sentence'{sentence}'")

'''

#6 fibanoci sequence
x=y=1
while y < 100:
    print(y)
    x,y = y, x+y

#7

u= (input("An interger"))

currentXter= len(u) -1
reversedXter=''
while (currentXter>= 0):
    reversedXter += u[currentXter]
    currentXter -=1
print(f"{u} reversed is {reversedXter}")

#8
w=input("A palindrome")


currentword= len(w) -1
reversedword=''

while (currentword>= 0):
    reversedword += w[currentword]
    currentword -=1
    print(f"{w} reversed is {reversedword}")

if w==reversedword:
    print(w, "is a palindrome")
else:
    print(w, "is not a palindrome")


#9

    

#10


for i in range(1, 101):
    if i % 3 == 0  and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
      print("Fizz")
    elif i % 5 == 0:
        print("Buzz") 
    else:
        print(i)