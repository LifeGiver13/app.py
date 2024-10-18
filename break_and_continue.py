
# #1
# for num in range(1, 21):
#     if not num %4 == 0:
#         print(num," is not divisible by 4")
#     else:
#         continue
#         print('Number is divisible by 4')


for num in range(1, 21):
    if  num %4 ==0:
        continue
    print(num)




#2 

#while True:

  
number=[]
for num in range(5):
    num = int(input('Enter a number'))
    if num > 100:
        continue
    number.append(num)
print(number)


for j in range(1, 31):
    if j %7 == 0:
        break        
    print(j)
        


