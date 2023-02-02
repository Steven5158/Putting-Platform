from tkinter import *


window = Tk()
window.title("Putting Platform")
window.geometry("800x600")

window.configure(bg='#202340')

def button1():
    listbox.insert(END, 'button1 pressed')

b=Button(window, text="Setting1", command=button1)
b2=Button(window, text="Setting2")
b3=Button(window, text="Setting3")
b4=Button(window, text="Setting4")


b.place(x=300,y=200)
b2.place(x=425,y=200)
b3.place(x=300,y=250)
b4.place(x=425,y=250)

window.mainloop()
