import kivy
import RPi.GPIO as GPIO
import logging

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)  # GPIO 18
GPIO.setup(16, GPIO.OUT)  # GPIO 23
GPIO.setup(18, GPIO.OUT)  # GPIO 24
GPIO.output(12, GPIO.LOW)
GPIO.output(16, GPIO.LOW)
GPIO.output(18, GPIO.LOW)

class Lights(FloatLayout):
    def switch_light(self, id):
        GPIO.output(16, GPIO.LOW)
        GPIO.output(18, GPIO.LOW)
        GPIO.output(12, GPIO.LOW)
        if (id == 1):
            GPIO.output(12, GPIO.HIGH)
        elif (id == 2):
            GPIO.output(16, GPIO.HIGH)
        elif (id == 3):
            GPIO.output(18, GPIO.HIGH)

    def stop_lights(self):
        App.get_running_app().stop()
        GPIO.cleanup()

class LightsApp(App):
    def build(self):
        return Lights()

lights = LightsApp()
lights.run()
