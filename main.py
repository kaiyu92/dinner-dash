#!/usr/bin/env python

from flask import Flask, render_template, Response, send_from_directory, request, make_response
import json, datetime

#NUS Start Date for Sem 1
#13/08/18
nus_startDate_sem1_before = datetime.datetime(2018, 8, 6)
nus_startDate_sem1_after = datetime.datetime(2018, 9, 22)
#NUS Start Date for Sem 1
#14/01/19
nus_startDate_sem2_before = datetime.datetime(2019, 1, 7)
nus_startDate_sem2_after = datetime.datetime(2019, 2, 23)

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

@app.route('/estimate', methods=['POST'])
def estimate():

  data = request.form

  #retrieve inputDate & inputTime from the body of request
  inputDate = data.get("inputDate")
  inputTime = data.get("inputTime")
  datetime_object = datetime.datetime.strptime(inputDate, "%d/%m/%Y")
  time_object = datetime.datetime.strptime(inputTime, '%H:%M').time()

  #retrieve the sem
  retrieveSem = findSem(datetime_object)

  #retrieve week
  retrieveWeek = int(findWeek(datetime_object, retrieveSem))

  #retrieve day
  retrieveDay = datetime_object.weekday() + 1

  #ml_input = process_data(data)
  #prediction = predict(ml_input)

  resp = make_response(json.dumps({'Sem': retrieveSem, 'Week': retrieveWeek, 'Day': retrieveDay}))
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


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True, threaded=True)