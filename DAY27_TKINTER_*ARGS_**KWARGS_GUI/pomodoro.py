# POMODORO.PY DAY 27
from tkinter import *
from tkinter import font
# from tkinter import font
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
  
# ---------------------------- UI SETUP ------------------------------- #
# CHECK MARK COPY FROM WIKIOEDIA
# COLORS = https://colorhunt.co/ 
def setup_screen():
    # SPECIFY WINDOW SIZE
    window = Tk()

    window.title("Tkinter Pomodoro Program")
    # window.minsize(width=200, height=224)
    # ADD PADDING
    window.config(padx=0, pady=0, bg=YELLOW)

    # Configure row and column weights to adjust sizes
    window.grid_rowconfigure(0, weight=1)
    window.grid_rowconfigure(1, weight=0) # Setting to 0 prevents it from expanding
    window.grid_rowconfigure(2, weight=1)
    window.grid_columnconfigure(0, weight=1) 
    window.grid_columnconfigure(1, weight=0) # Setting to 0 prevents it from expanding
    window.grid_columnconfigure(2, weight=1)  

    title_label = Label(text="Timer", fg="#90C67C", bg=YELLOW, font=(FONT_NAME, 35, "bold"))
    title_label.grid(column=1, row=0, pady=(10, 0), sticky="s")
    #canvas.create_text(205, 90, text="Timer", fill="#90C67C", font=(FONT_NAME, 35, "bold"))
    #canvas = Canvas(width=500, height=524, bg=YELLOW, highlightthickness=0)

    canvas = Canvas(width=201, height=225, bg=YELLOW, highlightthickness=0)
    # CREATE IMAGE
    try:
        tomato_img = PhotoImage(file="tomato.png")
    except window.TclError:
        print("Error: Image file not found or invalid format.")
        window.destroy()
        exit()
    canvas.create_image(100, 112, image=tomato_img)
    # CREATE TIMER TEXT
    timer_text = canvas.create_text(100, 130, text="00:00", fill="white", \
                       font=(FONT_NAME, 35, "bold"))
    # CREATE IMAGE AND TEXT AT CENTER OF THE CANVAS
    canvas.grid(column=1, row=1, sticky="n")
    # ---------------------------- TIMER MECHANISM --------------------------- # 
    def start_timer(reps):
        reps += 1 
        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60
        print(reps)
        if reps % 8 == 0:
            count_down(long_break_sec, reps)
            title_label.config(text="Break", fg=RED)
        elif reps % 2 == 0:
            count_down(short_break_sec, reps)
            title_label.config(text="Break", fg=PINK)
        else:
            count_down(work_sec, reps)
            title_label.config(text="Work", fg=GREEN)
    # ---------------------------- COUNTDOWN MECHANISM ----------------------- #  
    # https://stackoverflow.com/questions/11328920/is-python-strongly-typed
    def count_down(count, reps):
        count_min = math.floor(count / 60) 
        count_sec = count % 60 
        if count_sec < 10:
            count_sec = f"0{count_sec}" 
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        if count > 0:
            window.after(1000, count_down, count - 1)
        else:
            start_timer(reps)
    # CREATE START BUTTON
    start_button = Button(text="Start", command=lambda: start_timer(0)) 
    # OR command=start_timer
    start_button.grid(column=0, row=2, pady=0, sticky="ne")
    # CREATE RESET BUTTON
    reset_button = Button(text="reset")
    reset_button.grid(column=2, row=2, pady=0, sticky="nw")
    # CREATE CHECK BUTTON
    larger_font = font.Font(family="Arial", size=22)
    check_mark = Label(text="\u2714", fg=GREEN, bg=YELLOW, font=larger_font)
    check_mark.grid(column=1, row=3)
    # ---------------------------- TIMER RESET ------------------------------- #
    
           
     
    # Draw grid lines
    # for i in range(0, 500, 100): # Vertical lines
    #     canvas.create_line(i, 0, i, 500, fill="black")
    #     print(f"Vertical line: ({i}, 0) to ({i}, 524):")
    # for j in range(0, 500, 7): # Horizontal lines
    #       if i != 250: # Skip the middle line
    #         canvas.create_line(0, j, 500, j, fill="black")
    #         print(f"Horizontal line: (0, {j}) to (500, {j})")
    window.mainloop()


def main():
    setup_screen()
    
if __name__=="__main__":
    main()


