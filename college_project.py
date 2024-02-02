

import tkinter as tk
from tkinter import messagebox
import requests

def get_weather(city):
    api_key = '0068bcd8a5e6fec7504158c3c14aa8c5'
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']

            result = f'Temperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s'
            return result
        else:
            return f'Error: {data["message"]}'
    except Exception as e:
        return f'Error: {str(e)}'

def get_weather_info():
    city = entry.get()

    if not city:
        messagebox.showinfo('Weather App', 'Please enter a city.')
        return

    weather_info = get_weather(city)
    messagebox.showinfo('Weather App', weather_info)

# GUI Setup
root = tk.Tk()
root.title('Weather App')

label = tk.Label(root, text='Enter city:')
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

button = tk.Button(root, text='Get Weather', command=get_weather_info)
button.pack(pady=10)

root.mainloop()
