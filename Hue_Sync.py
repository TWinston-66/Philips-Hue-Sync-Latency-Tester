import turtle 
import time 

turtle.title("COLORS")

colors = ["green", "red", "blue", "orange"]

while(True):
    for x in colors: 
        time.sleep(0.5)
        turtle.bgcolor(x)