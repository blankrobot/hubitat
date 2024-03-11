from flask import Flask, request, Response
import subprocess, re, time
import RPi.GPIO as GPIO
attributes = {}
led = 18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)

app = Flask(__name__)
@app.route('/hubitat/webhook', methods=['POST'])

def return_response():
  hook = request.json
  
  if hook['content']['value'] == 'closed':
    GPIO.output(led, GPIO.LOW)
  elif hook['content']['value'] == 'open':
    GPIO.output(led, GPIO.HIGH)
  ## Do something with the request.json data.
  return Response(status=200)
if __name__ == "__main__": app.run()


