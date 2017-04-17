import time

import RPi.GPIO as GPIO
import Adafruit_DHT

import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


# Raspberry Pi hardware SPI config:
DC = 23
RST = 24
SPI_PORT = 0
SPI_DEVICE = 0

# Hardware SPI usage:
disp = LCD.PCD8544(DC, RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=4000000))
GPIO.setup(17, GPIO.OUT)

relay_out = True

# Initialize library.
disp.begin(contrast=60)

def refresh_temp():
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)

    # Clear display.
    disp.clear()
    disp.display()

    image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
    draw = ImageDraw.Draw(image)
    draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)

    # Load default font.
    font = ImageFont.truetype("/usr/share/fonts/truetype/roboto/Roboto-Regular.ttf", 30)
    fontHumidity = ImageFont.truetype("/usr/share/fonts/truetype/roboto/Roboto-Regular.ttf", 16)
    # Write some text.
    draw.text((0,0), '{0:0.1f} C'.format(temperature), font=font)
    draw.text((5,30), '{0:0.1f} HUM'.format(humidity), font=fontHumidity)

    disp.image(image)

    disp.display()

while True:
    time.sleep(5)
    refresh_temp()
    GPIO.output(17, relay_out)
    relay_out = not relay_out
