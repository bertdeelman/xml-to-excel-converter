
from flask import Flask, render_template, request, send_file
import os
import json
from datetime import datetime
from helpers.structure import get_structure, generate_excel_for_customer, get_latest_xlsx_files
from helpers.logger import get_log

app = Flask(__name__)

@app.route("/")
def index():
    base_path = os.path.join(os.getcwd())
    structure = get_structure(base_path)
    labels = json.load(open("type_mapping.json", "r", encoding="utf-8"))
    extra = get_log()
    customers = list(structure.keys())
    latest_files = get_latest_xlsx_files(base_path)
    return render_template("index.html",
        today=datetime.now().strftime("%Y-%m-%d"),
        now=datetime.now(),
        customers=customers,
        structure=structure,
        extra=extra,
        labels=labels,
        latest_files=latest_files
    )

@app.route("/generate_all/<customer>")
def generate_all(customer):
    base_path = os.path.join(os.getcwd())
    output_path = generate_excel_for_customer(customer, base_path)
    return send_file(output_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True, port=5050)
