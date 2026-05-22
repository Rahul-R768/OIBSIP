import tkinter as tk
from tkinter import messagebox
import random 
import string


def gen_password():
    try:
        length=int(length_entry.get())

        if length<=0:
            messagebox.showerror("Error","Please enter a valid password length.")
            return
        if length<6:
            messagebox.showerror("weak password!","password length should be at least 6 chracters for better security.")
            return
    except ValueError:
        messagebox.showerror("Error","please enter a numeric values only for password length.")
        return
    
    include_letters=letters_var.get()
    include_digits=digits_var.get()
    include_symbols=symbols_var.get()

    if not(include_letters or include_digits or include_symbols):
        messagebox.showerror("Selection Error","please select at least 1 character type.")
        return
    characters=''
    if include_letters:
        characters+=string.ascii_letters
    if include_digits:
        characters+=string.digits
    if include_symbols:
        characters+=string.punctuation

    exclude_chars=exclude_entry.get()
    for char in exclude_chars:
        characters=characters.replace(char,'')
    if not characters:
        messagebox.showerror("Char error!","All characters are excluded.")
        return
    
    password=''.join(random.choice(characters) for i in range(length))

    result_entry.delete(0,tk.END)
    result_entry.insert(0,password)

def copy_password():
    password=result_entry.get()
    if password=='':
        messagebox.showerror("Copy Error!","No password to copy.")
        return
    window.clipboard_clear()
    window.clipboard_append(password)
    window.update()
    messagebox.showinfo("copied","password copied to clipboard successfully.")





window=tk.Tk()
window.title("PASSWORD GENERATOR")
window.geometry("500x500")

title_label=tk.Label(window,text="PASSWORD GENERATOR",font=("Arial",15,"bold"),fg="red")
title_label.pack(pady=10)

length_label=tk.Label(window,text="Enter Password Length: ",font=("Arial",10))
length_label.pack()

length_entry=tk.Entry(window)
length_entry.pack(pady=10)

letters_var=tk.BooleanVar(value=True)
digits_var=tk.BooleanVar(value=True)
symbols_var=tk.BooleanVar(value=True)

letters_check=tk.Checkbutton(window,text="Include Letters(a-z,A-Z)",variable= letters_var,font=("Arial",10))
letters_check.pack()

digits_check=tk.Checkbutton(window,text="Include Digits(0-9)",variable= digits_var,font=("Arial",10))
digits_check.pack()

symbols_check=tk.Checkbutton(window,text="Include Symbols(!@#$%&*)",variable= symbols_var,font=("Arial",10))
symbols_check.pack()

exclude_label=tk.Label(window,text="Exclude Characters(Optional):",font=("Arial",10))
exclude_label.pack(pady=15)

exclude_entry=tk.Entry(window)
exclude_entry.pack()

generate_button=tk.Button(window,text="Generate",font=("Arial",10,"bold"),command=gen_password)
generate_button.pack(pady=30)

result_label=tk.Label(window,text="password:",font=("Arial",10,"bold"))
result_label.pack()

result_entry=tk.Entry(window)
result_entry.pack()

copy_button=tk.Button(window,text="Copy Password",font=("Arial",10,"bold"),command=copy_password)
copy_button.pack(pady=25)


window.mainloop()





