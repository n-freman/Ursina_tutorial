from ursina import *


def update():
    # cube.x = cube.x + time.dt
    # cube.y = cube.y + time.dt
    # cube.z = cube.z + time.dt * 5
    cube.rotation_x += time.dt * 10
    cube.rotation_z = cube.rotation_z + time.dt * 10


app = Ursina()
cube = Entity(
    model='cube',
    color=color.red, rotation_y=45
)

PointLight(x=-2, y=0, z=0, color=color.yellow)

app.run()