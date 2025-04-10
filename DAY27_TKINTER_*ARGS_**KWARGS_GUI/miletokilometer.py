# MILE TO KILOMETER SECTION 27
from tkinter import *

def setup_screen():
    # SPECIFY WINDOW SIZE
    window = Tk()
    window.title("Tkinter Mile to Kilometer Program")
    window.minsize(width=600, height=500)
    # ADD PADDING
    window.config(padx=100, pady=200)

    # GRID COL ROW

    # MILES INPUT
    miles_input = Entry(width=10)
    # Insert initial text
    miles_input.insert(0, "0")  
    miles_input.grid(column=1, row=0)

    # SPECIFY MILES LABEL
    miles_label = Label(text="Miles", font=("Arial", 22, "bold"))
    # my_label.config(text="New Text")
    miles_label.grid(column=2, row=0)
    
    # SPECIFY ISEQUALTO LABEL
    ie_label = Label(text="is equal to", font=("Arial", 18, "bold"), fg="red", bg="yellow")
    # my_label.config(text="New Text")
    ie_label.grid(column=0, row=1)

    # KM INPUT
    #km_input = Entry(width=10)
    #km_input.insert(0, "0")  
    #km_input.grid(column=1, row=1)
    
    # SPECIFY KM LABEL
    km_label = Label(text="Km", font=("Arial", 22, "bold"))
    km_label.grid(column=2, row=1)

    # SPECIFY ANSWER LABEL
    ans_label = Label(text="", font=("Arial", 22, "bold"))
    ans_label.grid(column=1, row=1)

    # Bind the focus event to clear the placeholder text
    miles_input.bind("<FocusIn>", lambda event: clear_placeholder(event, miles_input))
    # km_input.bind("<FocusIn>", lambda event: clear_placeholder(event, km_input))

    # BUTTON 1
    """
    # Without lambda
    button = Button(text="Click Me", command=button_clicked(input, my_label))
    # This calls button_clicked(input, my_label) immediately and sets command to None

    # With lambda
    button = Button(text="Click Me", command=lambda: button_clicked(input, my_label))
    # This sets command to a function that calls button_clicked(input, my_label) when clicked
    """
    button = Button(text="Calculate", command=lambda: button_calculate(miles_input, ans_label))
    button.grid(column=1, row=2)



     # Bind the focus event to clear the placeholder text
    # input.bind("<FocusIn>", lambda event: clear_placeholder(event, input))

def button_calculate(input1, alabel):
    a = float(input1.get()) 
    # b = float(input2.get())
    # Convert to two decimal places
    ans = round(a * 1.60934, 2)
    alabel.config(text=ans)
    # Clear the entry fields
    input1.delete(0, END)
    # input2.delete(0, END)  
 
def clear_placeholder(event, input):
    if input.get() == "Type here":
        input.delete(0, END)

def main():
    setup_screen()
    mainloop()
    
if __name__=='__main__':
    main()