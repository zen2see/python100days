import tkinter
from tkinter import IntVar, Tk, Label, Button, Entry, Text, Spinbox, \
      Scale, Checkbutton, Radiobutton, Listbox

# docs.python.org/3/library/tkinter.html
# tcl.tk/man/tcl8.6/TkCmd/pack.htm

def setup_screen():
    window = Tk()
    window.title("Tkinter GUI Program")
    # SPECIFY WINDOW SIZE
    window.minsize(width=700, height=500)
    my_label = Label(text="A LABEL", font=("Arial", 24, "bold"))
    # Place label on the screen and centered - see manual for customization
    my_label.config(text="New Text")
    # The pack() method is called on a widget instance and takes several 
    # optional arguments to control its placement and behavior.
    # SIDE Option side=tk.LEFT side=tk.RIGHT
    # FILL Option fill=tk.x fill=tk.y
    # EXPAND fill parent expand=TRUE
    # PADDING padx=10 paddy=5
    # ANCHOR anchor="nw"
    my_label.pack() # my_label.pack(side="left") my_label.place(x=0, y=0)

    # WE COULD USE GRID PROVIDING A COLUMN AND ROW
    # button.grid(column=1, row=1)
    # GRID AND PACK CANNOT BE USED TOGETHER

    # Call a name of a function with the command
    button = Button(text="Click Me", command=lambda: button_clicked(entry, my_label))
    button.pack() 
    entry = Entry(width=10)
    entry.pack() 
    print(entry.get()) 
    # MORE WIDGETS
    # TEXT
    text = Text(height=5, width=30)
    # Put cursor in textbox
    text.focus()
    # Add some text
    text.insert(tkinter.END, "Example of multi-line text entry.")
    # Get current value in textbox at line1, character 0
    print(text.get("1.0", tkinter.END))
    text.pack()
    # Gets the current value in spinbox
    """
     The syntax is lambda arguments: expression. Lambda functions are often used for short, 
     simple operations where a full function definition is unnecessary. 
     They are particularly useful in higher-order functions like map, filter, and sorted. 
    """
    # SPINBOX INCREASES VALUE BY PRESSING UP/DOWN ARROWS
    spinbox = Spinbox(from_=0, to=10, width=5, command=lambda: spinbox_used(spinbox))
    spinbox.pack()  

    # SCALE - CALLED WITH CURRENT SCALE VALUE
    scale = Scale(from_=0, to=100, command=lambda value: scale_used(value))
    scale.pack()

    # CHECK BUTTON
    # IntVar allows for bi-directionally binding a variable and a UI element.
    checked_state = IntVar() 
    checkbutton = Checkbutton(text="Is on?", variable=checked_state, \
                              command=lambda: checkbutton_used(checked_state))
    checked_state.get()
    checkbutton.pack()
    
    # RADIO BUTTON
    radio_state = IntVar()
    radiobutton1 = Radiobutton(text="Option 1", value=1, variable=radio_state, \
                             command=lambda: radio_used(radio_state))
    radiobutton2 = Radiobutton(text="Option 2", value=2, variable=radio_state, \
                             command=lambda: radio_used(radio_state))
    radiobutton1.pack()
    radiobutton2.pack()

    # LIST BOX
    listbox = Listbox(height=4)
    fruits = ["Apple", "Pear", "Orange", "Banana"]
    for item in fruits:
        listbox.insert(fruits.index(item), item)
    listbox.bind("<<ListboxSelect>>", listbox_used)
    listbox.pack()

    # Start the Tkinter event loop * A MUST
    window.mainloop()
    return spinbox

def add(*args):
    for n in args:
        n+=n
    return n

def calculate(n, **kwargs):
    print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

def bar(a, *args, **kw):
    print(a, args, kw)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]

# BUTTON
def button_clicked(entry, my_label):
    print("I got clicked")
    new_text = entry.get()
    my_label.config(text=new_text)

# SPINBOX
def spinbox_used(spinbox):
    # Gets the current value in spinbox
    print(spinbox.get())

# SCALE
def scale_used(value):
    print(value)

# CHECKBUTTON
def checkbutton_used(checked_state):
    # Prints 1 if ON Button checked, else 0
    print(checked_state.get())    

# RADIOBUTTON 
def radio_used(radio_state):
    # Toggles radio button
    print(radio_state.get())

# LISTBOX
def listbox_used(event):
    listbox = event.widget
    selection = listbox.curselection()
    if selection:
        print(listbox.get(selection[0]))

def main():
    setup_screen()
    print(add(2, 3, 5))
    calculate(2, add=3, multiply=5)
    my_car = Car(make="Nissan", model="Skyline")
    print(my_car.model)
    calculate(5, add=3, multiply=2)
    bar(4,7,30,x=10,y=64)
    scale_used(Scale)

if __name__=='__main__':
    main()