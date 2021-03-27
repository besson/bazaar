from flask import Flask
from os import listdir
from flask import render_template
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    items = []

    for i in listdir('items'):
        with open(f'items/{i}') as j:
            items.append(json.load(j))
    
    print(items)

    return render_template('index.html', items=items)