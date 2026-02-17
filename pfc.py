from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor

#this above is the basics in using pybricks. 
#Using the pybricks library, you import the motors and sensors needed to perform a given task.

left_motor= Motor(Port.A, direction = Direction.CLOCKWISE)
right_motor= Motor(Port.B, direction = Direction.COUNTERCLOCKWISE)

#next, you let the hub know what ports the motors are connected to, and the direction indicates whether :
#1. The positive direction of the motor is clockwise(when it is moving forward, it moves clockwise) OR
#2. The positive direction of the motor is counterclockwise(when it is moving forward, it moves counterclockwise).

#tip: let the motors have opposite directions always

sensor1= ColorSensor(port.C)
sensor2= ForceSensor(port.F)

#next, define your sensors, and tell your hub which ports the sensors are connected to.
#That's all for now.
