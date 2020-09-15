"""
Author: Nick St. Pierre
Filename: main.py
Description: File used for testing the motor methods.
"""

from motor import Motor
import pygame


def main():
    
    motor1 = Motor("GPIO17")
    
    motor1.forward()
    motor1.backward()
    
if __name__ == '__main__':
    main()

