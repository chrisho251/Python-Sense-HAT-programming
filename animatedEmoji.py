# Import the required libraries
from sense_hat import SenseHat
import time

# Create a sense object
sense = SenseHat()

# Set up the color for emoji
r = (255, 0, 0)          # Red
m = (128, 0, 0)          # Maroon
p = (255, 105, 180)      # Pink
y = (255, 255, 0)        # Yellow
b = (0, 0, 0)            # Black
w = (255, 255, 255)      # White
g = (0, 128, 0)          # Green
db = (30, 144, 255)      # Dodger blue
lc = (224, 255, 255)     # Light cyan
s = (160, 82, 45)        # Sienna

# Create some pixel arts
frog = [
    lc, lc, lc, lc, lc, lc, lc, lc,
    lc, g, g, lc, lc, g, g, lc,
    g, g, g, g, g, g, g, lc,
    g, g, w, b, g, w, b, lc,
    g, g, g, g, g, g, g, lc, 
    db, g, s, s, s, s, s, lc,
    db, g, g, g, g, g, lc, lc,
    db, db, db ,db ,db ,db, lc, lc, 
]

pikachu = [
    g, b, b, g, g, g, g, b,
    g, g, y, s, g, g, g, s,
    g, g, g, y, y, y, y, s,
    s, s, g, y, b, y, y, b,
    s, s, y, r, y, y, y, s,
    g, m, g, y, s, s, s, g,
    g, m, y, s, y, s, y, g,
    g, g, y, s, m, m, s, g,
]

# Create list for pixel arts
list_pic = [frog, pikachu]

# Insert picture into the sense HAT
for i in list_pic:
    sense.set_pixels(i)
    time.sleep(3)


