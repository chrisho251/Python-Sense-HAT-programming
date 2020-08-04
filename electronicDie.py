from sense_hat import SenseHat
import time
import random


# set up environment
sense = SenseHat()
sense.clear()

# set up the RGB colour
w = [0, 0, 0]
b = [255, 255, 255]
r = [255, 0, 0]

# create and set the pixel of die's faces
one = [
    w,w,w,w,w,w,w,w,
    w,w,w,w,w,w,w,w,
    w,w,w,w,w,w,w,w,
    w,w,w,r,r,w,w,w,
    w,w,w,r,r,w,w,w,
    w,w,w,w,w,w,w,w,
    w,w,w,w,w,w,w,w,
    w,w,w,w,w,w,w,w,
]

two = [
    w,w,w,w,w,w,w,w,
    w,r,r,w,w,w,w,w,
    w,r,r,w,w,w,w,w,
    w,w,w,w,w,w,w,w,
    w,w,w,w,w,w,w,w,
    w,w,w,w,r,r,w,w,
    w,w,w,w,r,r,w,w,
    w,w,w,w,w,w,w,w,
]

three = [
    b,b,w,w,w,w,w,w,
    b,b,w,w,w,w,w,w,
    w,w,w,w,w,w,w,w,
    w,w,w,b,b,w,w,w,
    w,w,w,b,b,w,w,w,
    w,w,w,w,w,w,w,w,
    w,w,w,w,w,w,b,b,
    w,w,w,w,w,w,b,b,
]

four = [
    w,w,w,w,w,w,w,w,
    w,r,r,w,w,r,r,w,
    w,r,r,w,w,r,r,w,
    w,w,w,w,w,w,w,w,
    w,w,w,w,w,w,w,w,
    w,r,r,w,w,r,r,w,
    w,r,r,w,w,r,r,w,
    w,w,w,w,w,w,w,w,
]

five = [
    b,b,w,w,w,w,b,b,
    b,b,w,w,w,w,b,b,
    w,w,w,w,w,w,w,w,
    w,w,w,b,b,w,w,w,
    w,w,w,b,b,w,w,w,
    w,w,w,w,w,w,w,w,
    b,b,w,w,w,w,b,b,
    b,b,w,w,w,w,b,b,
]

six = [
    r,r,w,w,w,w,r,r,
    r,r,w,w,w,w,r,r,
    w,w,w,w,w,w,w,w,
    r,r,w,w,w,w,r,r,
    r,r,w,w,w,w,r,r,
    w,w,w,w,w,w,w,w,
    r,r,w,w,w,w,r,r,
    r,r,w,w,w,w,r,r,
]
# creat function to roll dice
def roll_die():
    # detect the motion
    while True:
        acceleration = sense.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']

        x = round(x, 0)
        y = round(y, 0)
        z = round(z, 0)

        #if the coordinates x, y, z change, die'face will randomly displayed
        if x > 1 or y > 1 or z > 1:
            face = random.randint(1,6)
            if face == 1:
                sense.set_pixels(one)
                time.sleep(1)
                sense.show_message("You get" + str(face), text_colour=r, scroll_speed=0.09)
            elif face == 2:
                sense.set_pixels(two)
                time.sleep(1)
                sense.show_message("You get" + str(face), text_colour=r, scroll_speed=0.09)
            elif face == 3:
                sense.set_pixels(three)
                time.sleep(1)
                sense.show_message("You get " + str(face), text_colour=r, scroll_speed=0.09)
            elif face == 4:
                sense.set_pixels(four)
                time.sleep(1)
                sense.show_message("You get " + str(face), text_colour=r, scroll_speed=0.09)
            elif face == 5:
                sense.set_pixels(five)
                time.sleep(1)
                sense.show_message("You get " + str(face), text_colour=r, scroll_speed=0.09)
            elif face == 6:
                sense.set_pixels(six)
                time.sleep(1)
                sense.show_message("You get " + str(face), text_colour=r, scroll_speed=0.09)

# show instruction
sense.show_message("Shake to roll the die", scroll_speed=0.06)
# call function to roll die
roll_die() 

