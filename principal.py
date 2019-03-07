
from AX12 import AX12
from time import sleep
from math import cos
from random import randint

# ---------------------------   ROBOT CONSTRUCTION   --------------------------#
#creates the robot skeleton


#adds motors to the robot skeleton
#r.add_object(AX12(174), "motor")

m = AX12(173)
precision = 10

# -------------------------   SEQUENCE DEFINITION ----------------------------#

def follow_scroll(): #first robot by dongrui !
    position = 0
    t = 0
    speed = 0
    while t < 1000:
        m.turn(speed)
        speed += randint(-1,1)
        sleep(0.01)
        t += 1
    m.turn(0)



follow_scroll()
