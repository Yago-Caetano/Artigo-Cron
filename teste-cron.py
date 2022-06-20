
import getopt
import sys

import Adafruit_BBIO.GPIO as GPIO

#GPIO onde o LED está conectado
LED = "P8_8" 

def main(args):
    try:
        GPIO.setup(LED, GPIO.OUT)
        optlist,args = getopt.getopt(args,'',['led='])

        opt,arg = optlist[0]

        if "on" == arg:
            turnOn()
        elif "off" == arg:
            turnOff()
        

    except getopt.GetoptError as err:
        print("Ivalid arguments")


def turnOn():
    GPIO.output(LED,GPIO.HIGH)

def turnOff():
    GPIO.output(LED,GPIO.LOW)

if __name__ == "__main__":
   main(sys.argv[1:])