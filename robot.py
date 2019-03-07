
from AX12 import AX12
from time import sleep
from math import cos

# ---------------------------   ROBOT CONSTRUCTION   --------------------------#
#creates the robot skeleton


#adds motors to the robot skeleton
#r.add_object(AX12(174), "motor")

m = AX12(173)
precision = 10

# -------------------------   SEQUENCE DEFINITION ----------------------------#

def follow_scroll():
    position = 0

    while 1:
        
        t = 0
	while t < 100:
        	m.turn(cos(t))
                t += 0.1
		sleep(0.001)



follow_scroll()
