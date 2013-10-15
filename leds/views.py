# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
import RPi.GPIO as GPIO

def leds(request,action):
  action = int(action)
  if ((action != 0) and (action != 1):
    i = { 'Iniciar secuencia de leds?'}
  elif action == 1:
    i = { 'Iniciando secuencia led'}
  elif action == 0:
    i = { 'Terminando secuencia led'}
  return render_to_response('leds.html', {
    'msg': i
  }, context_instance=RequestContext(request))
