import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("300x400")
root.title("Log In")

image = Image.open("splash.png")
image = ImageTk.PhotoImage(image)


background_label = tk.Label(root, image=image)
background_label.place(x=0, y=0)

password = tk.StringVar()
myentry = tk.Entry(root, textvariable=password, show="*")

def submit():
    if password.get() == "Password":
        print("Access Granted")
    else:
        print("Incorrect Password")

myentry.pack()

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

button = tk.Button(frame, text="Log In!", font=("Arial", 19), command=submit, width=2, height=1)
button.pack()

root.mainloop()