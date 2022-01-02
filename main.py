import temp_scan

from tkinter import *
import time
import threading

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
    
def read_temp():
    y=80
    for x in range(10):
        output_VP_Out.delete(1.0, END)
        output_VP_Out.insert( END, y + x )
        time.sleep( 1)  # Develop 2->1 sek

window = Tk()
window.geometry('600x400')
window.title("My Comp")



Label( window, text="Enter the word:", fg="black", font="non 12 bold") .place(x= 300, y=10)

textentry = Entry(window, width=20)
textentry.place(x=400, y=30)

Button(window, text="Submit", width=6, command=click) .grid(row=3, column=0)

Label(window, text="\nDefinition:", fg="black", font="none 12 bold") .grid(row=4, column=0)

output = Text(window, width=75, height=6, wrap=WORD)
output.grid(row=5, column=0, columnspan=2)

my_compdictionary = {
    'algorithm': 'Step by step instruction to complete a task', 'bug': 'Piece of code that cause a program to fail'
    }

Button(window, text="Close", width=6, command=close_window) .grid(row=7, column=0)

VP = Canvas( window, height=50, width=50, bg="red")
VP.place(x=10, y= 300)
VP.create_line(10,10, 40, 40, fill='white')
VP.create_line(10,40, 40, 10, fill='white', width=5)


output_VP_Out = Text(window, width=5, height=1, wrap=WORD)
output_VP_Out.place(x=20, y=260)
# output_VP_Out.insert(END, "75")

output_VP_In = Text(window, width=5, height=1, wrap=WORD)
output_VP_In.place(x=80, y=320)
output_VP_In.insert(END, "65")

output_VP_1 = Text(window, width=5, height=1, wrap=WORD)
output_VP_1.place(x=140, y=320)
x = temp_scan.temp_value()
output_VP_1.insert(END, x)

output_Acc_1 = Text(window, width=5, height=1, wrap=WORD)
output_Acc_1.place(x=350, y=320)
x = temp_scan.temp_value()
output_Acc_1.insert(END, x)

output_Acc_2 = Text(window, width=5, height=1, wrap=WORD)
output_Acc_2.place(x=530, y=320)
x = temp_scan.temp_value()
output_Acc_2.insert(END, x)

Acc_1 = Canvas( window, height=50, width=50, bg="blue")
Acc_1.place(x=280, y= 300)
Acc_1.create_line(10,10, 40, 40, fill='white')
Acc_1.create_line(10,40, 40, 10, fill='white', width=5)

Acc_2 = Canvas( window, height=50, width=50, bg="blue")
Acc_2.place(x=450, y= 300)
Acc_2.create_line(10,10, 40, 40, fill='white')
Acc_2.create_line(10,40, 40, 10, fill='white', width=5)

Elem = Canvas( window, height=50, width=50, bg="blue")
Elem.place(x=280, y= 220)
Elem.create_line(10,10, 40, 40, fill='white')
Elem.create_line(10,40, 40, 10, fill='white', width=5)

threading.Thread(target=read_temp).start()

window.mainloop()


