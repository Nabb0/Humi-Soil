import tkinter as tk
import pyowm
from datetime import datetime, timedelta
from PIL import Image, ImageTk

# Crea una finestra Tkinter
root = tk.Tk()
root.title("App Meteo con Tkinter")

# Imposta le dimensioni della finestra
larghezza_finestra = 1000
altezza_finestra = 800
root.geometry(f"{larghezza_finestra}x{altezza_finestra}")

# Funzione per ottenere le informazioni meteo di una città e mostrare l'immagine corrispondente allo stato del tempo
def get_weather(city):
    owm = pyowm.OWM('2de7c19ab75bb0d7182f2a46cea6859a')  # Inserisci qui la tua chiave API di OpenWeatherMap

    try:
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(city)
        weather = observation.weather
        temperature = weather.temperature('celsius')['temp']
        status = weather.status
        print(status)

        frame1_label.config(text=f"{city}\nTemperature: {temperature}°C\nStatus: {status}")

        # Mappa lo stato del tempo a un percorso di immagine
        image_path = map_weather_status_to_image(status)

        # Carica l'immagine utilizzando PIL
        image = Image.open(image_path)

        # Converte l'immagine in un formato compatibile con Tkinter
        tk_image = ImageTk.PhotoImage(image)

        # Aggiorna l'immagine nel widget Label
        label.config(image=tk_image)
        label.image = tk_image

        # Ottenere le previsioni per oggi
        forecast = mgr.forecast_at_place(city, '3h')
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        tomorrow = today + timedelta(days=1)
        weather_forecast = forecast.get_weather_at(tomorrow)
        temperature_forecast = weather_forecast.temperature('celsius')['temp']

        frame2_label.config(text=f"{city}\nTemperature Forecast Today: {temperature_forecast}°C")
    except Exception as e:
        frame1_label.config(text=f"Error: {e}")

# Funzione per mappare lo stato del tempo a un percorso di immagine
def map_weather_status_to_image(status):
    # Aggiungi qui le tue mappature tra stati del tempo e percorsi delle immagini
    # Ad esempio:
    if "clear" in status.lower():
        return "Immagini Meteo\clear sky.png"
    elif "overcast_clouds" in status.lower():
        return "Immagini Meteo\overcast_clouds.png"
    elif "rain" in status.lower():
        return "Immagini Meteo\rain.png"
    elif "snow" in status.lower():
        return "Immagini Meteo\snow.png"
    elif "shower rain" in status.lower():
        return "Immagini Meteo\shower rain.png"
    elif "thunderstorm" in status.lower():
        return "Immagini Meteo\thunderstorm.png"
    elif "overcast_clouds" in status.lower():
        return "Immagini Meteo\overcast_clouds.png"
    elif "mist" in status.lower():
        return "Immagini Meteo\mist.png"
    else:
        return ".\Immagini Meteo\drizzle.png"

# Creazione dei widget
frame1 = tk.Frame(root, bg="lightblue")
frame1.place(relx=0, rely=0, relwidth=0.5, relheight=0.5)

frame1_label = tk.Label(frame1, text="", padx=10, pady=10)
frame1_label.pack()

frame2 = tk.Frame(root, bg="lavender")
frame2.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.5)

frame2_label = tk.Label(frame2, text="", padx=10, pady=10)
frame2_label.pack()

frame3 = tk.Frame(root, bg="#7e99dd")
frame3.place(relx=0, rely=0.5, relwidth=0.5, relheight=0.5)

frame4 = tk.Frame(root, bg="orange")
frame4.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.5)

# Crea un widget Label per visualizzare l'immagine meteo
label = tk.Label(root)
label.pack()

# Organizzazione dei widget nella finestra
get_weather("Southampton,US")  # Chiamata iniziale per ottenere i dati meteo di Milano

# Avvia il loop principale di Tkinter
root.mainloop()
