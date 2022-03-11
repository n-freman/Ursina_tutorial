from ursina import *


def update():
    knife.rotation_y += time.dt*10


app = Ursina()

knife = Entity(
    model='Earth/earth_model.obj', 
    texture='Earth/Earth_diff.jpg', 
    rotation_x=-90,
    y=-1,
    scale=0.007)

app.run()