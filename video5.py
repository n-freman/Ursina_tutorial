from ursina import *


def update():
    cube.x += time.dt
    camera.position = (cube.x, 0, -20)


app = Ursina()

cube = Entity(model="cube", color=color.red, scale_y=2)
cube_2 = Entity(model="cube", scale=(2, 1, 2))

app.run()