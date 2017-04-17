import Adafruit_DHT
import RPi.GPIO as GPIO

import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI


class LocalExecutor():

    def __init__(self):
        GPIO.setup(17, GPIO.OUT)
        # Raspberry Pi hardware SPI config:
        DC = 23
        RST = 24
        SPI_PORT = 0
        SPI_DEVICE = 0

        # Hardware SPI usage:
        disp = LCD.PCD8544(DC, RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=4000000))
        
        # Initialize library.
        disp.begin(contrast=60)

    def power_on():
        GPIO.output(17, True)

    def power_off():
        GPIO.output(17, False)

    def read_temp():
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)
        return temperature

    def display_temp(temp):
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
        draw.text((0,0), '{0:0.1f} C'.format(temp), font=font)
        draw.text((5,30), '{0:0.1f} HUM'.format(humidity), font=fontHumidity)

        disp.image(image)

        disp.display()
        return True


    def execute(self, command, *args):
        result = False
        if (command == 'on'):
            print('Execute on')
            result = True
        elif (command == 'off'):
            print('Execute off')
            result = True
        elif (command == 'temp'):
            result = read_temp()
        elif (command == 'show_temp'):
            result = display_temp(args[0])

        return result
