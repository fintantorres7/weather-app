#!/usr/bin/env python
from pprint import pprint as pp
import pandas as pd
from flask import (Flask, jsonify, render_template, request)
from weather import query_api

app = Flask(__name__)


def read_csv(csv_file_path):
    try:
        data = pd.read_csv(csv_file_path)
        return data.to_dict(orient='records')
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/')
def index():
    # Path to the file CSV
    csv_file_path = 'data/cities_list.csv'
    cities_list = read_csv(csv_file_path=csv_file_path)
    return render_template('weather.html', data=cities_list)


@app.route("/result", methods=['GET', 'POST'])
def result():
    data = []
    error = None
    select = request.form.get('comp_select')
    resp = query_api(select)
    pp(resp)
    if resp:
        data.append(resp)
    if len(data) != 2:
        error = 'Bad Response from Weather API'
    return render_template('result.html', data=data, error=error)


if __name__ == '__main__':
    app.run(debug=True)
