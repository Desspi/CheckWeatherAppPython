## Importy
import tkinter as tk
import requests
import datetime
from PIL import ImageTk, Image

# Funkcja czyszcząca placeholder
def clear_entry(event, entry):
    entry.delete(0, tk.END)

# Funkcja zwraca informacje pogodowe na podstawie nazwy miasta w formacie JSON
def get_weather_desc_in_json(cityName):
    api_key = "1c51578a86451319ec022878b7e3adca"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"appid": api_key, "q": cityName, "units":"metric", "lang": "pl"}
    response = requests.get(url, params=params)
    return response.json()

#Funkcja pokazująca okno z informacjami o pogodzie
def get_weather(city):
    weather = get_weather_desc_in_json(city)

    frame_lower.place(relx = 0.5, rely = 0.32, relwidth =0.75, relheight =0.6, anchor="n")

    if weather["cod"] == 200:
        #Dodanie frame na informacja pogodowe
    
        cityLabel = tk.Label(frame_lower, text=weather["name"] + ", " + weather["sys"]["country"], font=("Verdana", 14))
        cityLabel.place(relwidth=0.4, relheight=0.1)

        sunriseImageLabel = tk.Label(frame_lower, image=sunriseImage)
        sunriseImageLabel.place(relwidth=0.1, relx=0.4, relheight=0.1)

        sunriseTime = datetime.datetime.fromtimestamp(weather['sys']['sunrise']).strftime("%H:%M")
        sunriseLabel = tk.Label(frame_lower, text="Wschód: " + str(sunriseTime), justify="left")
        sunriseLabel.place(relwidth=0.20, relx= 0.5, relheight=0.1)

        sunsetImageLabel = tk.Label(frame_lower, image=sunsetImage)
        sunsetImageLabel.place(relwidth=0.1, relx= 0.7, relheight=0.1)

        sunsetTime = datetime.datetime.fromtimestamp(weather['sys']['sunset']).strftime("%H:%M")
        sunsetLabel=tk.Label(frame_lower, text="Zachód: " + str(sunsetTime), justify="left")
        sunsetLabel.place(relwidth=0.20, relx= 0.8, relheight=0.1)

        currentWeatherLabel = tk.Label(frame_lower, text=weather['weather'][0]['description'].upper(), font=("Verdana", 14))
        currentWeatherLabel.place(relwidth = 1, relheight=0.2, rely=0.1)

        currentTempInfoLabel = tk.Label(frame_lower, text="Temperatura", font=("Verdana", 10))
        currentTempInfoLabel.place(relwidth=0.5, relheight=0.1, rely=0.3)

        tempIconLabel = tk.Label(frame_lower, image=temperatureImage)
        tempIconLabel.place(relwidth=0.1, rely=0.3, relheight=0.1)

        currentTempFeelInfoLabel = tk.Label(frame_lower, text="Temperatura odczuwalna", font=("Verdana", 10))
        currentTempFeelInfoLabel.place(relwidth=0.5, relheight=0.1, relx=0.5, rely=0.3)

        tempFeelIconLabel = tk.Label(frame_lower, image=feelingTemperatureImage)
        tempFeelIconLabel.place(relwidth=0.1, rely=0.3, relheight=0.1, relx = 0.5)

        currentTempLabel = tk.Label(frame_lower, text=str(weather["main"]["temp"]) + " \u2103", font=("Verdana", 12))
        currentTempLabel.place(relwidth=0.5, relheight=0.1, rely = 0.4)

        currentTempFeelLabel = tk.Label(frame_lower, text=str(weather["main"]["feels_like"]) + " \u2103", font=("Verdana", 12))
        currentTempFeelLabel.place(relwidth=0.5, relheight=0.1, relx = 0.5, rely = 0.4)

        PressureInfoLabel = tk.Label(frame_lower, text="Ciśnienie", font=("Verdana", 10))
        PressureInfoLabel.place(relwidth = 0.5, relheight=0.1, rely=0.5)

        iconPressure = tk.Label(frame_lower, image=pressureImage)
        iconPressure.place(relwidth=0.1, relheight=0.1, rely=0.5)

        HumidityInfoLabel = tk.Label(frame_lower, text="Wilgotność", font=("Verdana", 10))
        HumidityInfoLabel.place(relwidth=0.5, relx =0.5, relheight=0.1, rely=0.5)

        iconHumidity = tk.Label(frame_lower, image=humidityImage)
        iconHumidity.place(relwidth=0.1, relx=0.5, relheight=0.1, rely=0.5)

        PressureLabel = tk.Label(frame_lower, text=str(weather["main"]["pressure"]) + " hPa", font=("Verdana", 12))
        PressureLabel.place(relwidth=0.5, relheight=0.1, rely=0.6)

        HumidityLabel = tk.Label(frame_lower, text=str(weather["main"]["humidity"]) + "%", font=("Verdana", 12))
        HumidityLabel.place(relwidth=0.5, relx= 0.5, relheight= 0.1, rely=0.6)

        CloudinessInfoLabel = tk.Label(frame_lower, text="Poziom zachmurzenia", font=("Verdana", 10))
        CloudinessInfoLabel.place(relwidth=0.5, relheight= 0.1, rely=0.7)

        IconCloudiness = tk.Label(frame_lower, image=cloudinessImage)
        IconCloudiness.place(relwidth=0.1, relheight=0.1, rely=0.7)

        WindInfoLabel = tk.Label(frame_lower, text = "Siła wiatru", font=("Verdana", 10))
        WindInfoLabel.place(relwidth=0.5, relx = 0.5, relheight=0.1, rely = 0.7)

        IconWind = tk.Label(frame_lower, image=windImage)
        IconWind.place(relwidth=0.1, relx = 0.5, relheight= 0.1, rely=0.7)

        CloudinessLabel = tk.Label(frame_lower, text=str(weather["clouds"]["all"]) + "%", font=("Verdana", 12))
        CloudinessLabel.place(relwidth=0.5, relheight=0.1, rely = 0.8)

        WindLabel = tk.Label(frame_lower, text=str(weather["wind"]["speed"]) + " km/h", font=("Verdana", 12))
        WindLabel.place(relwidth=0.5, relx = 0.5, relheight=0.1, rely = 0.8)
    else:
        tk.Label(frame_lower, text="Podane miasto nie istnieje bądź nie ma go w naszej bazie pogodowej", font=("Verdana", 12)).place(relwidth=1, relheight=0.2)

## Początek programu
root = tk.Tk()
root.title(" CheckWeatherApp")
root.iconbitmap("images/kweather.ico")


##Images
sunriseImage = ImageTk.PhotoImage(Image.open("images/sunrise.png"))
sunsetImage = ImageTk.PhotoImage(Image.open("images/sunset.png"))
temperatureImage = ImageTk.PhotoImage(Image.open("images/temperature.png"))
feelingTemperatureImage = ImageTk.PhotoImage(Image.open("images/high-temperature.png"))
pressureImage = ImageTk.PhotoImage(Image.open("images/atmospheric.png"))
humidityImage = ImageTk.PhotoImage(Image.open("images/humidity.png"))
cloudinessImage = ImageTk.PhotoImage(Image.open("images/overcast.png"))
windImage= ImageTk.PhotoImage(Image.open("images/wind.png"))
placeholder_text = ' Wprowadź tutaj miasto'


#Ustawianie tła dla aplikacji
canvas = tk.Canvas(root, width = 800, height=600)
img_bgc = ImageTk.PhotoImage(Image.open("images/background.jpg"))
label_wholepage = tk.Label(root, image=img_bgc)

#Stworzenie ramek
frame_upper = tk.Frame(root, bg="#a9d6e8", bd=4)
frame_lower = tk.Frame(root, bg="#a9d6e8", bd = 4)

#Stworzenie kontrolek
label_welcome = tk.Label(frame_upper, text="Sprawdź pogodę dla swojego miasta!",bg="#ffffff", font=("Verdana", 18), justify="center")
entry = tk.Entry(frame_upper, font=("Verdana", 14), justify="center")
entry.insert(0, placeholder_text)
entry.bind("<Button-1>", lambda event: clear_entry(event, entry))
button_submit = tk.Button(frame_upper, text="Pokaż pogodę", font=("Verdana", 14), justify="center", command=lambda: get_weather(entry.get()))
ButtonExit = tk.Button(frame_lower, text="Zakończ program", command = root.quit)

## Ustawienie widgetów na ekranie
canvas.pack()
label_wholepage.place(relwidth=1, relheight=1)
frame_upper.place(relx = 0.5, rely = 0.1, relwidth=0.75, relheight=0.2, anchor="n")
label_welcome.place(relwidth=1, relheight=0.45)
entry.place(rely = 0.5, relwidth=0.55, relheight=0.5)
button_submit.place(relx = 0.6, relwidth=0.4, rely = 0.5, relheight=0.5)
ButtonExit.place(relwidth=0.4, relx = 0.5, relheight=0.09, rely = 0.91, anchor="n")

root.mainloop()