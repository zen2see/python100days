# LABEL
from tkinter import *


def setup_screen():
    # SPECIFY WINDOW SIZE
    window = Tk()
    window.title("Tkinter Example Program")
    window.minsize(width=600, height=500)
    # ADD PADDING
    window.config(padx=100, pady=200)

    # PACK JUST CENTERS EACH ITEM IN THE MIDDLE ONE ON TOP OF THE OTHER
    # PLACE SPECIFIES
    # GRID COL ROW

    # SPECIFY LABEL
    my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
    my_label.config(text="New Text")
    #my_label.pack()
    #my_label.place(x=100, y=200)
    my_label.grid(column=0, row=0)
    
    # ENTRY
    input = Entry(width=10)
    # Insert initial text
    input.insert(0, "Type here")  
    #input.pack()
    input.grid(column=3, row=2)

     # Bind the focus event to clear the placeholder text
    # input.bind("<FocusIn>", lambda event: clear_placeholder(event, input))

    # BUTTON 1
    """
    # Without lambda
    button = Button(text="Click Me", command=button_clicked(input, my_label))
    # This calls button_clicked(input, my_label) immediately and sets command to None

    # With lambda
    button = Button(text="Click Me", command=lambda: button_clicked(input, my_label))
    # This sets command to a function that calls button_clicked(input, my_label) when clicked
    """
    button = Button(text="Click Me", command=lambda: button_clicked(input, my_label))
    #button.pack()
    button.grid(column=1, row=1)
    

    button2 = Button(text="2nd Button")
    button2.grid(column=2, row=0)
    button2.config(padx=10, pady=10)

def clear_placeholder(event, input):
    if input.get() == "Type here":
        input.delete(0, END)
    
def button_clicked(input, my_label):
    print("I got clicked")
    new_text = input.get()
    print(f"New text from entry: {new_text}")  # Debugging print
    my_label.config(text=new_text)
    # Clear the entry field
    input.delete(0, END)  
    # return my_label

def main():
    setup_screen()
    mainloop()


if __name__=='__main__':
    main()

