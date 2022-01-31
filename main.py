import time
import board
import neopixel
from analogio import AnalogIn
   

pixel_pin = board.A1
analog_in = AnalogIn(board.A3)

num_pixels = 16

pixels = neopixel.NeoPixel(pixel_pin, num_pixels,  auto_write=False)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
SOFTWHITE = (251, 250, 200)

while True:
    pixels.fill(SOFTWHITE)  
    pixels.show()
    time.sleep(1)
    pixels.brightness=analog_in.value / 65536
