# ---------------------------- IMPORT ------------------------------- #
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():

    password_list = []
    password_list += [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(END, string=password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_fn():
    website = website_comp.get()
    email = email_comp.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if website == "" or website is None or password == "" or password is None:
        messagebox.showerror(title="Error", message="Please don't leave any fields empty!")
    else:
        # is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
        #                                                       f"\nPassword: {password} \nIs it ok to save?")
        # if is_ok:
        # json 형식으로 쓰기
        # json.dump(new_data, file, indent=4)

        # json 형식 읽기
        # json_data = json.load(file)
        # print(json_data)

        # json 형식 업데이트하기
        # 기존 데이터 읽기
        # json_data = json.load(file)
        # 새로운 데이터 업데이트하기
        # json_data.update(new_data)
        # 새로운 데이터 쓰기
        # json.dump(json_data, file, indent=4)

        try:
            with open("data.json", "r") as file:
                json_data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            json_data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(json_data, file, indent=4)
        finally:
            website_comp.delete(0, END)
            password_entry.delete(0, END)


def search_fn():
    website = website_comp.get()
    # 솔루션에서는 if else로 아주 쉽게 처리할 수 있을 때는
    # 제어문으로 예외를 잡는 것이 좋다고한다. 즉 KeyError는 if else로 변환하자.
    # try:
    #     with open("data.json", "r") as file:
    #         json_data = json.load(file)
    #         messagebox.showinfo(title=website, message=f"Email: {json_data[website]['email']}\n"
    #                                                    f"Password: {json_data[website]['password']}")
    # except KeyError:
    #     messagebox.showerror(title="Error", message=f"No Details for {website} exists.")
    # except FileNotFoundError:
    #     messagebox.showerror(title="Error", message="No Data File Found.")
    try:
        with open("data.json", "r") as file:
            json_data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found.")
    else:
        if website in json_data:
            messagebox.showinfo(title=website, message=f"Email: {json_data[website]['email']}\n"
                                                       f"Password: {json_data[website]['password']}")
        else:
            messagebox.showerror(title="Error", message=f"No Details for {website} exists.")


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
website_comp = Entry(width=21)
website_comp.grid(row=1, column=1)
website_comp.focus()

search_btn = Button(text="Search", width=20, command=search_fn)
search_btn.grid(row=1, column=2)

email_comp = Entry(width=36)
email_comp.grid(row=2, column=1, columnspan=2)
email_comp.insert(END, string="asjk158@naver.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

password_gen_button = Button(text="Generate Password", command=generate_password)
password_gen_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=add_fn)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
