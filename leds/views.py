# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
import RPi.GPIO as GPIO
from time import sleep

def leds(request,action):
  action = int(action)
  if (action != 0) and (action != 1):
    i = { 'Iniciar secuencia de leds?'}
  elif action == 1:
    i = { 'Iniciando secuencia led'}
    secuencia(action)
  elif action == 0:
    i = { 'Terminando secuencia led'}
    secuencia(action)
  return render_to_response('leds.html', {
    'msg': i
  })

def secuencia(encendido):
  if encendido == 0:
    white.stop()
    red.stop()
    GPIO.cleanup()
  elif encendido == 1:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(24, GPIO.OUT)
    GPIO.setup(25, GPIO.OUT)

    white = GPIO.PWM(25, 100)
    red = GPIO.PWM(24,100)
    rest = 0.02
    while True:
      for i in range(0,100):
        white.ChangeDutyCycle(i)
        red.ChangeDutyCycle(100 - i)
        sleep(rest)
      for i in range(0,101):
        white.ChangeDutyCycle(100-1)
        red.ChangeDutyCycle(i)
        sleep(rest)