import time
import board
import neopixel
import digitalio      #needed for button
from analogio import AnalogIn
   
mode_pin = digitalio.DigitalInOut(board.BUTTON_A) #check button   #mode button (color change)
mode_pin.direction = digitalio.Direction.INPUT #input not output because it is going from the button to the trinket, not the other way

pixel_pin = board.A1              #lights data
analog_in = AnalogIn(board.A3)    #potentiometer
num_pixels = 16

pixels = neopixel.NeoPixel(pixel_pin, num_pixels,  auto_write=False)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
TEAL = (0, 250, 250)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
SOFTWHITE = (255, 200, 100)

#https://jjmojojjmojo.github.io/time-based-fading.html below class 1 loop fader

rgb = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=1.0, auto_write=False)

class LoopFader:
    def __init__(self, palette):
        self.palette = palette
        self.index = 0

    @property
    def color(self):
        color = self.palette[self.index]
        self.index += 1
        if self.index > len(self.palette)-1:
            self.index = 0
        return color

pride = (4980736, 4980736, 4981248, 4982272, 4984064, 4986880, 4990720, 4996096, 3951616, 1592320, 412672, 19456, 13312, 5126, 1048, 60, 76, 65612, 327756, 852044, 1507367, 2359309, 3538946, 4980736)


fader = LoopFader(pride)

while True:
    rgb.fill(fader.color)
    rgb.write()
    time.sleep(0.1)

light_mode = 0
previous_mode_pin = False #prior consecutive assessment of button held down or not

def handle_mode_button ():
    if mode_pin.value == True and previous_mode_pin == False: #implied True if mode_pin.value: and false if not preveious_mode_pin
                                                              #this is a rising edge detector
        light_mode += 1
        if light_mode == 7:
            light_mode = 0
           
    previous_mode_pin = mode_pin.value
           
           

while True:
    pixels.fill(SOFTWHITE)  
    pixels.show()
    print(analog_in.value)
    time.sleep(0.1)
    pixels.brightness = analog_in.value / 65536    #potentiometer

   
    #momentary switch (clicker button that changes light color)
    handle_mode_button()

