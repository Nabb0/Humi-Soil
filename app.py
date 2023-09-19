from flask import Flask,render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('login.html')

@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=3000)

    