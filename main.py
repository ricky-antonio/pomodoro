from math import floor
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 3
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 2
reps = 0

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        session_length = LONG_BREAK_MIN
    elif reps % 2 == 0:
        timer_label.config(text="Work", fg=PINK)
        session_length = SHORT_BREAK_MIN
    else:
        timer_label.config(text="Work", fg=GREEN)
        session_length = WORK_MIN

    count_down(session_length)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_sec:02d}")
    if count > 0:
        window.after(1000, count_down, count -1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
#window setup
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#Canvas setup
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


fg=GREEN
check_mark = "✓"

#Timer label
timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)

#check label
check_label = Label(text=check_mark, font=(FONT_NAME, 28, "bold"),bg=YELLOW, fg=GREEN)
check_label.grid(column=1, row=3)

#Start Button
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

#Reset Button
reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(column=2, row=2)


window.mainloop()