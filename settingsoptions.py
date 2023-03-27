from root import root
from tkinter import font as tkfont
from tkinter import tk
from tkinter import ttk

entry = None
selected_color = None

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
        font_family_label = ttk.Label(font_color_window, text="Font Family:")
        font_family_label.grid(row=0, column=0, padx=5, pady=5)
        font_family_dropdown = ttk.Combobox(font_color_window, values=tkfont.families())
        font_family_dropdown.set("Select Font Family")
        font_family_dropdown.grid(row=0, column=1, padx=5, pady=5)
        print('font family dropdown created')

        # Create the font size selection dropdown
        font_size_label = ttk.Label(font_color_window, text="Font Size:")
        font_size_label.grid(row=1, column=0, padx=5, pady=5)
        font_size_dropdown = ttk.Combobox(font_color_window, values=[8, 10, 12, 14, 16, 18, 20, 22, 24 , 26, 28])
        font_size_dropdown.set("Select Font Size")
        font_size_dropdown.grid(row=1, column=1, padx=5, pady=5)
        print(' font size dropdowqn created')

        # Create the text color selection button
        text_color_label = ttk.Label(font_color_window, text="Text Color:")
        text_color_label.grid(row=2, column=0, padx=5, pady=5)
        text_color_button = ttk.Button(font_color_window, text="Select Text Color", command=select_text_color)
        text_color_button.grid(row=2, column=1, padx=5, pady=5)
        print('text color selection button created')

        # Create the entry background color selection button
        entry_bg_color_label = ttk.Label(font_color_window, text="Entry Background Color:")
        entry_bg_color_label.grid(row=3, column=0, padx=5, pady=5)
        entry_bg_color_button = ttk.Button(font_color_window, text="Select Entry Background Color", command=select_entry_bg_color)
        entry_bg_color_button.grid(row=3, column=1, padx=5, pady=5)
        print(' entry background color selection button created')

        # Create the entry text color selection button
        entry_text_color_label = ttk.Label(font_color_window, text="Entry Text Color:")
        entry_text_color_label.grid(row=4, column=0, padx=5, pady=5)
        entry_text_color_button = ttk.Button(font_color_window, text="Select Entry Text Color", command=select_entry_text_color)
        entry_text_color_button.grid(row=4, column=1, padx=5, pady=5)
        print(' entry text color selection button created')

        # Create the GUI background color selection button
        gui_bg_color_label = ttk.Label(font_color_window, text="GUI Background Color:")
        gui_bg_color_label.grid(row=5, column=0, padx=5, pady=5)
        gui_bg_color_button = ttk.Button(font_color_window, text="Select GUI Background Color", command=select_gui_bg_color)
        gui_bg_color_button.grid(row=5, column=1, padx=5, pady=5)
        print('gui background color selecion button created')

        # Create the font and color submit button
        submit_button = ttk.Button(font_color_window, text="Submit", command=lambda: set_font_and_color(option, font_family_dropdown.get(), font_size_dropdown.get(), text_color_button['background'], entry_bg_color_button['background'], entry_text_color_button['background'], gui_bg_color_button['background']))
        submit_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)
        print('created font and color selection GUI')
    except Exception as e:
        raise ValueError('Error closing existing window') from e

        # Set the font and color selection window to be on top of the main window
        font_color_window.lift()
        font_color_window.attributes("-topmost", True)

    def select_text_color():
        try:
            # Open the color picker window
            selected_text_color = tk.colorchooser.askcolor()[1]
            text_color_button.configure(background=selected_text_color)
            print('selected text color')
        except Exception as e:
            raise ValueError('Error selecting text color') from e

    def select_entry_bg_color():
        try:
            # Open the color picker window
            selected_entry_bg_color = tk.colorchooser.askcolor()[1]
            entry_bg_color_button.configure(background=selected_entry_bg_color)
            print('selected entry background colopr selected')

    def select_gui_bg_color():
        try:
            # Open the color picker window
            selected_gui_bg_color = tk.colorchooser.askcolor()[1]
            gui_bg_color_button.configure(background=selected_gui_bg_color)
            print('Selected GUI background color')
        except Exception as e:
            raise ValueError('Error selecting GUI background color') from e

    def select_entry_text_color():
        try:
            # Open the color picker window
            selected_entry_text_color = tk.colorchooser.askcolor()[1]
            entry_text_color_button.configure(background=selected_entry_text_color)
            print('Selected entry text color')
        except Exception as e:
            raise ValueError('Error selecting entry text color') from e

    def set_font_and_color(option, font_family, font_size, text_color, entry_bg_color, entry_text_color, gui_bg_color):
        pass

    # Display the font and color selection window
    font_color_window.mainloop()

     # Handle the selected option
    if option == "change_text_color":
    # Change the text color based on the selected color
    if selected_color:
        root.config(fg=selected_color)
        print("Text color changed to", selected_color)
    elif option == "change_entry_background_color":

    # Change the entry background color based on the selected color
       if selected_color:
           entry.config(bg=selected_color)
           print("Entry background color changed to", selected_color)
    elif option == "change_entry_text_color":
        # Change the entry text color based on the selected color
            if selected_color:
                root.config(fg=selected_color)
                print("Entry text color changed to", selected_color)
    elif option == "change_gui_background_color":
         # Change the GUI background color based on the selected color
        if selected_color:
            root.config(bg=selected_color)
            print("GUI background color changed to", selected_color)

        # Destroy the font and color selection window
        font_color_window.destroy()
        print('Destroyed font and color selection window')

        return True
