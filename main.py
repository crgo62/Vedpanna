from tkinter import *

def click():
    entered_text=textentry.get()
    output.delete(0.0, END)
    try:
        definition = my_compdictionary[entered_text]
    except:
        definition = "Sorry there is no word like that please try again"
    output.insert(END, definition)

def close_window():
    window.destroy()
    exit()


window = Tk()
window.geometry('600x400')
window.title("My Comp")



Label( window, text="Enter the word:", fg="black", font="non 12 bold") .grid(row=1, column=0)

textentry = Entry(window, width=20)
textentry.grid(row=2, column=0)

Button(window, text="Submit", width=6, command=click) .grid(row=3, column=0)

Label(window, text="\nDefinition:", fg="black", font="none 12 bold") .grid(row=4, column=0)

output = Text(window, width=75, height=6, wrap=WORD)
output.grid(row=5, column=0, columnspan=2)

my_compdictionary = {
    'algorithm': 'Step by step instruction to complete a task', 'bug': 'Piece of code that cause a program to fail'
    }

Button(window, text="Close", width=6, command=close_window) .grid(row=7, column=0)

c = Canvas( window, height=50, width=50, bg="blue")
c.grid(row=8, column=1)

window.mainloop()


