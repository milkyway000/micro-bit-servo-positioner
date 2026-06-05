# Servo Positioner
# By Oliver Deja
# Created 6/3/2026
# Modified 6/3/2026

from microbit import *
import pins

# Sweeps servo to check movement when button A is pressed
def sweep():
    pins.servo_write_pin(AnalogPin.P0, 0)
    basic.pause(2000)
    pins.servo_write_pin(AnalogPin.P0, 180)
    basic.pause(2000)
    pins.servo_write_pin(AnalogPin.P0, 90)
input.on_button_pressed(Button.A, sweep)
