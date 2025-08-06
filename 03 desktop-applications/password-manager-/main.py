from platform import win32_is_iot
from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    # Password Generator Project
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = password_numbers + password_symbols+ password_letter
    random.shuffle(password_list)

    your_password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, string=your_password)
    pyperclip.copy(your_password)

def search_pass():
    website_name = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo("Error", "No data file found")
    else:
            if website_name in data:
                email = data[website_name]["email"]
                password = data[website_name]["password"]
                messagebox.showinfo(title=website_name, message=f"{email}, {password}")
                password_entry.insert(0, string=f"{password}")
            else:
                messagebox.showinfo("Error", "No details for this website")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Make sure everything is filled")
    else:
        try:
            with open("data.json", "r") as data_file:
            # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
        # updating dat
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file ,indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Passwork Manager")
window.config(padx=50, pady=50, bg= "black")

canvas = Canvas(width=200, height= 200, highlightthickness=0, bg="black")
image = PhotoImage(file= "logo.png")
canvas.create_image(100, 100, image = image)
canvas.grid(column=1, row=0)

# Website --> text
website_text = Label(text="Website:", bg="white")
website_text.grid(column=0, row=1)
website_entry = Entry()
website_entry.focus()
website_entry.grid(column=1, row=1,)

search_button = Button(text= "Search", command= search_pass, width= 20)
search_button.grid(row =1, column= 2, columnspan= 1)

# Email
email_text = Label(text="Email/Username:", bg="white")
email_text.grid(column=0, row=2)
email_entry = Entry(width=40)
email_entry.insert(END, "python@gamil.com")
email_entry.grid(column=1, row=2, columnspan= 2)

# Password
password_text = Label(text="Password:", bg="white")
password_text.grid(column=0, row=3)

password_entry = Entry(width=23) #width=21
password_entry.grid(column=1, row=3, columnspan= 1)

generate_pass = Button(text="Generate Password", bg="white", command=generate)
generate_pass.grid(column=2, row=3, columnspan= 1)

# Add
add_button = Button(text="Add", bg="white", command= save,width=36)
add_button.grid(column=1, row=4, columnspan=2) #



window.mainloop()