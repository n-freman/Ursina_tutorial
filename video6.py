from ursina import *


def update():
    
    for cube in cubes:
        cube.rotation_y += time.dt * 100
        cube.rotation_z += time.dt * 100
        cube.rotation_x += time.dt * 100


app = Ursina()

cubes = []
cube = Entity(model="cube", color=color.yellow, rotation=(45, 45, 0), texture="white_cube")
cubes.append(cube)

cube_2 = Entity(model="sphere", rotation=(45, 45, 0), position=(2, 0, 0), texture="kakashi.png")
cubes.append(cube_2)

cube_3 = Entity(model="cube", color=color.yellow, rotation=(45, 45, 0), position=(-2, 0, 0), texture="radial_gradient")
cubes.append(cube_3)

cube_4 = Entity(model="cube", color=color.yellow, rotation=(45, 45, 0), position=(0, 2, 0), texture="sky_sunset")
cubes.append(cube_4)

cube_5 = Entity(model="cube", color=color.yellow, rotation=(45, 45, 0), position=(0, -2, 0), texture="horizontal_gradient")
cubes.append(cube_5)

PointLight(x=-5,z=-5, color=color.red)

app.run()