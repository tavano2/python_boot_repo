from tkinter import *


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

"""
pack -> 단순 위젯 다음에 배치
place -> x,y 값을 기준으로 배치
grid -> 열과 행으로 나눠 배치
"""

# Label
my_label = Label(text="I Am a Label", font=("Arial", 24))
# the packer <- tkinter에서 컴포넌트를 배치시켜주는 시스템
my_label["text"] = "New Text!"
my_label.config(text="New Text")
my_label.grid(column=0, row=0)


def button_clicked():
    print("I clicked button")
    data = input_ent.get()
    my_label.config(text=data)


# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

button2 = Button(text="Click Me2", command=button_clicked)
button2.grid(column=2, row=0)

# Entry
input_ent = Entry(width=30)
input_ent.insert(END, string="Some text to begin with.")
input_ent.grid(column=3, row=2)

window.mainloop()
