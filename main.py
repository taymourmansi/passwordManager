from tkinter import *
from tkinter import messagebox
import pyperclip
import json
import pandas
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
def generatePassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters= random.randint(7,12)
    nr_symbols = random.randint(1,3)
    nr_numbers = random.randint(3,5)

    password_letters = [random.choice(letters) for _ in range(0,nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(0,nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(0,nr_numbers)]

    password = password_letters + password_symbols + password_numbers
    random.shuffle(password)
    strPassword = "".join(password)
    passwordInput.insert(END,strPassword)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def savePass():
    website = websiteInput.get()
    email = emailInput.get()
    password = passwordInput.get()
    newData = {
        website:{
            "email" : email,
            "password": password,
        }
    }
    info = f"{website} | {email} | {password}\n"
    if len(website) == 0 or len(password)== 0 == "" or len(email) == 0:
        messagebox.showerror(title ="Error",message="Please fill all fields!")

    else:
        try:
            with open("passwords.json", "r") as saved:
                data = json.load(saved)

        except FileNotFoundError:
            with open("passwords.json","w") as saved:
                json.dump(newData, saved,indent=4)

        else:
            data.update(newData)
            with open("passwords.json","w") as saved:
                json.dump(data, saved,indent=4)

        finally:
            pyperclip.copy(password)
            passwordInput.delete(0, 'end')
            websiteInput.delete(0, 'end')



# ---------------------------- Search For Password ------------------------------- #
def searchPassword():
    website = websiteInput.get()
    try:
        with open("passwords.json", "r") as saved:
            data = json.load(saved)
    except FileNotFoundError:
        messagebox.showinfo(title=f"Error", message=f"No data file found!")

    else:
        if websiteInput.get() in data:
            passwordSearch = data[website]["password"]
            emailSearch = data[website]["email"]
            messagebox.showinfo(title =f"Account Info for {data[website]}",message=f"Email: {emailSearch}\nPassword:{passwordSearch}\nPassword has been copied to clipboard")
            pyperclip.copy(passwordSearch)
        else:
            messagebox.showinfo(title=f"Error", message=f"No credentials for {website} found!")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx= 20,pady = 20)
window.title("Password Manager")

canvas = Canvas(width = 200, height = 200)
logImg = PhotoImage(file="logo.png")
canvas.create_image(100,100,image = logImg)
canvas.grid(column = 1, row=0)

websiteLabel = Label(text="Website:",font=("Arial",15,"normal"))
websiteLabel.grid(column=0, row = 1)
websiteInput = Entry(width = 20)
websiteInput.grid(column=1,row=1,columnspan=1)
websiteInput.focus()
websiteSearch = Button(text = "Search",width=16,command = searchPassword)
websiteSearch.grid(column=2,row=1)

emailLabel = Label(text="Email/Username:",font=("Arial",15,"normal"))
emailLabel.grid(column=0, row = 2)
emailInput = Entry(width = 39)
emailInput.grid(column=1,row=2,columnspan=2)
emailInput.insert(0,"taymourmansi@gmail.com")


passwordLabel = Label(text="Password:",font=("Arial",15,"normal"))
passwordLabel.grid(column=0, row = 3)
passwordInput = Entry(width = 20)
passwordInput.grid(column=1,row=3)
passwordGenerate = Button(text = "Generate Password",command = generatePassword)
passwordGenerate.grid(column=2,row=3)

addBtn = Button(text = " Add", width=36, command = savePass)
addBtn.grid(column=1,row=4,columnspan=2)

window.mainloop()