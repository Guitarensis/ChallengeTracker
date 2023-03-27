import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image
from globals import root

canvas = None
background_label = None
img = None

def add_image():
    global canvas, background_label
    
    # Open the file dialog to select an image file
    try:
        file_path = filedialog.askopenfilename(filetypes=[('Image Files', ('*.jpg', '*.png'))])
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while opening the file dialog: {str(e)}")
        return
    
    # Load the selected image using PIL
    try:
        img = Image.open(file_path)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while opening the image file: {str(e)}")
        return

    # Resize the image to fit the canvas
    img = img.resize((550, 325), Image.ANTIALIAS)

    # Set the alpha channel to 30%
    alpha = 0.3
    if img.mode == 'RGBA':
        r, g, b, a = img.split()
        a = a.point(lambda i: i * alpha)
        img = Image.merge('RGBA', (r, g, b, a))
    else:
        img.putalpha(int(alpha * 255))

    # Convert the image to a Tkinter PhotoImage
    try:
        img = ImageTk.PhotoImage(img)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while converting the image to a Tkinter PhotoImage: {str(e)}")
        return
    
    # Create the canvas if it does not exist
    if canvas is None:
        try:
            canvas = tk.Canvas(root, width=550, height=325)
            canvas.grid(row=0, column=0)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while creating the canvas: {str(e)}")
            return
    
    # Create the label if it does not exist
    if background_label is None:
        try:
            background_label = tk.Label(root, image=img)
            background_label.grid(row=0, column=0)
            background_label.image = img
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while creating the label: {str(e)}")
            return
    
    # Update the image in the label
    try:
        background_label.configure(image=img)
        background_label.image = img
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while updating the image in the label: {str(e)}")
        return
