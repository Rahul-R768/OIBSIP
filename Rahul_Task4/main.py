import tkinter as tk
from tkinter import messagebox
import requests
API_KEY="e2c1b69e24ea866938ba53ad4eb4c968"

def get_weather():
    city=city_entry.get()
    if city=="":
        messagebox.showerror("Invalid Input","Please enter a city name.")
        return
    
    if  city.isdigit():
            messagebox.showerror("Invalid Input","Please enter a valid city name...Not digits.")
            return
    
    selected_unit=unit.get()
    url = (f"https://api.openweathermap.org/data/2.5/weather"f"?q={city}&appid={API_KEY}&units={selected_unit}")

    try:
        response=requests.get(url)
        data=response.json()
        # print(data)
    except requests.exceptions.RequestException:
        messagebox.showerror("Internet connection Error","Check your internet connection.")
        return
    
    if str(data["cod"])!="200":
        result_label.config(text="City Not Found!")
        return
    temperature=data["main"]["temp"]  
    humidity=data["main"]["humidity"]
    condition=data["weather"][0]["description"]

    icon=""
    if "clear" in condition:
        icon = "☀️"

    elif "cloud" in condition:
        icon = "☁️"

    elif "rain" in condition:
        icon = "🌧️"

    elif "thunderstorm" in condition:
        icon = "⛈️"

    elif "snow" in condition:
        icon = "❄️"

    else:
        icon = "🌤️"
    
    symbol="°C"
    if selected_unit=="imperial":
        symbol="°F"
    result_label.config(text=f"City: {city}\nTemperature: {temperature}{symbol}\nHumidity: {humidity}%\nCondition: {condition} {icon}")


    

window=tk.Tk()
window.title("WEATHER APP",)
window.geometry("500x500")
unit = tk.StringVar(value="metric")


title_label=tk.Label(window,text="WEATHER APPLICATION",font=("Arial",15,"bold"),fg="red")
title_label.pack(pady=20)

city_label=tk.Label(window,text="Enter City Name:",font=("Arial",12,"bold"))
city_label.pack()

city_entry=tk.Entry(window,width=30,font=("Arial",18))
city_entry.pack()

celsius_button=tk.Radiobutton(window,text="Celsius",variable=unit,value="metric",font=("Arial",12,"bold"))
celsius_button.pack(pady=15)

fahrenheit_button=tk.Radiobutton(window,text="Fahrenheit",variable=unit,value="imperial",font=("Arial",12,"bold"))
fahrenheit_button.pack()                                                                                                                                                                                       

search_button=tk.Button(window,text="Get Weather",font=("Arial",15,"bold"),command=get_weather,padx=10,pady=10,bg="lightblue")
search_button.pack(pady=30)

result_label=tk.Label(window,text="",font=("Arial",14,"bold"),justify="left",fg="green")
result_label.pack(pady=20)


window.mainloop()