import pandas as pd

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)
df = pd.read_csv(r'C:\Users\Mahvish Fatima\Downloads\Travel_Data.csv')


@app.route("/")
def main():
    return "hello", 200


@app.route("/get_travel", methods=["GET"])
def get_travel():
    return jsonify(travel)


@app.route("add_travel", methods=["POST"])
def add_travel():
    data = request.get_json()
    if data is None:
        return jsonify({'error': 'Data is required'}), 400

    return jsonify({'message': 'Record added successfully'}), 201


if __name__ == "main":
    app.run(debug=True)
