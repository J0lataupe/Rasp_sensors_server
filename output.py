from gpiozero import LED

class Output :

    def __init__(self, pin):
        self.pin = pin
        self.out = LED(self.pin)


    def Led_On(self) :
        self.out.on()

    def Led_Off(self) :
        self.out.off()
