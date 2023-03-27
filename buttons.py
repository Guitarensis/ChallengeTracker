from addimage import add_image
from allcolors import colors
from root import root
from settings import settings_menu, settings_menu_options
import tkinter as tk
from tkinter import ttk

def menu_bar(root):
    try:
        global menu_bar
        menu_bar = tk.Menu(root)
        print('menu bar created')
    except Exception as e:
        raise ValueError('Error creating menu bar') from e
        
    settings_menu()
    settings_menu_options()
    
    if "add_menu_root" in globals():
        add_menu_root()

    else:
        raise ValueError('Error creating menu bar') from e

def file_menu(menu_bar):   
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
    
    try:
        color_dropdown = ttk.Combobox(root, values=colors)
        color_dropdown.set("Select Color")
        color_dropdown.grid(row=0, column=2)
        print('color dropdown created')
    except Exception as e:
        raise ValueError('Error creating color dropdown') from e

    def get_color():
        try:
            selected_color_name = color_dropdown.get()
            selected_color_hex = colors[selected_color_name]
            print('got color')
            return selected_color_hex
        except Exception as e:
            raise ValueError('Error getting color') from e

    return get_color

def add_menu_root():
    try:
        # Add the menu bar to the root window
        root.config(menu=menu_bar)
        print('menu bar added to root window')
    except Exception as e:
        raise ValueError('Error adding menu bar to main window') from e
