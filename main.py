"""
Author: Nick St. Pierre
Filename: main.py
Description: File used for testing the motor methods.
"""

from automobile import Automobile
from motor import Motor
import pygame

SCREEN_SIZE = (500,500)

def main():
    
    RUNNING = True
    pygame.init()
    pygame.display.set_caption("SERVO TEST")
    screen = pygame.display.set_mode(list(SCREEN_SIZE))
    
    robot = Automobile(Motor("GPIO17"),
                       Motor("GPIO27"),
                       Motor("GPIO22"),
                       Motor("GPIO23"))
    
    while RUNNING:
      
      # event handling, gets all event from the eventqueue
      for event in pygame.event.get():
         # only do something if the event is of type QUIT or ESCAPE is pressed
         if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            # change the value to False, to exit the main loop
            RUNNING = False
         elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_UP:
                  # change to up arrow
                  robot.drive()
               elif event.key == pygame.K_DOWN:
                  robot.reverse()
               elif event.key == pygame.K_RIGHT:
                  robot.turnRight()
               elif event.key == pygame.K_LEFT:
                  robot.turnLeft()
         elif event.type == pygame.KEYUP:
            robot.park()       
    pygame.quit()
    
if __name__ == '__main__':
    main()