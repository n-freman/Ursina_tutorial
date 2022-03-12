# Collisions in ursina engine

from ursina import *
from random import randint


def update():
    global dx
    ball.x += dx
    hit_info = ball.intersects()
    if hit_info.hit:
        R = randint(0, 255)
        G = randint(0, 255)
        B = randint(0, 255)
        dx = -dx
        ball.color = color.rgb(R, G, B)
        if hit_info.entity in boxes:
            destroy(hit_info.entity)
            


app = Ursina()

ball = Entity(
    model='sphere', 
    scale=0.5, 
    position=(0, 0, 0),
    collider="box"
)
boxes = []
box = Entity(
    model="cube", 
    color=color.cyan, 
    texture="white_cube", 
    scale=(2, 4, 2), 
    position=(4, 0, 0),
    collider="box"
)
box1 = duplicate(box, x=-4)
boxes.append(box)
boxes.append(box1)
dx=.05

app.run()