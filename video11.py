# Animating an image sequence

from ursina import *


class User(Entity):
    speed = 10

    def __init__(self):
        super().__init__()
    
    def update(self):
        self.x += held_keys['d'] * time.dt * self.speed
        self.x -= held_keys['a'] * time.dt * self.speed
        self.z += held_keys['w'] * time.dt * self.speed
        self.z -= held_keys['s'] * time.dt * self.speed
        camera.x = self.x
        camera.z = self.z

        self.rotation_y += held_keys['l'] * time.dt * self.speed * 10
        self.rotation_y -= held_keys['j'] * time.dt * self.speed * 10
        camera.rotation_y = self.rotation_y


app = Ursina()

# Entity(
#     model='quad', 
#     texture='assets/run1.png',
#     position=(0, 0, 0),
#     scale=5
# )
lady_running = Animation(
    'assets/run', 
    posititon=(0, 0, 0), 
    scale=5, 
    fps=8, 
    Loop=True, 
    autoplay=True)

player = User()


app.run()