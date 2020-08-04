from sense_hat import SenseHat
import random
import time 
import csv

# set up environment
sense = SenseHat()
sense.clear()

# set up the RGB colour
w = [0, 0, 0]
b = [255, 255, 255]
r = [255, 0, 0]
y = [255,255,0]

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

point = 0
turn = 1
score_player1 = 0
score_player2 = 0

# creat function to roll dice
def roll_die():
    global point
    while True:
        acceleration = sense.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']
        
        x = round(x, 0)
        y = round(y, 0)
        z = round(z, 0)

        if x>1.5 or y>1.5 or z>1.5:
            face = random.randint(1,6)
            if face == 1:
                sense.set_pixels(one)
                time.sleep(2)
            elif face == 2:
                sense.set_pixels(three)
                time.sleep(2)
            elif face == 4:
                sense.set_pixels(four)
                time.sleep(2)
            elif face == 5:
                sense.set_pixels(five)
                time.sleep(2)
            elif face == 6:
                sense.set_pixels(six)
                time.sleep(2)
            point = face
            break
# Start game message
def say_hello():
    sense.show_message("Game start! Shake the Pi to roll", scroll_speed=0.05)

# Bye message
def say_bye():
    sense.show_message("Thanks for playing the game")
    
# function set turn of player
def play_turn():
    global turn, score_player1, score_player2
    # player 1 turn
    if turn % 2 != 0:
        sense.show_message('Turn of Player 1', text_colour= r,scroll_speed=0.06)
        roll_die()
        score_player1 += point
        sense.show_message('Player 1 got ' + str(score_player1), scroll_speed=0.06) 
    # player 2 turn
    elif turn % 2 == 0:
        sense.show_message('Turn of Player 2', text_colour= r,scroll_speed=0.06)
        roll_die()
        score_player2 += point
        sense.show_message('Player 2 got ' + str(score_player2), scroll_speed=0.06)
    turn += 1
    return play_game()

# Function run the game
def play_game():
    global score_player1, score_player2
    time_format = time.strftime("%d/%m/%Y, %H:%M:%S", time.localtime())
    while score_player1 <= 30 and score_player2 <= 30 :
        play_turn()
        # condition of a win
        if score_player1 > 30:
            sense.show_message('Player 1 win', text_colour= y)
            # write the report when the player 1 win
            with open('winner.csv', 'a', newline='') as csv_file:
                writer = csv.writer(csv_file)
                message_1 = 'Player 1 won with ' + str(score_player1) + ' points'
                writer.writerow([time_format,message_1])
                say_bye()
            exit()

        elif score_player2 > 30:
            sense.show_message('Player 2 win', text_colour= y)
            # write the report when player 2 win
            with open('winner.csv', 'a', newline='') as csv_file:
                writer= csv.writer(csv_file)
                message_2 = 'Player 2 won with ' + str(score_player2) + ' points'
                writer.writerow([time_format,message_2])
                say_bye()
            exit()
        break

# main
def main():
    say_hello()
    play_game()
# run main
if __name__== "__main__":
    main()
