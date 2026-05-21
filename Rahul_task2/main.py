import tkinter as tk
from tkinter import messagebox
import csv
from datetime import datetime

def calculate_bmi():
    try: 
        name=name_entry.get()
        if name.strip()=="":
            messagebox.showerror("Invalid Input!","please enter your name")
            return
        weight=float(weight_entry.get())
        height=float(height_entry.get())

        if weight<=0 or height<=0:
            messagebox.showerror("Invalid Input!","weight & height must be greater than 0")
            return
    except ValueError:
        messagebox.showerror("Invalid Input!"," please enter numeric input values only")    
        return
    
    bmi=weight/(height**2)

    if bmi<18.5:
        category="Underweight"
    elif bmi>=18.5 and bmi<25:
        category="Normal weight"
    elif bmi>=25 and bmi<30:
        category="Overweight"
    else:
        category="Obesity"

    result_label.config(text=f"Your BMI: {bmi:.3f}({category})")
    
    with(open("bmi_data.csv","a",newline="")) as file:
        writer=csv.writer(file)
        writer.writerow([name,weight,height,f"{bmi:.3f}",category,datetime.now().strftime("%Y-%m-%d %H:%M:%S")])




        


window = tk.Tk()
window.title("BMI Calculator")
window.geometry("500x400")


title=tk.Label(window,text="BMI CALCULATOR",font=("Arial",20,"bold"),fg="red")
title.pack(pady=20)
 
name_label=tk.Label(window,text="Enter name:",font=("Arial",10))
name_label.pack(pady=10)

name_entry=tk.Entry(window)
name_entry.pack()

weight_label=tk.Label(window,text="Enter weight(kgs):",font=("Arial",10))
weight_label.pack(pady=10)

weight_entry=tk.Entry(window)
weight_entry.pack()

height_label=tk.Label(window,text="Enter height(m):",font=("Arial",10))
height_label.pack(pady=10)

height_entry=tk.Entry(window)
height_entry.pack()

calculate_button=tk.Button(window,text="CALCULATE BMI",command=calculate_bmi,font=("Arial",10,"bold"))
calculate_button.pack(pady=20)

result_label=tk.Label(window,text="",font=("Arial",14,"bold"),fg="red")
result_label.pack(pady=10)



window.mainloop()




