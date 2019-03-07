
from AX12 import AX12
from time import sleep
from math import cos
from random import random

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
    speed = 70
    while t < 1000:
        if random() > 0.90:
            m.turn(speed)
            sleep(0.1)
        if random() > 0.90:
            m.turn(-speed)
            sleep(0.1)
        m.turn(0)
        sleep(0.001)
        t += 1
    m.turn(0)



follow_scroll()
