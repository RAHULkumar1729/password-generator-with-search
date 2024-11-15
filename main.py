from tkinter import *
from tkinter import messagebox
from password_generator.main import password
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def get_pass():
    password_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    website = website_input.get()
    username = username_input.get()
    passwords = password_input.get()
    new_data = {
        website: {
            "email": username,
            "password": passwords
        }
    }
    if len(website) == 0 or len(username) == 0:
        messagebox.showinfo(title="OOPS", message="Please don't leave any field empty!", )
    else:
        is_ok = messagebox.askokcancel(title=username,
                                       message=f"Is the given info\nwebsite={website}\npassword={passwords}"
                                               f"\nis ok")
        if is_ok:

            try:
                with open("data.json", mode="r") as file:
                    data = json.load(file)
            except:
                with open("data.json", mode ="w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", mode="w") as file:
                    json.dump(data, file, indent=4)
                    website_input.delete(0, END)
                    password_input.delete(0, END)

def search_file():
    website = website_input.get()
    username = username_input.get()

    with open("data.json", "r") as file:
        data = json.load(file)
        if website in data:
            password = data[f"{website}"]["password"]
            messagebox.showinfo(title=website,message=f"Email: {username}\nPassword: {password}\n  Already there")
        else:
            messagebox.showinfo(title="Error", message="no file found")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
canvas = Canvas(width=200, height=200)
window.config(padx=20, pady=20)
locker_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=locker_image)
canvas.grid(row=0, column=1)
website_label = Label(text="Website:")
website_label.grid(row=2, column=0)
username_label = Label(text="Email/Username:")
username_label.grid(row=3, column=0)
password_label = Label(text="Password:")
password_label.grid(row=4, column=0)
website_input = Entry(width=35)
website_input.focus()
website_input.grid(row=2, column=1)
username_input = Entry(width=35)
username_input.insert(0, "Ulaptop@gmail.com")
username_input.grid(row=3, column=1, columnspan=2)
password_input = Entry(width=21)
password_input.grid(row=4, column=1)
search_button = Button(text="search",command=search_file)
search_button.grid(row=2, column=2)
password_button = Button(text="Generate Password", command=get_pass)
password_button.grid(row=4, column=2)
add_button = Button(text="Add", width=36, command=save_pass)
add_button.grid(row=5, column=1, columnspan=2)


window.mainloop()
