#!/usr/bin/python
from flask import Flask, render_template, request, jsonify
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

app = Flask(__name__)
led_state = False

@app.route("/index2.html")
def index2():
    return render_template('index2.html')

@app.route("/")
def root():
    return render_template('index.html')

@app.route("/on")
def on():
    GPIO.output(18,GPIO.HIGH)
    return "LED is on"

@app.route("/off")
def off():
    GPIO.output(18,GPIO.LOW)
    return "LED is off"

@app.route("/toggle", methods=['POST'])
def toggle():
    global led_state
    if led_state == False:
        GPIO.output(18,GPIO.HIGH)
        led_state = not led_state
        return jsonify(status="on")

    else:
        GPIO.output(18,GPIO.LOW)
        led_state = not led_state
        return jsonify(status="off")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80')
