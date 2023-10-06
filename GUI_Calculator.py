'''
Description: The following code is to write a program to make a basi calculator.
             The calculator should be displayed in a small GUI when you run the program.
'''

'''
# ******************************************************************************
# *                               COPYRIGHT NOTICE                             *
# ******************************************************************************
# *                                                                            *
# *  This code is authored by Marcelo Villalobos Diaz                          *
# *  You are free to use, modify, and distribute this code, provided           *
# *  you give appropriate credit by including the author's name.               *
# *                                                                            *
# *  Copyright (c) 2023 Marcelo Villalobos Diaz                                *
# *                                                                            *
# ******************************************************************************
'''

import tkinter # library to make GUIs

w = [] # empty list to hold the buttons

window = tkinter.Tk() # creates a window

window.title("Calculator") # Adds tittle to the window
window.geometry("350x375") # Sets the size of the window

e = tkinter.Entry(window, width=48) # makes entry box and places it in window
e.grid(row=0, columnspan=4)


#------------------ this nested loop will add buttons 1 - 9 -------------------------
buttonNumber = 0
for r in range(1, 4):
    for c in range(0, 3):
        w.append(tkinter.Button(window,
                                text = buttonNumber + 1,
                                width = 10, height = 5,
                                command = lambda n = buttonNumber + 1: myFunction(n)))
        w[buttonNumber].grid(row = r, column = c)
        buttonNumber = buttonNumber + 1

#-------------------- this will add the "-" button -------------------------------
w.append(tkinter.Button(window,
                        text = "-",
                        width = 10, height = 5,
                        command = lambda: myFunction("-")))
w[9].grid(row =2, column = 3)


#--------------------- adds button "0" to the list & the grid ---------------------
w.append(tkinter.Button(window,
                        text = "0", # makes the button text equal to the button number
                        width = 10, height = 5, # amkes the buttons look square-ish
                        command = lambda n = 0: myFunction(0))) # n is the button number
w[10].grid(row = 4, column =1) # place button in a grid, tell it to span 2 columns

#--------------------- this adds the "." button ------------------------------------
w.append(tkinter.Button(window,
                        text = ".",
                        width = 10, height = 5,
                        command = lambda: myFunction(".")))
w[11].grid(row =4, column = 2)

#----------------------- this adds the "+" button ----------------------------------
w.append(tkinter.Button(window,
                        text = "+",
                        width = 10, height = 5,
                        command = lambda: myFunction("+")))
w[12].grid(row =1, column = 3)

#----------------------- this adds the "=" button -----------------------------------
w.append(tkinter.Button(window,
                        text = "=",
                        width = 10, height = 5,
                        command = lambda: myFunction("=")))
w[13].grid(row =4, column = 3)

#--------------------- Add the clearWindow function --------------------------------
def clearWindow():
    e.delete(0, tkinter.END)

w.append(tkinter.Button(window,
                        text="Clear",
                        width=10, height=5,
                        command=clearWindow))
w[14].grid(row=4, column=0)

#------------------------ this adds the "*" button ----------------------------------
w.append(tkinter.Button(window,
                        text = "*",
                        width = 10, height = 5,
                        command = lambda: myFunction("*")))
w[15].grid(row =3, column = 3)

#----------------------  this function will be called when a button is clicked ----------
def myFunction(buttonNumber):
    e.insert(50, buttonNumber) # appends buttonNumber to the entry box
    # the 50 is how many characters will be appended, after, it starts inserting numbers in reverse

    equation = e.get() # get the text that is currently inside the Entry box
    if buttonNumber == "=":
        splitEquation = equation.split("=")
        answer = eval(splitEquation[0])
        e.insert(50,answer)
        # print("equation=", equation, "=", answer)

# show the window
window.mainloop()