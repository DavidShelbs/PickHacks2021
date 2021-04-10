from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Use a service account
cred = credentials.Certificate('pickhacks2021-f8318e5b6b48.json')
firebase_admin = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://pickhacks2021-default-rtdb.firebaseio.com/'
    })

ref = db.reference()

# file = open('title_to_png.txt')
# lines = file.readlines()
# for line in lines:
#     image_key_ref = ref.child('image_keys')
#     image_key_ref.update({
#         line.split(',')[0]: line.split(',')[1].replace('https://', '').replace('/', '-')[:-1]
#     })

file = open('pokedata')
lines = file.readlines()
for line in lines:
    image_key_ref = ref.child('image_locs')
    key = ' '.join(line.split(' ')[4:])[:-1].replace('.', '')
    value = ','.join(line.split(' ')[:4])
    print(key, value)
    image_key_ref.update({
        key: value
    })

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main_index.html')

@app.route('/pokemap.html')
def pokemap():
    return render_template('pokemap.html')
    
@app.route('/game.html')
def game():
	return render_template('game.html')

if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True,host='0.0.0.0', port=80)
