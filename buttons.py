from dictionary import gear_ratios
from tkinter import font
import tkinter as tk
from tkinter import ttk
from globals import root
from add_image import add_image
from font_settings import *
from all_colors import colors

color_library = colors

def menu_bar():
    try:
        # Create the menu bar
        menu_bar = tk.Menu(root)
        print('menu bar was created')
        return menu_bar
    except Exception as e:
        raise ValueError('Error menu bar did not create') from e

def file_menu():   
    try:    
        # Create the File tab
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)
        print('file menu created')
    except Exception as e:
        raise ValueError('Error creating file menu') from e

def color_get():
    global all_colors
    color_names = list((colors, neon, pastel))
    try:
        color_dropdown = ttk.Combobox(root, values=color_names)
        color_dropdown.set("Select Color")
        color_dropdown.grid(row=0, column=2)
        print('color dropdown created')
    except Exception as e:
        raise ValueError('Error creating color dropdown') from e

    def get_color():
        try:
            selected_color_name = color_dropdown.get()
            selected_color_hex = color_library[selected_color_name]
            return selected_color_hex
            print('got color')
        except Exception as e:
            raise ValueError('Error getting color') from e
    return get_color

def set_option(option):
    global font_color_window
    try:
        # Close any existing option windows
        if font_color_window:
            font_color_window.destroy()
            print('Existing font color window smashed')
    except Exception as e:
        raise ValueError('Error closing existing window') from e
    
    try:
        # Create the font and color selection window
        font_color_window = tk.Toplevel(root)
        font_color_window.title("Select Font and Color") 
        print('created font and color selection window')
   
        # Create the font family selection dropdown
        font_family_label = ttk.Label(font_window, text="Font Family:")
        font_family_label.grid(row=0, column=0, padx=5, pady=5)
        font_family_dropdown = ttk.Combobox(font_window, values=tkfont.families())
        font_family_dropdown.set("Select Font Family")
        font_family_dropdown.grid(row=0, column=1, padx=5, pady=5)
        print('Created font family selection dropdown')
    
        # Create the font size selection dropdown
        font_size_label = ttk.Label(font_window, text="Font Size:")
        font_size_label.grid(row=1, column=0, padx=5, pady=5)
        font_size_dropdown = ttk.Combobox(font_window, values=[8, 10, 12, 14, 16, 18, 20, 22, 24 , 26, 28])
        font_size_dropdown.set("Select Font Size")
        font_size_dropdown.grid(row=1, column=1, padx=5, pady=5)
        print('Created font size selection dropdown')
    except Exception as e:
        raise ValueError('Error creating font size dropdown') from e
   
        # Display the font and color selection window
        font_color_window()
        return True
        print('displaying font and color selection window')
    except Exception as e:
        raise ValueError('Error creating font family dropdown') from e
            
    if option == "change_text_color":
        # implementation for changing text color with selected_color
        print("Change Text Color to", selected_color)
    elif option == "change_entry_background_color":
        selected_color = color_get()()
        # implementation for changing entry background color with selected_color
        print("Change Entry Background Color to", selected_color)
    elif option == "change_entry_text_color":
        selected_color = color_get()()
        # implementation for changing entry text color with selected_color
        print("Change Entry Text Color to", selected_color)
    elif option == "change_gui_background_color":
        # call the add_image function to get the image
        selected_color = color_get()()
        # set the background image of the root widget
        background_label = tk.Label(root, image=img)
        background_label.place(relwidth=1, relheight=1)
        background_label.image = img
    elif option == "add_image":
        add_image()

def settings_menu():
    try:
        #Create the Settings sub-menu
        settings_menu = tk.Menu(menu_bar, tearoff=0)
        print('created settings sub menu')
    except Exception as e:
        raise ValueError('Error setting sub menu') from e

def settings_menu_options():
    try:
        #Add options to the Settings sub-menu
        menu_bar.add_cascade(label="Settings", menu=settings_menu)
        settings_menu.add_command(label="Change Text Color", command=lambda: set_option("change_text_color"))
        settings_menu.add_command(label="Change Entry Background Color", command=lambda: set_option("change_entry_background_color"))
        settings_menu.add_command(label="Change Entry Text Color", command=lambda: set_option("change_entry_text_color"))
        settings_menu.add_command(label="Change GUI Background Color", command=lambda: set_option("change_gui_background_color"))
        settings_menu.add_command(label="Add Custom Image", command=lambda: set_option("add_image"))
        settings_menu.add_command(label="Account Settings", command=open_account_settings)
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
        
def help_menu():        
    try:    
        #Create the Help sub-menu
        help_menu = tk.Menu(menu_bar, tearoff=0)
        print('Help sub menu created')
    except Exception as e:
        raise ValueError('Error creating help sub menu') from e
        
def help_menu_options():
    try:
        #Add options to the Help sub-menu
        help_menu.add_command(label="User Manual", command=open_user_manual)
        help_menu.add_command(label="Contact Us", command=open_contact_us)
        help_menu.add_command(label="About", command=open_about_window)
        print('help menu options added')
    except Exception as e:
        raise ValueError('Error adding help menu options to help menu') from e
        
    try:
        #Add the Help sub-menu to the menu bar
        menu_bar.add_cascade(label="Help", menu=help_menu)
        print('help menu added to menu bar')
    except Exception as e:
        raise ValueError('Error adding help menu to menu bar') from e

def add_menu_root():
    try:
        # Add the menu bar to the root window
        root.config(menu=menu_bar)
        print('menu bar added to root window')
    except Exception as e:
        raise ValueError('Error adding menu bar to main window') from e