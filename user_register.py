options = ('Save', 'Retrieve')
choice = ''


user_data = {
    'firstName': "First Name",
    'lastName' : "Last Name",
    'emailaddress':"Email Address",
    "password": "Password",
}

while (choice not in options):
    choice= input("Enter Save or Retrieve to  save or collect  you email address: ")


if choice == "Save":

    userInfo= {}

    for feild in user_data.keys():
        userInfo[feild] = input(f'Enter your {user_data[feild]}:')

    user_file = open(f"{userInfo['emailaddress']}.txt",'w')

    for prop in userInfo.keys():
        user_file.write(f'{prop}:{userInfo[prop]}\n')
    user_file.close()
 
else:
    '''
    else block start
    '''
    emailaddress = ''
    while emailaddress =='' :
        emailaddress= input(f"Enter your previously used emailaddress: ")
    
    user_file = open(f"{emailaddress}.txt",'r')

    userD= {}

    for property in user_file:
        item = property.split(":")
        userD[item[0]]=item[1].strip("\n")

        print(userD)

        print('Yo, nice reading you are alive',userD['firstName'])
       
    '''
    else block end
        '''








