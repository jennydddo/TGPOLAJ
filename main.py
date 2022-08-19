<<<<<<< HEAD
from pygame import * 
width = 1200
height = 600
window = display.set_mode((height, width))
=======
from pygame import *

win_width = 1700
win_height = 1700

>>>>>>> cb73849 (Added a the basis of functions, etc)

class GameSprite(sprite.Sprite):
    def __init__(self, imageFile, x, y, width, height, speed):
        super().__init__()
        self.image = transform.scale(image.load(imageFile), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed


class Player(GameSprite):
    def move(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < (win_width - self.rect.x):
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < (win_height - self.rect.y):
            self.rect.y += self.speed

    def update(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def gravity(self):
        self.rect.y += self.speed
        # if is_touching_ground:
        # space = key.get_pressed()
        # if space[K_w] and self.rect.y > 0:
        # self.rect.y -= self.speed


class Enemy(GameSprite):
    pass

<<<<<<< HEAD
shift = 0 
speed = 0
for event in event.get():
    if event.type == KEYDOWN: 
        if event.key == K_d:
            speed = 5 
        elif event.key == K_a: 
            speed = -5 
    elif event.type == KEYUP: 
        if event.key == K_d:
            speed = 0 
        elif event.key == K_a: 
            speed = 0

left_bound = width / 40 
right_bound = width - left_bound
# if screen.rect.x > right_bound or screen.rect.x < left_bound: 
#     screen.rect.x -= shift

shift += speed  
local_shift = shift % width
window.blit("background",(local_shift,0))
if local_shift != 0: 
    window.blit("background",(local_shift - width,0))

class Platform(sprite.Sprite): 
    def __init__(self,x,y,w,h,color): 
        super().__init__()
        self.image = Surface((w,h))
        self.rect = self.image.get_rect()
        self.image.fill(color)
        self.rect.x = x
        self.rect.y = y
        self.color = color
    def draw(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class MovingPlatform(Platform): 
    changex = 0 
    chagey = 0 
    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0
    player = None
def update(self):
    self.rect.x += self.change_x

    
window = display.set_mode((1000,670))
background = transform.scale(image.load("scifi background.webp"),(1000,670))
clock = time.Clock()
=======
>>>>>>> cb73849 (Added a the basis of functions, etc)

window = display.set_mode((1000, 670))
# background = transform.scale(image.load("scifi background.png"),(1000,670))
clock = time.Clock()
male = Player("New Piskel.gif", 30, 400, 70, 70, 5)
enemy = Enemy("New Piskel1.gif", 700, 400, 70, 70, 5)
flag = True
# please draw the walls and input parameters jenny -lucas
souls = 0


class Souls(GameSprite):
    pass
    # enemy death by colidding with player, weapons, etc...
    # Example code: if sprite.collide_rect(spaceship, alien):
    # if on_enemy_death:
    # souls += 1


class Weapon(GameSprite):
    # soul consumption on weapon or ability use...
    pass
    if souls > 0:
        # use weapon then minus soul
        keybind = key.get_pressed()
        if keybind[K_q]:
            # use weapon , enemy killed
            souls -= 3


laser = Weapon("deathlaser.png", 30, 30, 200, 200, 5)

while flag:
    for e in event.get():
        if e.type == QUIT:
            flag = False
    # window.blit(background,(0,0))
    male.update()
    male.move()
    enemy.update()
    laser.update()
    display.update()
    clock.tick(60)
