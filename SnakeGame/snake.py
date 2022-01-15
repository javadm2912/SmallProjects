from cProfile import label
from cgitb import text
from curses import window
from math import fabs
from tkinter import *
import random
from turtle import color, speed, width, window_height, window_width

Game_Width = 1100
Game_Height = 500
Speed = 100
Space_Size = 20
Bodi_Parts = 1
Snake_Color = "#00FF00"
Food_Color = "#FF0000"
BackGround_Color = "#000000"


class Snake:
    def __init__(self):
        self.body_size = Bodi_Parts
        self.coordinates = []
        self.squares = []

        for i in range(0,Bodi_Parts):
            self.coordinates.append([0,0])

        for x,y in self.coordinates:
            square = canvas.create_rectangle(x,y,x+Space_Size,y+Space_Size,fill=Snake_Color,tags="snake")
            self.squares.append(square)

class Food:
    def __init__(self):
        x = random.randint(0,(Game_Width/Space_Size) - 1) * Space_Size
        y = random.randint(0,(Game_Height/Space_Size) - 1) * Space_Size

        self.coordinates = [x,y]
        canvas.create_oval(x,y,x+Space_Size,y+Space_Size,fill=Food_Color,tags='food')


def next_turn(snake,food):
    x,y = snake.coordinates[0]
    global randomColor 

    if direction == "up":
        y-=Space_Size
    elif direction == "down":
        y+=Space_Size
    elif direction == "left":
        x-= Space_Size
    elif direction == "right":
        x += Space_Size

    snake.coordinates.insert(0,(x,y))

    square = canvas.create_rectangle(x,y,x+Space_Size,y+Space_Size,fill=randomColor,tags="snake")
    snake.squares.insert(0,square)


    global speed 
    global level
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        
        score += 2
        randomColor =("#"+str(random.randint(10,99))+str(random.randint(10,99))+str(random.randint(10,99)))if int(score / 10)>level else randomColor
        level = int(score / 10) 
        speed = (Speed - level * 10) if speed > 10 else speed
        scorelabel.config(text="Score : {}  ".format(score) + "Level : {}".format(level))
        canvas.delete("food")

        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_collisions(snake):
        game_over()
    else:
        window.after(speed,next_turn,snake,food)



def change_direction(new_direction):
    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    if new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    if new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    if new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_collisions(snake):
    x,y = snake.coordinates[0]
    if x < 0 or x >= Game_Width:
        return True

    if y < 0 or y >= Game_Height:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True 
    return False


def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,
        font=('consolas',70),text = "GAME OVER",fill="red" ,tags="game_over")


window = Tk()
window.resizable(False,False)
window.title("Snake Game")

randomColor = Snake_Color
speed = Speed
score = 0 
level = score % 10
direction = "down"

scorelabel = Label(window,text="Score : {}  ".format(score) + "Level : {}".format(level),font=('consolas',40))
scorelabel.pack()


canvas = Canvas(window,bg=BackGround_Color,height=Game_Height,width=Game_Width)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2)-(window_width/2))
y = int((screen_height/2)-(window_height/2))


window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>',lambda event: change_direction('left'))
window.bind('<A>',lambda event: change_direction('left'))
window.bind('<Right>',lambda event: change_direction('right'))
window.bind('<D>',lambda event: change_direction('right'))
window.bind('<Up>',lambda event: change_direction('up'))
window.bind('<W>',lambda event: change_direction('up'))
window.bind('<Down>',lambda event: change_direction('down'))
window.bind('<S>',lambda event: change_direction('down'))

snake = Snake()
food = Food()
next_turn(snake,food)



window.mainloop()
