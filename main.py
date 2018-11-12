#!/usr/bin/env python

from flask import Flask, render_template, Response, send_from_directory, request, make_response
import json, datetime
from ml.model import Model

#harsh testing pushing

#NUS Start Date for Sem 1
#13/08/18
nus_startDate_sem1_before = datetime.datetime(2018, 8, 6)
nus_startDate_sem1_after = datetime.datetime(2018, 9, 22)
#NUS Start Date for Sem 1
#14/01/19
nus_startDate_sem2_before = datetime.datetime(2019, 1, 7)
nus_startDate_sem2_after = datetime.datetime(2019, 2, 23)

ml_model = Model('data/model.json', 'data/model.h5')
ml_model.model._make_predict_function()

app = Flask(__name__, static_url_path='')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('img', path)

@app.route('/video/<path:path>')
def send_vid(path):
    return send_from_directory('video', path)

@app.route('/fonts/<path:path>')
def send_fonts(path):
    return send_from_directory('fonts', path)

@app.route('/pages/<path:path>')
def send_pages(path):
    return send_from_directory('pages', path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/estimate', methods=['POST'])
def estimate():

  data = request.form

  #retrieve inputDate & inputTime from the body of request
  inputDate = data.get("inputDate")
  inputTime = data.get("inputTime")
  #format
  datetime_object = datetime.datetime.strptime(inputDate, "%d/%m/%Y")
  time_object = datetime.datetime.strptime(inputTime, '%H:%M').time()

  #retrieve the sem
  retrieveSem = findSem(datetime_object)

  #retrieve week
  retrieveWeek = int(findWeek(datetime_object, retrieveSem))

  #retrieve day
  retrieveDay = datetime_object.weekday() + 1

  dataArr = [retrieveSem, retrieveWeek, retrieveDay]

  #ml_input = process_data(data)
  prediction = ml_model.predict(dataArr)

  #retrieve estimation through the input time
  retrieveEstimation = findEstimationThroughTime(time_object, prediction)

  resp = make_response(json.dumps({'result': retrieveEstimation}))
  resp.status_code = 200
  resp.headers['Access-Control-Allow-Origin'] = '*'
  return resp

def findSem(inputDate):
  if inputDate >= nus_startDate_sem2_before:
    return 2
  else:
    return 1

def findWeek(inputDate, sem):
  if sem == 1:
    if inputDate > nus_startDate_sem1_after:
      return (((inputDate - nus_startDate_sem1_after).days / 7.0) + 6)
    else:
      return (inputDate - nus_startDate_sem1_before).days / 7.0
  else:
    if inputDate >nus_startDate_sem2_after:
      return ((inputDate - nus_startDate_sem2_after).days / 7.0) + 6
    else:
      return (inputDate - nus_startDate_sem2_before).days / 7.0

def findEstimationThroughTime(inputTime, prediction):
  if inputTime.hour > 7:
    return prediction[1] - prediction[0]
  else:
    return prediction[0]

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True, threaded=True)
