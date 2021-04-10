from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main_index.html')

@app.route('/pokemap.html')
def pokemap():
    return render_template('pokemap.html')

if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True,host='0.0.0.0', port=80)
