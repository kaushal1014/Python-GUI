from tkinter import *
import sys

# global operator
entry = ""


def onclick(numbers):
    global entry
    entry = entry + str(numbers)
    text_inputs.set(entry)


def equal():
    global entry
    addition = eval(entry)
    text_inputs.set(addition)


def clear():
    global entry
    entry = '0'

    text_inputs.set(entry)


def close():
    sys.exit()


root = Tk()
root.title("Calculator")
root.geometry("280x311")
operator = ""
text_inputs = StringVar()
# entery box
txtbox = Entry(root, font='Helvetica,20,bold', textvariable=text_inputs, bd=18, width=27, insertwidth=1,
               insertofftime=0, bg='red', justify='right').place(x=0, y=0)
# row1
btn1 = Button(root, font=('Helvetica', '16'), text="1", padx=18, bd=8, width=1, command=lambda: onclick(1)).place(x=0,
                                                                                                                  y=60)
btn2 = Button(root, font=('Helvetica', '16'), text="2", padx=18, bd=8, width=1, command=lambda: onclick(2)).place(x=70,
                                                                                                                  y=60)
btn3 = Button(root, font=('Helvetica', '16'), text="3", padx=18, bd=8, width=1, command=lambda: onclick(3)).place(x=140,
                                                                                                                  y=60)
add = Button(root, font=('Helvetica', '16'), text="+", padx=18, bd=8, width=1, command=lambda: onclick("+")).place(
    x=210, y=60)

# row2
btn4 = Button(root, font=('Helvetica', '16'), text="4", padx=18, bd=8, width=1, command=lambda: onclick(4)).place(x=0,
                                                                                                                  y=110)
btn5 = Button(root, font=('Helvetica', '16'), text="5", padx=18, bd=8, width=1, command=lambda: onclick(5)).place(x=70,
                                                                                                                  y=110)
btn6 = Button(root, font=('Helvetica', '16'), text="6", padx=18, width=1, bd=8, command=lambda: onclick(6)).place(x=140,
                                                                                                                  y=110)
sub = Button(root, font=('Helvetica', '16'), text="-", padx=18, width=1, bd=8, command=lambda: onclick("-")).place(
    x=210, y=110)

# row3
btn7 = Button(root, font=('Helvetica', '16'), text="7", padx=18, width=1, bd=8, command=lambda: onclick(7)).place(x=0,
                                                                                                                  y=160)
btn8 = Button(root, font=('Helvetica', '16'), text="8", padx=18, width=1, bd=8, command=lambda: onclick(8)).place(x=70,
                                                                                                                  y=160)
btn9 = Button(root, font=('Helvetica', '16'), text="9", padx=18, width=1, bd=8, command=lambda: onclick(9)).place(x=140,
                                                                                                                  y=160)
mul = Button(root, font=('Helvetica', '16'), text="*", padx=18, width=1, bd=8, command=lambda: onclick("*")).place(
    x=210, y=160)

# row4
btn0 = Button(root, font=('Helvetica', '16'), text="0", padx=18, width=1, bd=8, command=lambda: onclick(0)).place(x=0,
                                                                                                                  y=210)
AC = Button(root, font=('Helvetica', '16'), text="C", padx=18, width=1, bd=8, command=lambda: clear()).place(x=70,
                                                                                                             y=210)
equalbtn = Button(root, font=('Helvetica', '16'), text="=", padx=18, width=1, bd=8, command=lambda: equal()).place(
    x=140, y=210)
div = Button(root, font=('Helvetica', '16'), text="/", padx=18, width=1, bd=8, command=lambda: onclick("/")).place(
    x=210, y=210)

# row5
close = Button(root, font=('Helvetica', '16'), text="close", padx=20, bd=6, width=1, command=close).place(x=0, y=263)
point = Button(root, font=('Helvetica', '16'), text=".", padx=20, bd=6, width=1, command=lambda: onclick(".")).place(
    x=70,
    y=263)
root.mainloop()
