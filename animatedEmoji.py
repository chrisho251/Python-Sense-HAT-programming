from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

# create colour RGB

Y = (255, 255, 0) #YELLOW
B = (0, 0, 255)  #BLUE
R = (255, 0, 0)  #RED
W = (255,255,255)  #WHITE
O = (0,0,0)        #OFF LED
P = (255,105, 180) #PINK    

# create 3 function of emoji
def duck_logo():
    emoji = [
        B, B, B, B, B, R, R, R,
        B, W, W, W, B, B, R, R,
        B, W, P, W, B, B, B, R,
        Y, Y, W, W, B, B, B, B,
        B, B, W, W, W, W, B, W,
        B, W, W, W, W, W, W, W,
        B, W, W, W, W, W, W, W,
        B, B, W, W, W, W, W, B,
    ]
    return emoji
    
def drunk_logo():
    emoji = [
        O, R, R, R, R, R, B, B,
        R, R, R, R, R, R, R, B,
        R, W, O, R, R, W, O, R,
        R, W, W, R, R, W, W, R,
        R, R, R, R, R, R, R, R,
        R, R, O, O, O, R, R, R,
        R, R, O, R, O, R, R, R,
        O, R, R, R, R, R, R, O,
    ]
    return emoji
  
def coolFace_logo():
    emoji = [
        Y, Y, Y, Y, Y, Y, Y, Y,
        Y, Y, Y, Y, Y, Y, Y, Y,
        B, B, B, B, B, B, B, B,
        B, B, B, Y, Y, B, B, B,
        B, B, B, Y, Y, B, B, B,
        Y, R, R, R, R, R, R, Y,
        Y, Y, R, R, R, R, Y, Y,
        Y, Y, Y, Y, Y, Y, Y, Y,
    ]
    return emoji

# create the list name of function    
images = [coolFace_logo, drunk_logo, duck_logo]

# create function to show the emoji

def showEmoji():
    for m in range(3): 
        for n in range (0,len(images)):
            sense.set_pixels(images[n]())
            time.sleep(1)
    sense.clear()
# define main
def main():
    showEmoji()

#run main
if __name__== "__main__":
    main()