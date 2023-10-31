"""
Created by: Ihor Chernyshev
Created on: Oct 2023
This module is a Micro:bit MicroPython program
"""

from microbit import *
import neopixel
from machine import time_pulse_us

display.clear()
np = neopixel.NeoPixel(pin16, 4)
np[0] = (0, 0, 0)
np[1] = (0, 0, 0)
np[2] = (0, 0, 0)
np[3] = (0, 0, 0)
np.clear()
display.show(Image.HAPPY)

tring = pin1
echo = pin2

tring.write_digital(1)
echo.read_digital()

while True:
    if button_a.was_pressed():
        tring.write_digital(1)
        tring.write_digital(0)
        micros = time_pulse_us(echo, 2)
        t_echo = micros / 1000000
        dist_cm = (t_echo / 2) * 34300
    if dist_cm < 10:
        np[0] = (255, 0, 0)
        np[1] = (255, 0, 0)
        np[2] = (255, 0, 0)
        np[3] = (255, 0, 0)
        print(np[0], np[1], np[2], np[3])
        np.show()
        sleep(1000)
        np.clear()
        display.show(Image.HAPPY)
    elif dist_cm >= 10:
        np[0] = (0, 0, 0)
        np[1] = (0, 0, 0)
        np[2] = (0, 0, 0)
        np[3] = (0, 0, 0)
        print(np[0], np[1], np[2], np[3])
        np.show()
        sleep(1000)
        np.clear()
        display.show(Image.HAPPY)
