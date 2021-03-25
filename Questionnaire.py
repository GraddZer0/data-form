#Created by GraddZer0
#Written on 25/03/21
import sys
import os

while True:
    if os.path.isfile('users.txt'):
        username = str(input('Enter your username\n'))
        with open('users.txt','a+') as data:
            while True:
                input1 = str(input('Enter your name.\n> '))
                if input1.lower() == 'exit':
                    quit()
                input2 = str(input('Enter your age.\n> '))
                if input2.lower() == 'exit':
                    quit()
                input3 = str(input('Enter your Date of Birth.\n> '))
                if input3.lower() == 'exit':
                    quit()
                input4 = str(input('Enter your E-Mail.\n> '))
                if input4.lower() == 'exit':
                    quit()
                break
            data.write('\b\t\''+username+'\':{\n\t\t\'name\':\''+input1+'\',\n\t\t\'age\':\''+input2+'\',\n\t\t\'Date of Birth\':\''+input3+'\',\n\t\t\'email\':\''+input4+'\'\n\t},}')
            quit()
    else:
        with open('users.txt', 'w+') as users:
            users.write('{\n\t\'template\':{\n\t\t\'name\':\'\',\n\t\t\'age\':\'\',\n\t\t\'Date of Birth\':\'\',\n\t\t\'email\':\'\'\n\t},\n}')
            assert False, 'Restart the program, data file has been created.'
