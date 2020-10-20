from flask import render_template, url_for, request
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
trig = 17
echo = 27
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    distance = sensor_1()
    return render_template("sensor.html", distance=distance)

def sensor_1():
    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)
    while GPIO.input(echo)==0:
        pulse_s = time.time()
    while GPIO.input(echo)==1:
        pulse_e = time.time()
    pulse_d = pulse_e - pulse_s
    d = 34000*pulse_d/2
    return int(d)
if __name__ == "__main__":
    app.run(host = '0.0.0.0',port=4556,debug=True)
