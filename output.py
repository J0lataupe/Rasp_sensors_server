from gpiozero import LED
from time import sleep

class Output :

    def __init__(self, pin):
        self.pin = pin
        self.out = LED(self.pin)


    def Led_On(self) :
        out.on()

    def Led_Off(self) :
        out.off()
