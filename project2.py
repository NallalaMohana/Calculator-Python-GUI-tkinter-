from tkinter import *

from sklearn.datasets import clear_data_home
root=Tk()


#definition for clear button
def clear():
    e.delete(0,END)

#definition for equalto button
def button_equalto():
    sec=e.get()
    e.delete(0,END)
    if math=="addition":
       e.insert(0,int(first)+int(sec))
    if math=="subtraction":
       e.insert(0,first-int(sec))
    if math=="multiplication":
       e.insert(0,first*int(sec))
    if math=="division":
       e.insert(0,first/int(sec))


#definitons for the number buttons 
def button_click(number):
    first=number
    new=e.get()
    e.delete(0,END)
    e.insert(0,str(new)+str(first))

#definition for add button
def button_addition():
    global first
    global math
    math="addition"
    sec=e.get()
    first=int(sec)
    e.delete(0,END)
    
#definition for mul button
def button_multiplication():
    global first
    global math
    math="multiplication"
    sec=e.get()
    first=int(sec)
    e.delete(0,END)

#definition for sub button
def button_subtraction():
    global first
    global math
    math="subtraction"
    sec=e.get()
    first=int(sec)
    e.delete(0,END)

#definition for div button
def button_division():
    global first
    global math
    math="division"
    sec=e.get()
    first=int(sec)
    e.delete(0,END)

#title to the window
root.title("Basic calci")

#entering the text
e=Entry(root, width=30, borderwidth=2, relief="solid")

#geometry for the entry label
e.grid(row=0, column=0, columnspan=4)

#creating number buttoins
button_1=Button(root, text="1", padx=20, pady=20, command=lambda: button_click(1))
button_2=Button(root, text="2", padx=20, pady=20, command=lambda: button_click (2))
button_3=Button(root, text="3", padx=20, pady=20, command=lambda: button_click(3))
button_4=Button(root, text="4", padx=20, pady=20, command=lambda: button_click(4))
button_5=Button(root, text="5", padx=20, pady=20, command=lambda: button_click(5))
button_6=Button(root,text="6", padx=20, pady=20, command=lambda: button_click(6))
button_7=Button(root,text="7", padx=20, pady=20, command=lambda: button_click(7))
button_8=Button(root,text="8", padx=20, pady=20, command=lambda: button_click(8))
button_9=Button(root, text="9", padx=20, pady=20, command=lambda: button_click(9))
button_0=Button(root, text="0", padx=20, pady=20, command=lambda: button_click(0))
button_clear=Button(root, text="clear", padx=73, pady=20, command=clear)
button_equal=Button(root, text="=", padx=20, pady=20, command=button_equalto)
button_add=Button(root, text="+", padx=20, pady=20, command=button_addition)
button_mul=Button(root,text="*",padx=20,pady=20,command=button_multiplication)
button_sub=Button(root,text="-",padx=20,pady=20,command=button_subtraction)
button_div=Button(root,text="/",padx=20,pady=20,command=button_division)


#geometry for buttons
button_1.grid(row=3,column=1)
button_2.grid(row=3,column=2)
button_3.grid(row=3,column=3)

button_4.grid(row=2,column=1)
button_5.grid(row=2,column=2)
button_6.grid(row=2, column=3)

button_7.grid(row=1, column=1)
button_8.grid(row=1, column=2)
button_9.grid(row=1, column=3)

button_0.grid(row=4, column=2)
button_equal.grid(row=4, column=3)
button_clear.grid(row=6, column=0, columnspan=4)
button_add.grid(row=4,column=1)
button_mul.grid(row=5,column=1)
button_sub.grid(row=5,column=2)
button_div.grid(row=5,column=3)


root.mainloop()