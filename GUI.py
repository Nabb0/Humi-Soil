import RPi.GPIO as GPIO
import time
import random
import tkinter as tk
import pyowm
from datetime import datetime, timedelta
from PIL import Image, ImageTk

# Configura i pin GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

def generate_and_save_random_number_with_time():
    random_number = random.randint(1, 10)
    current_time = datetime.now()
    
    # Formatta l'orario nel formato desiderato, ad esempio "2023-09-28 14:30:00"
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    file_path = "/home/pi/Desktop/Humi-Soil-main/numeri_casuali.txt"
    
    # Scrive il numero casuale e l'orario nel file
    with open("numeri_casuali.txt", "a") as file:
        file.write(f"{formatted_time}: {random_number}\n")
    
    # Controlla se il numero è pari o dispari e controlla il LED
    if random_number % 2 == 0:
        print("LED on")
        GPIO.output(18, GPIO.HIGH)
    else:
        print("LED off")
        GPIO.output(18, GPIO.LOW)

   try:
        with open("numeri_casuali.txt", "r") as file:
            content = file.read()
            text_box.config(state=tk.NORMAL)
            text_box.delete(1.0, tk.END)
            text_box.insert(tk.END, content)
            text_box.config(state=tk.DISABLED)
    except FileNotFoundError:
        text_box.config(state=tk.NORMAL)
        text_box.delete(1.0, tk.END)
        text_box.insert(tk.END, "File not found")
        text_box.config(state=tk.DISABLED)

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
        frame1_label.place(relx=0.5,rely=0.5,anchor='center')

        # Mappa lo stato del tempo a un percorso di immagine
        image_path = map_weather_status_to_image(status)

        # Carica l'immagine meteo utilizzando PIL
        image = Image.open(image_path)
        tk_image = ImageTk.PhotoImage(image)

        # Aggiorna l'immagine meteo nel widget Label
        label.config(image=tk_image)
        label.image = tk_image

        # Carica l'immagine locale
        local_image = Image.open("/home/pi/Desktop/Humi-Soil-main/Documentazione/Logo.png")
        local_tk_image = ImageTk.PhotoImage(local_image)

        # Crea un widget Label per visualizzare l'immagine locale
        local_image_label = tk.Label(root, image=local_tk_image)
        local_image_label.pack()
        

        # Ottenere le previsioni per oggi
        forecast = mgr.forecast_at_place(city, '3h')
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        tomorrow = today + timedelta(days=1)
        weather_forecast = forecast.get_weather_at(tomorrow)
        temperature_forecast = weather_forecast.temperature('celsius')['temp']

        frame2_label.config(text=f"{city}\nTemperature Forecast Today: {temperature_forecast}°C")
        frame2_label.place(relx=0.5,rely=0.5,anchor='center')
    except Exception as e:
        frame1_label.config(text=f"Error: {e}")

# Funzione per mappare lo stato del tempo a un percorso di immagine
def map_weather_status_to_image(status):
    # Aggiungi qui le tue mappature tra stati del tempo e percorsi delle immagini
    # Ad esempio:
    if "clear" in status.lower():
        return "/home/pi/Desktop/Humi-Soil-main/Immagini Meteo/clear sky.png"
    elif "clouds" in status.lower():
        return "/home/pi/Desktop/Humi-Soil-main/Immagini Meteo/overcast_clouds.png"
    elif "rain" in status.lower():
        return "/home/pi/Desktop/Humi-Soil-main/Immagini Meteo/rain.png"
    elif "snow" in status.lower():
        return "/home/pi/Desktop/Humi-Soil-main/Immagini Meteo/snow.png"
    elif "shower rain" in status.lower():
        return "/home/pi/Desktop/Humi-Soil-main/Immagini Meteo/shower rain.png"
    elif "thunderstorm" in status.lower():
        return "/home/pi/Desktop/Humi-Soil-main/Immagini Meteo/thunderstorm.png"
    elif "Few_Clouds" in status.lower():
        return "/home/pi/Desktop/Humi-Soil-main/Immagini Meteo/Few_Clouds.png"
    elif "mist" in status.lower():
        return "/home/pi/Desktop/Humi-Soil-main/Immagini Meteo/mist.png"
    else:
        return "/home/pi/Desktop/Humi-Soil-main/Immagini Meteo/drizzle.png"

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
label.place(relx=0.25,rely=0.16,anchor='center')

# Crea un pulsante Tkinter per generare il numero casuale con l'orario
random_button = tk.Button(root, text="Genera Numero Casuale", command=generate_and_save_random_number_with_time)
random_button.pack()


# Crea una scrollbar
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Crea un widget Text per visualizzare il contenuto del file
text_box = tk.Text(root, yscrollcommand=scrollbar.set)
text_box.pack()

# Configura la scrollbar
scrollbar.config(command=text_box.yview)



# Organizzazione dei widget nella finestra
get_weather("Milan")  # Chiamata iniziale per ottenere i dati meteo di Milano

# Avvia il loop principale di Tkinter
root.mainloop()
