from tkinter import *
import math
import os
import random

PURPLE = "#8D8DAA"
GREY = "#DFDFDE"
PINK = "#F56D91"
FONT_NAME = "American Typewriter"
WORK_MIN = 25
SHORT_BREAK_MIN = 25
LONG_BREAK_MIN = 20
CHECKMARK = "✔"
PATH_BREAK = "./images/break/"
PATH_WORK = "./images/work/"
PATH_LONG_BREAK = "./images/long_break/"
reps = 0
timer = None


def timer_reset():
    global reps
    reps = 0
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=PINK)
    canvas.itemconfig(timer_text, text="00:00")
    canvas.itemconfig(image_container, image=format_cat_default_img)
    check_mark_label.config(text="")


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 0:
        timer_label.config(text="Break", fg=PURPLE)
        canvas.itemconfig(image_container, image=random.choice(format_break_img))
        count_down(short_break_sec)

    elif reps % 8 == 0:
        timer_label.config(text="Break", fg=PURPLE)
        canvas.itemconfig(image_container, image=random.choice(format_long_break_img))
        count_down(long_break_sec)

    else:
        timer_label.config(text="Work", fg=PINK)
        canvas.itemconfig(image_container, image=random.choice(format_work_img))
        count_down(work_sec)


def count_down(count):

    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_sec == 0:
        count_sec = "00"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        work_sessions = math.floor(reps/2)
        checkmark_string = ""
        for _ in range(work_sessions):
            checkmark_string += CHECKMARK
        check_mark_label.config(text=checkmark_string)


def format_images(image_path_list, path):

    return [PhotoImage(file=f"{path}{image_path}") for image_path in image_path_list]


break_image_list = os.listdir(PATH_BREAK)
work_image_list = os.listdir(PATH_WORK)
long_break_image_list = os.listdir(PATH_LONG_BREAK)

window = Tk()
window.title("Cat Study Timer")
window.config(padx=200, pady=100, bg=GREY)


format_break_img = format_images(break_image_list, PATH_BREAK)
format_work_img = format_images(work_image_list, PATH_WORK)
format_long_break_img = format_images(long_break_image_list, PATH_LONG_BREAK)

format_cat_default_img = PhotoImage(file="./images/cat_default.png")
canvas = Canvas(width=512, height=512, bg=GREY, highlightthickness=0)
image_container = canvas.create_image(256, 256, image=format_cat_default_img)

timer_text = canvas.create_text(256, 256, text="00:00", fill=PINK, font=(FONT_NAME, 80, "bold"))
canvas.grid(column=1, row=2)

timer_label = Label(text="Timer", font=(FONT_NAME, 100, "bold"), fg=PINK, bg=GREY)
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", font=(FONT_NAME, 40), fg=PURPLE, highlightbackground=GREY, command=start_timer)
start_button.grid(column=0, row=3)

reset_button = Button(text="Reset", font=(FONT_NAME, 40), fg=PURPLE, highlightbackground=GREY, command=timer_reset)
reset_button.grid(column=2, row=3)

check_mark_label = Label(font=(FONT_NAME, 70), fg=PURPLE, bg=GREY)
check_mark_label.grid(column=1, row=3)

window.mainloop()
