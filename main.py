from pstats import count_calls
from tkinter import *
from turtledemo.penrose import start

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#c0757a"
RED = "#e7305b"
GREEN = "#579a68"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 20
CHECK = "✔"
reps = 0
checks = ""
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():

    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_label.config(text="Break", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_label.config(text="Break", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=PINK)
    else:
        countdown(work_sec)
        timer_label.config(text="Work", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)





# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global reps
    global checks
    min = int(count/60)
    if min < 10:
        min = ("0" + str(min))
    sec = int(count%60)
    if sec < 10:
        sec = ("0" + str(sec))
    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            checks += CHECK
            check_marks.config(text=checks, font=(FONT_NAME, 15, "normal"), bg=YELLOW, fg=GREEN)







# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")

canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


timer_label = Label()
timer_label.config(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)


start_button = Button()
start_button.config(text="Start", font=(FONT_NAME, 15, "bold"), highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)


reset_button = Button()
reset_button.config(text="Reset", font=(FONT_NAME, 15, "bold"), highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label()
check_marks.config(font=(FONT_NAME, 15, "normal"), bg=YELLOW, fg=GREEN)
check_marks.grid(column=1, row=3)

window.mainloop()