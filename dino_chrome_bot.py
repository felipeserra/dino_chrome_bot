import time

from PIL import ImageGrab
import pyautogui

X = 243.0  # X2 = X + 15
Y1 = 310
Y2 = 350
N = 0
N1 = 0.1
def capture_screen():
    screen = ImageGrab.grab()
    return screen

def detect_enemy(screen):
    aux_color = screen.getpixel((int(X), Y1))
    for x in range(int(X), int(X+15)):
        for y in range(Y1, Y2):
            color = screen.getpixel((x, y))
            #print(color, time.clock())
            if color != aux_color:
                return True # Return True for a detected enemy
            else:
                aux_color = color


def detect_update(screen):
    aux_color = screen.getpixel((int(X), Y1))
    for x in range(int(X), int(X+15)):
        for y in range(Y1, Y2):
            color = screen.getpixel((x, y))
            #print(color, time.clock())
            if color != aux_color:
                return True # Return True for a detected enemy
            else:
                aux_color = color                


# Dino Jumps
def jump():
    global X
    global N
    N +=1
    print(N)
    pyautogui.press("up")
    if (N == 7):
        X += (1.1+N1)  # Increment in detection region for increase speed of game
        N = 0

print("Start in 3 seconds...")
time.sleep(3)

# Infinite Loop of bot
while True:
    screen = capture_screen()
    if detect_enemy(screen):
        jump()
