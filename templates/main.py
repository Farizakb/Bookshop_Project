import sys
import os
from datetime import datetime
from os.path import exists

class Book:
    def set_id(self, i):
        self.sira = i
    def set_date(self, d):
        self.date = d  


    def add(self):
        with open('book_list.txt', 'r+') as f:
            title = input('Please enter book name: ')
            writer = input('Please enter writer name: ')
            obj = f.readlines()
            self.sira = 1
            if obj:
                self.sira = int(obj[-5].split(':')[1]) + 1
            ele = f'ID : {self.sira}\nBook name : {title}\nWriter name : {writer}\nAdded in : {datetime.today().strftime("%d %B %Y")}'
            f.write(f"{ele}\n{'*' * 50}\n")


    def show_all(self):
        with open('book_list.txt', 'r+') as f:
            print('There are ',len(f.readlines())//5, 'books!')


      

    def show_book(self):
        id = input('Please enter ID: ' )
        f = open('book_list.txt', 'r+')
        obj = f.readlines()
        for i in range(0, len(obj), 5):
            search = obj[i].split(':')[1].strip()
            if id == search:
                index = i
                range_list = [index, index + 1, index + 2, index + 3, index + 4]
                for i in range(len(obj)):
                        if i in range_list:
                            print(obj[i])     
    
    def remove_book(self):
        id = input('Please enter ID: ' )
        with open('book_list.txt', 'r+') as file:
            obj = file.readlines()
            file.seek(0)
            for line in range(0, len(obj), 5):
                remove_ele = obj[line].split(':')[1].strip()
                if id == remove_ele:
                    index = line
                    range_list = [index, index + 1, index + 2, index + 3, index + 4]
                    file.truncate()
                    for i in range(len(obj)):
                        if i not in range_list:
                            file.write(obj[i])
                    print('\nSuccesfully deleted!\n')
                    break
            else:
                print('\nID does not exist!\n')




              
        
         

if not  exists('book_list.txt'):
    file = open('book_list.txt', "x")
command = sys.argv    

Kitab1 = Book()
if "add" in command:
    Kitab1.add()
elif "show" and "book" in command:
    Kitab1.show_book()
elif "all" in command:
    with open('book_list.txt', 'r+') as file:
        obj = file.readlines()
        Kitab1.show_all()
elif "remove" in command:
     Kitab1.remove_book()
else:
    print('Wrong input!')













