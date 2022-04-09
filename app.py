from flask import Flask, render_template, redirect, request
from settings import parse_form, decode_settings, Settings
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


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        settings = parse_form(request.form)
        if len(request.form['seed']) > 0:
            return redirect("/seed/" + str(request.form['seed']) + "?settings=" + str(settings))
        else:
            return redirect("/seed?settings=" + str(settings))
    return render_template('index.html')


@app.route("/seed")
@app.route("/seed/")
def get_seed():
    settings = request.args.get('settings')
    seed = secrets.token_hex(4)
    if settings is None:
        return redirect("/seed/" + seed)
    else:
        return redirect("/seed/" + seed + "?settings=" + settings)


@app.route("/seed/<seed>")
def randomizer(seed : int):
    if len(seed) != 8:
        return "Invalid seed length."
    else:
        try:
            seed_value = int(seed, 16)
        except ValueError:
            return "Seed can only contain hex."
    settings = request.args.get('settings')
    if settings is not None:
        settings_class = decode_settings(settings)
    else:
        settings_class = Settings()

    return render_template('randomizer.html', seed=seed, moons=generate_page(seed_value, settings_class))
