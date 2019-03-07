from robot import Robot
from AX12 import AX12
from time import sleep
from math import cos

# ---------------------------   ROBOT CONSTRUCTION   --------------------------#
#creates the robot skeleton
r = Robot()

#adds motors to the robot skeleton
r.add_object(AX12(174), "motor")

precision = 10

# -------------------------   SEQUENCE DEFINITION ----------------------------#

def follow_scroll():
    position = 0

    while 1:
        
        t = 0
	while t < 100:
        	r.motor.turn(cos(t))
                t += 0.1
		sleep(0.001)



follow_scroll()
