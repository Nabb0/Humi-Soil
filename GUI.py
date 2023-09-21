import tkinter as tk
import pyowm

# Crea una finestra Tkinter
root = tk.Tk()
root.title("App Meteo con Tkinter")

# Impostare le dimensioni della finestra
larghezza_finestra = 1000  # Larghezza in pixel
altezza_finestra = 800  # Altezza in pixel
root.geometry(f"{larghezza_finestra}x{altezza_finestra}")

# Funzione per ottenere le informazioni meteo di Milano
def get_milan_weather():
    owm = pyowm.OWM('2de7c19ab75bb0d7182f2a46cea6859a')
 
    location = "Milano, IT"  # Imposta la località su Milano
    
    try:
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(location)
        weather = observation.weather
        temperature = weather.temperature('celsius')['temp']
        status = weather.status

        frame1_label.config(text=f"Milano\nTemperature: {temperature}°C\nStatus: {status}")
    except Exception as e:
        frame1_label.config(text=f"Error: {e}")
    
# Creazione dei widget
frame1 = tk.Frame(root, bg="lightblue", width=400, height=300)
frame1.grid(row=0, column=0, rowspan=2, columnspan=2)

frame1_label = tk.Label(frame1, text="", padx=10, pady=10)
frame1_label.pack()


frame2 = tk.Frame(root, bg="lavender", width=larghezza_finestra // 2, height=altezza_finestra // 2)
frame2.grid(row=0, column=2, rowspan=2, columnspan=2)

frame3 = tk.Frame(root, bg="#7e99dd", width=larghezza_finestra // 2, height=altezza_finestra // 2)
frame3.grid(row=2, column=0, rowspan=2, columnspan=2)

frame4 = tk.Frame(root, bg="orange", width=larghezza_finestra // 2, height=altezza_finestra // 2)
frame4.grid(row=2, column=2, rowspan=2, columnspan=2)

# Organizzazione dei widget nella finestra
get_milan_weather()  # Chiamata iniziale per ottenere i dati meteo di Milano
# Rimuovi il campo di input e il pulsante di ricerca, poiché ora mostriamo solo i dati di Milano
# label.pack()
# entry.pack()
# search_button.pack()

# Avvia il loop principale di Tkinter
root.mainloop()
