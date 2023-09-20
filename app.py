from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('paginainiziale.html')

@app.route('/register', methods=['GET'])
def inserisci():
    return render_template('register.html')

@app.route('/dati', methods=['GET'])
def dati():
    # Lettura dei dati dal form HTML
    username = request.args['username']
    email = request.args['email']
    first_name = request.args['first_name']
    last_name = request.args['last_name']
    gender = request.args['gender']
    birthdate = request.args['birthdate']
    password = request.args['password']

    # Creazione di un dizionario con i nuovi dati
    nuovi_dati = {'username': username, 'email': email, 'first_name': first_name, 'last_name': last_name, 'gender': gender, 'birthdate': birthdate, 'password': password}

    # Lettura dei dati dal file nel dataframe
    df1 = pd.read_csv('/workspace/Humi-Soil/registrations.csv')

    # Creazione di un nuovo DataFrame con i nuovi dati
    df2 = pd.DataFrame(nuovi_dati, index=[0])  # Create a DataFrame with a single row

    # Aggiunta dei nuovi dati al dataframe
    df1 = df1.append(df2, ignore_index=True)

    # Salvataggio del dataframe nel file 'registrations.csv'
    df1.to_csv('/workspace/Humi-Soil/registrations.csv', index=False)

    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3246, debug=True)
