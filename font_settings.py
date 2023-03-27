from globals import root
from all_colors import colors

def font_color_window():
    font_family = tk.StringVar()
    font_size = tk.StringVar()
    font_color = tk.StringVar()
    entry_bg_color = tk.StringVar()
    entry_text_color = tk.StringVar()

    # Create the font options frame
    font_frame = ttk.LabelFrame(root, text="Font Options")
    font_frame.grid(row=1, column=0, padx=10, pady=10)

    # Font family dropdown
    font_family_label = ttk.Label(font_frame, text="Font Family:")
    font_family_label.grid(row=0, column=0, padx=5, pady=5)
    font_family_options = ("Arial", "Helvetica", "Times New Roman", "Courier New")
    font_family_dropdown = ttk.Combobox(font_frame, values=font_family_options, textvariable=font_family)
    font_family_dropdown.grid(row=0, column=1, padx=5, pady=5)

    # Font size entry
    font_size_label = ttk.Label(font_frame, text="Font Size:")
    font_size_label.grid(row=1, column=0, padx=5, pady=5)
    font_size_entry = ttk.Entry(font_frame, textvariable=font_size)
    font_size_entry.grid(row=1, column=1, padx=5, pady=5)

    # Font color dropdown
    font_color_label = ttk.Label(font_frame, text="Font Color:")
    font_color_label.grid(row=2, column=0, padx=5, pady=5)
    font_color_options = all_colors
    font_color_dropdown = ttk.Combobox(font_frame, values=font_color_options, textvariable=font_color)
    font_color_dropdown.grid(row=2, column=1, padx=5, pady=5)

    # Create the entry options frame
    entry_frame = ttk.LabelFrame(root, text="Entry Options")
    entry_frame.grid(row=2, column=0, padx=10, pady=10)

    # Entry background color dropdown
    entry_bg_color_label = ttk.Label(entry_frame, text="Background Color:")
    entry_bg_color_label.grid(row=0, column=0, padx=5, pady=5)
    entry_bg_color_options = all_colors
    entry_bg_color_dropdown = ttk.Combobox(entry_frame, values=entry_bg_color_options, textvariable=entry_bg_color)
    entry_bg_color_dropdown.grid(row=0, column=1, padx=5, pady=5)

    # Entry text color dropdown
    entry_text_color_label = ttk.Label(entry_frame, text="Text Color:")
    entry_text_color_label.grid(row=1, column=0, padx=5, pady=5)
    entry_text_color_options = all_colors
    entry_text_color_dropdown = ttk.Combobox(entry_frame, values=entry_text_color_options, textvariable=entry_text_color)
    entry_text_color_dropdown.grid(row=1, column=1, padx=5, pady=5)

    # Apply button
    apply_button = ttk.Button(root, text="Apply", command=apply_font_color)
    apply_button.grid(row=3, column=0, padx=10, pady=10)

def apply_font_color():
    selected_font = font_dropdown.get()
    selected_color = color_dropdown.get()
    if selected_font and selected_color:
        # implementation for applying font and color to labels and entry fields
        print("Font:", selected_font, "Color:", selected_color)
        # close the window
        font_color_window.destroy()
		
def change_font_color():
    # create the font color window
    font_color_window = tk.Toplevel(root)
    font_color_window.title("Font and Color")
    font_color_window.geometry("300x200")

    # create the font selection dropdown
    font_names = list(tkfont.families())
    font_dropdown = ttk.Combobox(font_color_window, values=font_names)
    font_dropdown.set("Select Font")
    font_dropdown.grid(row=0, column=1)

    # create the color selection dropdown
    color_names = all_colors
    color_dropdown = ttk.Combobox(font_color_window, values=color_names)
    color_dropdown.set("Select Color")
    color_dropdown.grid(row=1, column=1)

    # create the apply button
    apply_button = ttk.Button(font_color_window, text="Apply", command=apply_font_color)
    apply_button.grid(row=2, column=1)
