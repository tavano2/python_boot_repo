from tkinter import *


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# entry
input_ent = Entry(width=7)
input_ent.grid(row=0, column=1, padx=10)
# Miles Label
miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)
# is eqqual label
equal_label = Label(text="is equal to")
equal_label.grid(row=1, column=0)
# result Label
result_label = Label(text="0")
result_label.grid(row=1, column=1)
# km label
km_label = Label(text="Km")
km_label.grid(row=1, column=2)


def button_clicked():
    input_miles = float(input_ent.get())
    result_km = round(input_miles * 1.609)
    result_label.config(text=f"{result_km}")


# cal btn
button = Button(text="Calculate", command=button_clicked)
button.grid(row=2, column=1)


window.mainloop()
