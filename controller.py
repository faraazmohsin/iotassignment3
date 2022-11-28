# Controllerservice
import RPi.GPIO as GPIO
import time
import sqlite3 as lite
import sys

con = lite.connect('database.sqlite')
cur = con.cursor()

GPIO.setmode(GPIO.BCM)
threshold = 1000
LDR_PIN = 18
LIGHT_PIN = 25


def readldr(PIN):
    reading = 0
    GPIO.setup(PIN, GPIO.OUT)
    GPIO.output(PIN, GPIO.LOW)
    time.sleep(0.1)
    GPIO.setup(PIN, GPIO.IN)
    while GPIO.input(PIN) == GPIO.LOW:
        reading = reading + 1
    return reading


def switchOnLight(PIN):
    GPIO.setup(PIN, GPIO.OUT)
    GPIO.output(PIN, GPIO.HIGH)


def switchOffLight(PIN):
    GPIO.setup(PIN, GPIO.OUT)
    GPIO.output(PIN, GPIO.LOW)


def runAutoMode():
    ldr_reading = readldr(LDR_PIN)
    if ldr_reading < threshold:
        switchOnLight(LIGHT_PIN)
        setCurrentState('on')
    else:
        switchOffLight(LIGHT_PIN)
        setCurrentState('off')


def runManualMode():
    state = getCurrentState()
    if state == 'on':
        switchOnLight(LIGHT_PIN)
        setCurrentState('on')
    elif state == 'off':
        switchOffLight(LIGHT_PIN)
        setCurrentState('off')


def getCurrentMode():
    cur.execute('SELECT * FROM myapp_mode')
    data = cur.fetchone()  # (1, u'auto')
    return data[1]


def getCurrentState():
    cur.execute('SELECT * FROM myapp_state')
    data = cur.fetchone()  # (1, u'on')
    return data[1]


def setCurrentState(val):
    query = 'UPDATE myapp_state set name="' + val + '"'
    cur.execute(query)


while True:
    currentMode = getCurrentMode()
    if currentMode == 'auto':
        runAutoMode()
    elif currentMode == 'manual':
        runManualMode()
    time.sleep(5)
