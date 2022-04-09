from flask import Flask, render_template, redirect
from randomizer import generate_page
import secrets

app = Flask(__name__)


@app.context_processor
def utility_processor():
    def get_number(value : str) -> str:
        output = 0
        for x in value:
            output += ord(x)
        return output
    return dict(get_number=get_number)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/seed")
@app.route("/seed/")
def get_seed():
    seed = secrets.token_hex(4)
    return redirect("/seed/" + seed)


@app.route("/seed/<seed>")
def randomizer(seed : int):
    if len(seed) != 8:
        return "Invalid seed length."
    else:
        try:
            seed_value = int(seed, 16)
        except ValueError:
            return "Seed can only contain hex."

    return render_template('randomizer.html', seed=seed, moons=generate_page(seed_value, {}))