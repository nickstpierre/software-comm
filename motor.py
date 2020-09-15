"""
Author: Nick St. Pierre
Filename: mobile.py
"""

import pygame, time
from gpiozero import Servo

class Motor(Servo):
    
    def __init__ (self, servoPin):
        "Initializes the servo and has basic drive functions"
        self.servo = Servo(servoPin)
        
    def forward(self):
        "Function that drives the servos forward"
        self.servo.max()
        pause(0.05)
    
    def backward(self):
        "Function that drives the servos backward"
        self.servo.min()
        pause(0.05)
        
    def pause(time):
        "This will utilize the detach() method to reduce jitter of the servo"
        time.sleep(time)
        
        
        