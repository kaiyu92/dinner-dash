#!/usr/bin/env python

from flask import Flask, render_template, Response, send_from_directory, request, make_response
import json, datetime

#NUS Start Date for Sem 1
#13/08/18
nus_startDate_sem1 = datetime.datetime(2018, 8, 13)
nus_startDate_sem2 = datetime.datetime(2019, 1, 14)
app = Flask(__name__, static_url_path='')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/images/<path:path>')
def send_img(path):
    return send_from_directory('images', path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_reference', methods=['POST'])
def check_reference():
  resp = make_response(json.dumps("TO BE FILLED"))
  resp.status_code = 200
  resp.headers['Access-Control-Allow-Origin'] = '*'
  return resp

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True, threaded=True)