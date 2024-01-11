# ---------------------------- IMPORT ------------------------------- #
from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_fn():
    with open("data.txt", "a") as file:
        website = website_comp.get()
        email = email_comp.get()
        password = password_entry.get()
        file.write(f"{website} | {email} | {password}\n")

        website_comp.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# labels
website_lb = Label(text="Website:")
website_lb.grid(row=1, column=0)

email_lb = Label(text="Email/Username:")
email_lb.grid(row=2, column=0)

password_lb = Label(text="Password:")
password_lb.grid(row=3, column=0)

# component
website_comp = Entry(width=36)
website_comp.grid(row=1, column=1, columnspan=2)
website_comp.focus()

email_comp = Entry(width=36)
email_comp.grid(row=2, column=1, columnspan=2)
email_comp.insert(END, string="asjk158@naver.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

password_gen_button = Button(text="Generate Password")
password_gen_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=add_fn)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
