import os

def show_contacts(file_name):
    os.system('CLS')
    with open(file_name, 'r') as file:
        data = file.readlines()

        for contact in data:
            print(contact)
    input('Press any key ')

def search_contact(file_name):
    os.system('CLS')
    with open(file_name, 'r') as file:
        contacts = file.readlines()

        target = input('Enter setchnig name: ').capitalize()

        for contact in contacts:
            if target in contact:
                print(contact)
                break
        else:
            print('Contact does not exist or you made a misprint')
    input('Press any key ')

def add_contact(file_name):
    os.system('CLS')
    with open(file_name, 'a') as file:
        res = '\n'
        res += input('Enter surname: ').replace(' ','').capitalize() + ' '
        res += input('Enter first name: ').replace(' ','').capitalize() + ' '
        res += input('Enter phone number: ').replace(' ','') 
        
        file.write(res)
    input('Press any key ')

def draw_menu():
    print('1 - show contacts')
    print('2 - search contact')
    print('3 - add contact')
    print('4 - delet contact')
    print('5 - change contact')
    print('6 - exit')

def delet_contact(file_name):
    os.system('CLS')
    with open(file_name, 'r') as file:
        data = file.readlines()

    with open(file_name, 'w') as file:
        target = input('Enter searchnig name: ').capitalize()
        size = len(data)
        temp = []
        j = 0

        for i in range(size):
            if target in data[i]:
                temp += ['']
                temp[j] = data[i]
                j += 1
            
        if j > 1:
            print('We found some contacts: \n{}'.format(temp))
            x = int(input('Choose number 1 - {}: '.format(len(temp))))
            while x > len(temp):
                x =int(input('Your chosen number is out of range! Chose another: '))
            j = 0
            for content in data:
                if temp[x-1] != content:
                    file.write(content)
        else: 
            for content in data:
                if target not in content:
                    file.write(content)
        
    input('Contact successfully deleted.\nPress any key to return to main menu')

def change_contact(file_name):
    os.system('CLS')
    with open(file_name, 'r') as file:
        data = file.readlines()
    with open(file_name, 'w') as file:
        target = input('Enter searchnig name: ').capitalize()
        size = len(data)
        temp = []
        j = 0
        x = 0

        for i in range(size):
            if target in data[i]:
                temp += ['']
                temp[j] = data[i]
                j += 1
            
        if j > 1:
            print('We found some contacts: \n{}'.format(temp))
            x = int(input('Choose number 1 - {}: '.format(len(temp))))
            while x > len(temp):
                x = int(input('Your chosen number is out of range! Chose another: '))
        print('What you want to change in contact?\n{}'.format(temp[x-1]))
        tempsplit = temp[x-1].split()
        y = int(input('Сhoose the word number 1 - 3: '))
        change = input('Enter the change we will make: ').capitalize()
        tempsplit[y-1] = change
        for i in range(len(data)):
            if data[i] == temp[x-1]:
                file.write(' '.join(tempsplit) + '\n')
            else:
                file.write(data[i])
        input("Changes applied!\nPress any key to return to main menu")

def main():
    while True:
       os.system('CLS')
       draw_menu()

       tmp = int(input('Enter chosen number: '))
       if tmp == 1:
           show_contacts('Data.txt')
       if tmp == 2:
           search_contact('Data.txt')
       if tmp == 3:
           add_contact('Data.txt')
       if tmp == 4:
           delet_contact('Data.txt')
       if tmp == 5:
           change_contact('Data.txt')
       if tmp == 6:
           print('Have a nice day!')
           return

    
main()


