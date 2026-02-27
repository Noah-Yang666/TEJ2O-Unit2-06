"""
Created by: Noah
Created on: Feb 2026
This module is a Micro:bit MicroPython program that turns a light on and off.
"""

from microbit import *

display.clear()
pin16.write_digital(0)
display.show(Image.HAPPY)

# on and off
while True:
    if button_a.is_pressed():
        pin16.write_digital(1)
        display.show(Image.YES)
    if button_b.is_pressed():
        pin16.write_digital(0)
        display.show(Image.NO)
