# POMODORO.PY DAY 27
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

# CHECK MARK COPY FROM WIKIOEDIA
# COLORS = https://colorhunt.co/ 
def setup_screen():
    # SPECIFY WINDOW SIZE
    window = Tk()
    window.title("Tkinter Pomodoro Program")
    # window.minsize(width=200, height=224)
    # ADD PADDING
    #window.config(padx=100, pady=50, bg=YELLOW)
    title_label = Label(text="Timer", fg="#90C67C", bg=YELLOW, font=(FONT_NAME, 35, "bold"))
    title_label.grid(column=1, row=0)
    #canvas.create_text(205, 90, text="Timer", fill="#90C67C", font=(FONT_NAME, 35, "bold"))
    #canvas = Canvas(width=500, height=524, bg=YELLOW, highlightthickness=0)
    canvas = Canvas(width=500, height=524, bg=YELLOW, highlightthickness=0)
    # CREATE TIMER TEXT
    try:
        tomato_img = PhotoImage(file="tomato.png")
    except window.TclError:
        print("Error: Image file not found or invalid format.")
        window.destroy()
        exit()
    # SET IMAGE
    #canvas.create_image(250, 262, image=tomato_img)  
    canvas.create_image(100, 112, image=tomato_img)
    #canvas.create_text(250, 282, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
    canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
    # CREATE IMAGE AT CENTER OF THE CANVAS
    canvas.grid(column=1, row=1)
    # CREATE START TEXT
    #canvas.create_text(80, 330, text="Start", fill="black", font=(FONT_NAME, 10, "bold"))
    # CREATE RESET TEXT
    #canvas.create_text(322, 330, text="Reset", fill="black", font=(FONT_NAME, 10, "bold"))
    # CREATE START BUTTON
    start_button = Button(text="Start")
    start_button.grid(column=0, row=2)
    # CREATE RESET BUTTON
    reset_button = Button(text="reset")
    reset_button.grid(column=2, row=2)

    # Draw grid lines
    for i in range(0, 500, 100): # Vertical lines
        canvas.create_line(i, 0, i, 400, fill="black")
        print(f"Vertical line: ({i}, 0) to ({i}, 524):")
    for j in range(0, 500, 100): # Horizontal lines
          if i != 250: # Skip the middle line
            canvas.create_line(0, j, 400, j, fill="black")
            print(f"Horizontal line: (0, {j}) to (500, {j})")
    
    # Configure row and column weights to adjust sizes
    # window.grid_rowconfigure(0, weight=1)
    # window.grid_rowconfigure(1, weight=2) # Middle row double height
    # window.grid_rowconfigure(2, weight=1)
    # window.grid_rowconfigure(3, weight=1) # New row
    # window.grid_rowconfigure(4, weight=1) # New row
    # window.grid_columnconfigure(0, weight=1)
    # window.grid_columnconfigure(1, weight=2) # Middle column double width
    # window.grid_columnconfigure(2, weight=1)

    window.mainloop()


def main():
    setup_screen()

if __name__=="__main__":
    main()


