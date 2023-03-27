from buttons import menu_bar
from settingsoptions import set_option
from root import root
from tkinter import tk

def settings_menu():
    try:
        #Create the Settings sub-menu
        global settings_menu
        settings_menu = tk.Menu(menu_bar, tearoff=0)
        print('created settings sub menu')
    except Exception as e:
        raise ValueError('Error setting sub menu') from e

def settings_menu_options():
    try:
        #Add options to the Settings sub-menu
        settings_menu.add_command(label="Change Text Color", command=lambda: set_option("change_text_color"))
        settings_menu.add_command(label="Change Entry Background Color", command=lambda: set_option("change_entry_background_color"))
        settings_menu.add_command(label="Change Entry Text Color", command=lambda: set_option("change_entry_text_color"))
        settings_menu.add_command(label="Change GUI Background Color", command=lambda: set_option("change_gui_background_color"))
        settings_menu.add_command(label="Add Custom Image", command=lambda: set_option("add_image"))
        settings_menu.add_separator()
        settings_menu.add_command(label="Exit", command=quit_application)
        print('Options added')
    except Exception as e:
        raise ValueError('Error options for setting menu not added') from e

    try:    
        #Add the Settings sub-menu to the menu bar
        menu_bar.add_cascade(label="Settings", menu=settings_menu)
        print('add settings sub menu to menu bar')
    except Exception as e:
        raise ValueError('Error adding setting sub menu to menu') from e

def quit_application():
    root.destroy()
