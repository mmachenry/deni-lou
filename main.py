import time
import board
import neopixel
import digitalio  # needed for button
from analogio import AnalogIn

mode_pin = digitalio.DigitalInOut(board.A0)
mode_pin.direction = digitalio.Direction.INPUT
mode_pin.pull = digitalio.Pull.DOWN

pixel_pin = board.A1  # lights data
analog_in = AnalogIn(board.A3)  # potentiometer
num_pixels = 16

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, auto_write=False)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
TEAL = (0, 250, 250)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
SOFTWHITE = (255, 200, 100)


light_mode = 0
previous_mode_pin = False  # prior consecutive assessment of button held down or not


# BUTTON SELECT
def handle_mode_button():
    global mode_pin
    global previous_mode_pin
    global light_mode
    print(mode_pin.value, previous_mode_pin)
    if mode_pin.value is True and previous_mode_pin is False:

        light_mode += 1
        if light_mode == 8:
            light_mode = 0

    previous_mode_pin = mode_pin.value
    print(light_mode)


# RAINBOW FADE
# https://jjmojojjmojo.github.io/time-based-fading.html below class 1 loop fader



class LoopFader:
    def __init__(self, palette):
        self.palette = palette
        self.index = 0

    @property
    def color(self):
        color = self.palette[self.index]
        self.index += 1
        if self.index > len(self.palette) - 1:
            self.index = 0
        return color


pride = (
    4980736,
    4980736,
    4981248,
    4982272,
    4984064,
    4986880,
    4990720,
    4996096,
    3951616,
    1592320,
    412672,
    19456,
    13312,
    5126,
    1048,
    60,
    76,
    65612,
    327756,
    852044,
    1507367,
    2359309,
    3538946,
    4980736,
)

fader = LoopFader(pride)
# end of loop fader


while True:
    handle_mode_button()
    pixels.brightness = 1.0
    # pixels.brightness = analog_in.value / 65536    #potentiometer
    if light_mode == 0:
        print("here")
        pixels.fill(SOFTWHITE)
    elif light_mode == 1:
        pixels.fill(RED)
    elif light_mode == 2:
        pixels.fill(BLUE)
    elif light_mode == 3:
        pixels.fill(TEAL)
    elif light_mode == 4:
        pixels.fill(GREEN)
    elif light_mode == 5:
        pixels.fill(YELLOW)
    elif light_mode == 6:
        pixels.fill(WHITE)
    elif light_mode == 7:
        print("there")
        pixels.fill(fader.color)

    pixels.show()
    time.sleep(0.1)

