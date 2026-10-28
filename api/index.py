import os, json
from flask import Flask, render_template, jsonify

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
app = Flask(__name__, template_folder=os.path.join(BASE, "templates"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/results")
def results():
    with open(os.path.join(BASE, "results", "metrics.json")) as f:
        return jsonify(json.load(f))

@app.route("/api/predict", methods=["POST"])
def predict():
    return jsonify({"error": "Live prediction is disabled in the hosted version."}), 400
