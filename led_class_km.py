import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

class Led(object):
    def __init__(self,num):
        self.num=num
        GPIO.setup(num,GPIO.OUT)
        
    def led_on(self):
        GPIO.output(self.num, GPIO.HIGH)
            
    def led_off(self):
        GPIO.output(self.num, GPIO.LOW)
        
def clean_up():
    GPIO.cleanup()
    
