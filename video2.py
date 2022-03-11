from ursina import *

app = Ursina()

cube = Entity(
    model='cube', 
    rotation=(45, 45, 0), 
    scale_z=2, 
    position=(3, 2, 1),
    color=color.red,
    )
label = Text(text='This is a red cube!', scale_y=2, rotation=(45, 45, 0), )

PointLight(x=-2, y=2, z=-2)


app.run()