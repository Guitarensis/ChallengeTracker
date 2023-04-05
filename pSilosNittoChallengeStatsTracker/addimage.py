from root import root
from PIL import ImageTk, Image
from tkinter import filedialog, messagebox
import tkinter as tk

title = "pSilos Nitto Challenge Stats Tracker"

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Add Image")

        # Create a button to select an image
        self.button = tk.Button(self.master, text="Select Image", command=self.add_image)
        self.button.pack()
        
        # Initialize image variable
        self.img = None
        
    def add_image(self):
        try:
            # Open the file dialog to select an image file
            file_path = filedialog.askopenfilename(filetypes=[('Image Files', ('*.jpg', '*.png'))])
            
            # Load the selected image using PIL
            self.img = Image.open(file_path)
            
            # Create a Tkinter label widget to display the image using the PhotoImage class
            img_tk = ImageTk.PhotoImage(self.img)
            self.label = tk.Label(self.master, image=img_tk)
            self.label.image = img_tk
        
            # Pack the label widget onto the main window
            self.label.pack()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while adding the image: {str(e)}")

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
