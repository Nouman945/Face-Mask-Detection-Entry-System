from pyfirmata import Arduino, SERVO
#from time import sleep
 
# Setting up the Arduino board
port = 'COM6'
pin=9
board = Arduino(port)
board.digital[pin].mode = SERVO
# Need to give some time to pyFirmata and Arduino to synchronize
#sleep(5)
# Custom angle to set Servo motor angle
def setServoAngle(pin, angle):
  board.digital[pin].write(angle)
  #sleep(0.015)
def doorAutomate(val): 
    if val==0:
        setServoAngle(pin,180)
    elif val==1:
            setServoAngle(pin,40) 

