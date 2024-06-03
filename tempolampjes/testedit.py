import time
from rpi_ws281x import PixelStrip, Color

# LED strip configuration
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10  # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)

class GroveWS2813RgbStrip(PixelStrip):
    def __init__(self, pin, count, brightness=None):
        ws2812_pins = {12: 0, 13: 1, 18: 0, 19: 1}
        if not pin in ws2812_pins.keys():
            print("OneLedTypedWs2812: pin {} could not be used with WS2812".format(pin))
            return
        channel = ws2812_pins.get(pin)

        if brightness is None:
            brightness = LED_BRIGHTNESS

        # Create PixelStrip object with appropriate configuration.
        super(GroveWS2813RgbStrip, self).__init__(
            count,
            pin,
            LED_FREQ_HZ,
            LED_DMA,
            LED_INVERT,
            brightness,
            channel
        )

        # Initialize the library (must be called once before other functions).
        self.begin()

def flash(strip, color, num_flashes=3, flash_duration=0.5):
    """Flash all LEDs three times."""
    for _ in range(num_flashes):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, color)
        strip.show()
        time.sleep(flash_duration)

        for i in range(strip.numPixels()):
            strip.setPixelColor(i, 0)
        strip.show()
        time.sleep(flash_duration)

def colorWipe3(strip, color, wait_ms=10, num_repeats=10):
    """Wipe color across the LED strip with a group of three LEDs at a time."""
    
    # Flash all LEDs three times
    flash(strip, color, num_flashes=3, flash_duration=1)

    # Clear all LEDs
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, 0)
    strip.show()

    # Repeat color wipe effect
    for _ in range(num_repeats):
        for i in range(strip.numPixels() - 2):
            strip.setPixelColor(i, color)
            strip.setPixelColor(i + 1, color)
            strip.setPixelColor(i + 2, color)
            strip.show()
            time.sleep(wait_ms / 1000.0)
            strip.setPixelColor(i, 0)
            strip.setPixelColor(i + 1, 0)
            strip.setPixelColor(i + 2, 0)

    # Turn off all LEDs after the color wipe effect
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, 0)
    strip.show()

def main():
    from grove.grove_ws2813_rgb_led_strip import GroveWS2813RgbStrip
    from grove.helper import SlotHelper
    from rpi_ws281x import Color

    sh = SlotHelper(SlotHelper.PWM)
    pin = sh.argv2pin(" [led-count]")

    import sys
    count = 30
    if len(sys.argv) >= 3:
        count = int(sys.argv[2])

    strip = GroveWS2813RgbStrip(pin, count)

    print('Press Ctrl-C to quit.')
    try:
        while True:
            print('Color wipe and flash animations.')
            colorWipe3(strip, Color(255, 0, 0))  # Red wipe
            
    except KeyboardInterrupt:
        # Clear all LEDs when exit
        colorWipe3(strip, Color(0, 0, 0), 10)

if __name__ == '__main__':
    main()
