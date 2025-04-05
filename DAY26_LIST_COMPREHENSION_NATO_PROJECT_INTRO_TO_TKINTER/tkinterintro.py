import tkinter

# docs.python.org/3/library/tkinter.html
# tcl.tk/man/tcl8.6/TkCmd/pack.htm

def setup_screen():
    window = tkinter.Tk()
    window.title("Tkinter GUI Program")
    window.minsize(width=700, height=500)
    my_label = tkinter.Label(text="A LABEL", font=("Arial", 24, "bold"))
    # Place label on the screen and centered - see manual for customization
    my_label.pack()
    # Start the Tkinter event loop * A MUST
    window.mainloop()

def add(*args):
    for n in args:
        n+=n
    return n

def calculate(n, **kw):
    print(kwargs)
    n += kw["add"]
    n *= kw["multiply"]
    print(n)

class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]

def main():
    # setup_screen()
    # print(add(2, 3, 5))
    # calculate(2, add=3, multiply=5)
    my_car = Car(make="Nissan", model="Skyline")
    print(my_car.model)

if __name__=='__main__':
    main()