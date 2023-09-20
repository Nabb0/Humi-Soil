from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('login.html')

@app.route('/register', methods=['GET'])  # Ora gestisce il metodo GET
def register():
    if request.method == 'GET':
        username = request.args.get('username')
        email = request.args.get('email')
        first_name = request.args.get('first_name')
        last_name = request.args.get('last_name')
        gender = request.args.get('gender')
        birthdate = request.args.get('birthdate')
        password = request.args.get('password')
        
        with open('registrations.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([username, email, first_name, last_name, gender, birthdate, password])
        
        return "Registration Successful!"
    else:
        return "Invalid Request"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=3000)
