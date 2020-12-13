from threading import Thread
from flask import Flask, render_template, request, abort
import os
app = Flask("None")
@app.route('/')
def home():
    return render_template("home.html")
def run():
   app.run(host='0.0.0.0',port=8080)
def keep_alive():
    t = Thread(target=run)
    t.start()