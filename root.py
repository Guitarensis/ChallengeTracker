from typing import Optional, Callable
import tkinter as tk
import tkinter.messagebox as messagebox
from all_colors import colors
import traceback

root: Optional[tk.Tk] = None

def root_window(root: tk.Tk):
    try:    
        # Create main window
        root_color = colors[0]  # choose a color from the list
        root.title('Race Stats Tracker')
        root.geometry('675x325')
        root.config(bg=root_color)

        def title_bar():
            # create title bar frame
            menu_bar: Optional[tk.Frame] = tk.Frame(root, bg=colors[1], relief='raised', bd=2)

            # add title bar to root window using grid
            grid: Optional[Callable[..., None]] = menu_bar.grid if menu_bar else None
            if grid:
                grid(row=0, column=0, columnspan=2, sticky="ew")
                print('Created Title Bar and added to Root window')

        # call the function to create and add the title bar
        title_bar()

    except Exception as e:
        showerror: Optional[Callable[..., str]] = messagebox.showerror
        showerror("Error", str(e))
    finally:
        # This block is always executed, regardless of whether an exception was raised or not.
        traceback.print_exc()

if __name__ == '__main__':
    try:
        root = tk.Tk()
        root_window(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        # This block is always executed, regardless of whether an exception was raised or not.
        traceback.print_exc()
