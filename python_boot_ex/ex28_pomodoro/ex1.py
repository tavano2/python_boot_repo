# pomodoro 기법이란
# 25분 일 - 5분 휴식을 4번 반복후
# 15~30분 휴식하는 일의 집중력을 향상시키는 기법
# ---------------------------- IMPORT ------------------------------- #
from tkinter import *
import time
from datetime import datetime

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_fn():
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_mark_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_fn():
    global reps
    reps += 1

    if reps > 8:
        return

    work_sec = WORK_MIN * 60
    st_rest_sec = SHORT_BREAK_MIN * 60
    ln_rest_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(ln_rest_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(st_rest_sec)
        timer_label.config(text="Break", fg=RED)
    else:
        count_down(work_sec)
        timer_label.config(text="Timer", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# 해당 학습에서 동적 타이핑을 배운다. 파이썬은 변수 선언시 데이터 타입을 명시하고 선언하지 않기 때문에
# 참조되는 형식에 따라 동적으로 데이터 타입이 변한다.
# 동적 타이핑에 관한 내용 : https://stackoverflow.com/questions/11328920/is-python-strongly-typed
def count_down(count):
    rs_count = datetime.strftime(datetime.fromtimestamp(count), "%M:%S")
    canvas.itemconfig(timer_text, text=rs_count)

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_fn()
        if reps % 2 != 0:
            text_value = check_mark_label.cget("text")
            if text_value is None:
                new_value = "✔"
            else:
                new_value = text_value + " ✔"
            check_mark_label.config(text=new_value)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_btn = Button(text="Start", command=start_fn, highlightthickness=0)
start_btn.grid(row=2, column=0)
reset_btn = Button(text="Reset", command=reset_fn, highlightthickness=0)
reset_btn.grid(row=2, column=2)

# ✔
check_mark_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 10))
check_mark_label.grid(row=3, column=1)

window.mainloop()
