# Entity class and object

from turtle import position
from ursina import *


class Player(Entity):

    def __init__(self, x, speed):
        super().__init__()
        self.model = 'cube'
        self.color = color.red
        self.scale_y = 2
        self.x = x
        self.speed = speed
        self.texture = 'white_cube'
    
    def update(self):
        self.x += held_keys['d'] * time.dt * self.speed
        self.x -= held_keys['a'] * time.dt * self.speed
        self.z += held_keys['w'] * time.dt * self.speed
        self.z -= held_keys['s'] * time.dt * self.speed
        camera.x = self.x
        camera.z = self.z - 7
    
    def input(self, key):
        if key == 'space':
            self.color = color.random_color()
        
        if key == 'r':
            self.rotation_z += time.dt * 500

        if key == '0':
            Player.reset(self)
    
    def reset(self):
        self.color = color.red
        self.rotation_z = 0
        self.x = x


app = Ursina()

cube = Entity(
    model="cube",
    color=color.green,
    position=(0, 0, 1),
    scale=1.5,
    rotation=(0, 0, 45),
    texture="brick"
    )
x = -2
speed = 10
player = Player(x, speed)

app.run()