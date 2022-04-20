
from flask import Flask , render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/data', methods=['post'])
def data():
    firstname = request.form.get('first_name')
    secondname = request.form.get('second_name')
    phonenumber = request.form.get('phone_number')
    email = request.form.get('email')

    print(firstname , secondname, phonenumber, email)
    return 'data received'

app.run(debug = True) # should be always at the end
