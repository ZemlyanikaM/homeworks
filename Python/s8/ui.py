import core
import search
import exprt


def main_menu():
    print(" \n Welcome to the phone book. What do you want to do? \n \n \
            0 - add a new entry to the phone book \n \
            1 - find an entry by a surename \n \
            2 - show all entries in the phone book \n \
            3 - export data to a file \n \
            4 - import data from the 'phonebook.xml' file \n \
            5 - quit the program   \n ")
    mode = int(input("Choose the mode: "))
    return mode


def input_data(mode):
    data = ''
    if mode == 0:
        data += f'{input("Enter a Surename:")} '
        data += f'{input("Enter a Name: ")} '
        data += f'{input("Enter a phone number: ")} '
        data += f'{input("Enter a description: ")} \n'
        core.save_entry(data)
    elif mode == 1:
        print(search.find_entry(input("Enter a looking Surename: ")))
        print(input("Press the 'Enter' to return the main menu"))
    elif mode == 2:
        core.show_entryes()
        print(input("Press the 'Enter' to return the main menu"))
    elif mode == 3:
        
        return 0

def export_menu():
    format = input("Chose the format for expot: \n\
        0 - xml \n\
        1  html \n")    
    return format
