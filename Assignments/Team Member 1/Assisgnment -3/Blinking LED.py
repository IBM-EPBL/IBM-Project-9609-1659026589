import RPi.GPIO as GPIO    
from time import sleep     

GPIO.setmode(GPIO.BOARD)  
GPIO.setup(6, GPIO.OUT)   

while True: 
    GPIO.output(6, GPIO.HIGH) 
    sleep(3)
    GPIO.output(6, GPIO.LOW) 
    sleep(3)             
