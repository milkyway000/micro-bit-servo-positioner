# micro:bit Servo Positioner
# By Oliver Deja
# Created 6/3/2026
# NOTE: This program will only run in the Microsoft MakeCode IDE.
# Only usable with positional servos.
# Button A sweeps servo, Button B sets servo to 90 degrees.

# Sweeps servo to check movement when Button A is pressed
def sweep():
    pins.servo_write_pin(AnalogPin.P0, 0)
    basic.pause(2000)
    pins.servo_write_pin(AnalogPin.P0, 180)
    basic.pause(2000)
    pins.servo_write_pin(AnalogPin.P0, 90)

# Sets servo to center
def center():
    pins.servo_write_pin(AnalogPin.P0, 90)

# Inputs
input.on_button_pressed(Button.A, sweep)
input.on_button_pressed(Button.B, center)
