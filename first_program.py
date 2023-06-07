## Importing all the necessary packages required for the program
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
from PIL import ImageTk,Image

## This is to improve the resolution in the window Operating system
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

## To create an object and making it as a base for the widgets to place
root = ttk.Window(themename='darkly')

## To create a root window and make it constant
## The root.geometry() is in the format of (width,height)
root.geometry('1400x1000')
root.resizable(True,True)
root.title('CAN Simulation system')

## Menubar declaration here in the code
menubar = ttk.Menu(root)
#root.overrideredirect(True)


## Adding the options in the menu bar
file = tk.Menu(menubar,fg='blue')
edit = tk.Menu(menubar, fg='blue')

## To add some sub commands in the file menu
file.add_command(label='New',background='grey')
file.add_command(label='Exit',background='grey',command=root.destroy)

## To add some sub commands in the edit menu
edit.add_command(label='Cut',background='grey')
edit.add_command(label='Copy',background='grey')
edit.add_command(label='Paste',background='grey')

## To add these file and edit in the menubar in a cascading manner
menubar.add_cascade(label='File', menu=file)
menubar.add_cascade(label='Edit', menu=edit)


## To open the image and include it in the title bar
## To open the image using the PIL library and we have to convert it to the Photo image
image = Image.open('C:\\Users\\ramakrishnan.mahesh\\Desktop\\magnetic sense files\\magnetic sense logo.png')
Photo_image = ImageTk.PhotoImage(image)

## We have to include the company logo in the top right corner in the title bar 
## For this we can use the function iconphoto() function and this is possible only if the Photo_Image is being provided
root.iconphoto(False,Photo_image)

## Now, we can create a frame and try to include the Magnetic sense logo in that frame
label = tk.Label(root, image=Photo_image)
label.pack(side='top',padx=20,pady=20)


## To configure the menu bar in the root window
root.config(menu=menubar)

## To execute the application
root.mainloop()


