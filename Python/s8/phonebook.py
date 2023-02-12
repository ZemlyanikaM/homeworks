import ui
import search
import core
import exprt
import imprt

mode = -1
while mode !=5:
    
        mode = ui.main_menu()
        if mode == 0:
            ui.input_data(mode)
        elif mode == 1:
            ui.input_data(mode)
        elif mode == 2:
            ui.input_data(mode) 
        elif mode == 3:
            format = ui.export_menu()
            if format == "0":
                exprt.to_xml()
                print("Export finished. See 'phonebook.xml' file.")
                print(input("Press the 'Enter' to return the main menu"))
            elif format == '1':
                exprt.to_html()
                print("Export finished. See 'phonebook.html' file.")
                print(input("Press the 'Enter' to return the main menu"))
        elif mode == 4:
            imprt.from_xml()
            print("Import finished.")
            print(input("Press the 'Enter' to return the main menu"))
        else:
            print("The wrong mode. Try again.")
