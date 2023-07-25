from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf

i2c=I2C(0,sda=Pin(20), scl=Pin(21), freq=40000)
oled = SSD1306_I2C(128, 64, i2c)

oled.fill(0)

image = bytearray([0b00011000,
                   0b00111100,
                   0b01111110,
                   0b11011011,
                   0b11111111,
                   0b00100100,
                   0b01011010,
                   0b10100101])
fb = framebuf.FrameBuffer(image, 8, 8, framebuf.MONO_HLSB)

for i in range(0,127,16):
    for j in range(0,32,16):
        oled.blit(fb, i, j)
oled.show()