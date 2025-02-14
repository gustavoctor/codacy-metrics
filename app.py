import os
import requests
from flask import Flask, jsonify
from dotenv import load_dotenv

load_dotenv()  # Cargar variables de entorno

app = Flask(__name__)

CODACY_API_URL = "https://api.codacy.com/2.0"
CODACY_TOKEN = os.getenv("CODACY_API_TOKEN")  # Token de Codacy

@app.route("/codacy/<repo_name>")
def get_codacy_metrics(repo_name):
    if not CODACY_TOKEN:
        return jsonify({"error": "Codacy API token not configured"}), 500

    headers = {"Authorization": f"Bearer {CODACY_TOKEN}"}
    response = requests.get(f"{CODACY_API_URL}/repositories/{repo_name}/issues", headers=headers)

    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch data from Codacy", "details": response.json()}), response.status_code

    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
