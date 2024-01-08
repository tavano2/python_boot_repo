"""
TKinter란?
GUI를 만들어주는 파이썬 외부 모듈이다.
"""

from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 24))
# the packer <- tkinter에서 컴포넌트를 배치시켜주는 시스템
my_label.pack()
my_label["text"] = "New Text!"
my_label.config(text="New Text")

# 위 pack() 메소드를 살펴보면 **kw 라고 인자가 명시되어 있다.
# 여기서 파이썬 고급 인수 개념을 학습해보자.
"""
선택적 인수에 기본값
ex)
    def my_fn(a=1, b=2, c=3):
        do this with a
        then do this with b
        finally do this with c
    
    my_fn(b=5)

함수 도움말중에 ...은 기본 값이 들어 있다고 생각하면 되고
인수명:데이터타입 으로 되어 있는 경우 필수적으로 입력해야 하는 값이다.

ex2에서 계속..
"""


def button_clicked():
    print("I clicked button")
    data = input_ent.get()
    my_label.config(text=data)


# Button
button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
input_ent = Entry(width=30)
input_ent.insert(END, string="Some text to begin with.")
input_ent.pack()


# Text
text = Text(height=5, width=30)
# Puts cursor in textbox.
text.focus()
# Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
# Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()


# Spinbox
def spinbox_used():
    # gets the current value in spinbox.
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
# Called with current scale value.
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
# variable to hold on to checked state, 0 is off, 1 is on.


checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()
