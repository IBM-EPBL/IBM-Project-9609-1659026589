from gpiozero import TrafficLights    
from time import sleep    

lights = TrafficLights(6, 8, 7)    
    
while True:    
           light.green.on()    
           sleep(2)    
           lights.amber.on()    
           sleep(2)    
           lights.red.on()    
           sleep(2) 
