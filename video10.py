# Button and mouse

from ursina import *
from random import randint


def update():
    if held_keys['q']:
        destroy(B)


def print_text():
    print_on_screen('Hello', position=(randint(-3, 3)*.1, randint(-3, 3)*.1))


def colors():
    B.color = color.random_color()


app = Ursina()

B = Button(
    color=color.azure,
    text='Button',
    text_color=color.green,
    scale=.5,
    # icon='kakashi.png',
    text_origin=(-0.5, 0)
)
B.on_click = print_text
B.tooltip = Tooltip("Click me")


mouse.visible = False


app.run()