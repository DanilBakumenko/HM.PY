import os
import datetime as dt
import random

def show_notes(file_name):
    os.system('CLS')
    with open(file_name, 'r') as file:
        data = file.readlines()
        for contact in data:
            print(contact)
    input('Press any key ')

def search_notes(file_name):
    os.system('CLS')
    with open(file_name, 'r') as file:
        contacts = file.readlines()
        target = input('Enter setchnig word, date or ID: ')
        for contact in contacts:
            if target in contact:
                print(contact)
            elif contact != null:
                print('Note does not exist or you made a misprint')
    input('Press any key ')

def add_note(file_name):
    os.system('CLS')
    id = random.randint(0,1000)
    with open(file_name, 'a') as file:
        res = '\n'
        res += "ID: " + str(id) + ";"
        res += "Date: " + str.format("{} {}", dt.datetime.now().date(), dt.datetime.now().strftime("%H:%M:%S")) + ";"
        res += input('Enter title ') + ";"
        res += input('Enter the note ') + ";"
        file.write(res)
    input('Press any key ')

def draw_menu():
    print('1 - show notes')
    print('2 - search note')
    print('3 - add note')
    print('4 - delet note')
    print('5 - change note')
    print('6 - exit')

def delet_note(file_name):
    os.system('CLS')
    with open(file_name, 'r') as file:
        data = file.readlines()

    with open(file_name, 'w') as file:
        target = input('Enter searchnig word, date or ID: ')
        size = len(data)
        temp = []
        j = 0

        for i in range(size):
            if target in data[i]:
                temp += ['']
                temp[j] = data[i]
                j += 1
            
        if j > 1:
            print('We found some notes: \n{}'.format(temp))
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
        
    input('Note successfully deleted.\nPress any key to return to main menu')

def change_note(file_name):
    os.system('CLS')
    with open(file_name, 'r') as file:
        data = file.readlines()
    with open(file_name, 'w') as file:
        target = input('Enter searchnig word, title or ID ')
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
            print('We found some notes: \n{}'.format(temp))
            x = int(input('Choose number 1 - {}: '.format(len(temp))))
            while x > len(temp):
                x = int(input('Your chosen number is out of range! Chose another: '))
        print('What you want to change in note?\n{}'.format(temp[x-1]))
        tempsplit = temp[x-1].split(";")
        y = int(input('Сhoos\n1)Title\n2)The note: '))
        change = input('Enter the change we will make: ')
        tempsplit[y+1] = change
        for i in range(len(data)):
            if data[i] == temp[x-1]:
                file.write(";".join(tempsplit))
            else:
                file.write(data[i])
        input("Changes applied!\nPress any key to return to main menu")

def main():
    while True:
       os.system('CLS')
       draw_menu()

       tmp = int(input('Enter chosen number: '))
       if tmp == 1:
           show_notes('Data.csv')
       if tmp == 2:
           search_notes('Data.csv')
       if tmp == 3:
           add_note('Data.csv')
       if tmp == 4:
           delet_note('Data.csv')
       if tmp == 5:
           change_note('Data.csv')
       if tmp == 6:
           print('Have a nice day!')
           return



main()

