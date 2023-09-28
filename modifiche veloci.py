# Funzione per generare e salvare un numero casuale con l'orario
def generate_and_save_random_number_with_time():
    random_number = random.randint(1, 10)
    current_time = datetime.datetime.now()
    
    # Formatta l'orario nel formato desiderato, ad esempio "2023-09-28 14:30:00"
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    
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



# ...

# Crea un pulsante Tkinter per generare il numero casuale con l'orario
random_button = tk.Button(root, text="Genera Numero Casuale", command=generate_and_save_random_number_with_time)
random_button.pack()

# ...
