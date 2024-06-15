from tkinter import colorchooser 
from tkinter import *

main = Tk()
main.title("Color Picker Application")
main.geometry("400x300")


def colorPicker():
    my_color_selection = colorchooser.askcolor()
    my_color = my_color_selection[1]
    color_label.config(bg=my_color,text="Your choosen color")
picker_button = Button(main, text="Pick your color",font=("arial",12,"bold"),command=colorPicker)
picker_button.pack(pady=50)
color_label =Label(main, text="Click on the button above", font=("arial",23,"bold"))
color_label.pack(pady=10)

main.mainloop()

