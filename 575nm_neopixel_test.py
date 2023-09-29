import time
import board
import neopixel

# On a Raspberry pi, use this instead, not all pins are supported
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 8


# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.5, auto_write=False, pixel_order=ORDER
)

while True:
    # Comment this line out if you have RGBW/GRBW NeoPixels
    pixels.fill((240, 255, 0))
    # Uncomment this line if you have RGBW/GRBW NeoPixels
    # pixels.fill((255, 0, 0, 0))
    pixels.show()
    time.sleep(1)
