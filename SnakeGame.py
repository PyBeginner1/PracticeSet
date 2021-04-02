from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(0, 0)]
aim = vector(0, -10)

def change(x,y):
    #represents x axis
    aim.x = x
    #represents y axis
    aim.y = y

#creating boundary
def boundary(head):
    return -200 < head.x < 200 and -200 < head.y < 200

def move():

    head = snake[-1].copy()
    #-1 is to make snake move forward 1 segment & copies itself after
    head.move(aim)

    if not boundary(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'green')

    #food representation
    square(food.x, food.y, 9, 'red')
    update()
    ontimer(move, 100)


#to hide turtle to speedup
hideturtle()
#brings object back to initial state
tracer(False)
#continuously update the game every second
listen()
onkey(lambda:change(0,10), 'Up')
onkey(lambda:change(0,-10), 'Down')
onkey(lambda:change(10,0),'Right')
onkey(lambda:change(-10,0),'Left')

move()
done()