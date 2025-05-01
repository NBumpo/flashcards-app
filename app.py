from flask import Flask, render_template, request, redirect
import os, json


app = Flask(__name__)
SETS_DIR ="flashcard_sets"

def get_set_names():
    return [f[:-5] for f in os.listdir(SETS_DIR) if f.endswith('.json')]

def load_set(set_name):
    path = os.path.join(SETS_DIR, f"{set_name}.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
    
@app.route('/')
def home():
    sets = get_set_names()
    return render_template("home.html", sets=sets)

@app.route('/set/<set_name>')
def view_set(set_name):
    cards = load_set(set_name)
    return render_template("set.html", set_name=set_name, cards=cards)

if __name__ == '__main__':
    app.run(debug=True)