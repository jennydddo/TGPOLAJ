from turtle import back
from pygame import * 
width = 1200
height = 600
window = display.set_mode((height, width))

class GameSprite(sprite.Sprite):
    def __init__(self, imageFile, x, y, width, height, speed):
        super().__init__()
        self.image = transform.scale(image.load(imageFile),(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    
    def update(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

shift = 0 
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
    
#draw the wall using the Platfrom class 
wall1 = Platform(30,30,30,30,(0,0,0))
    
window = display.set_mode((1000,670))
background = transform.scale(image.load("scifi background.webp"),(1000,670))
clock = time.Clock()


shift = 0 
speed = 0
width = 1200
shift += speed  
local_shift = shift % width
# window.blit(background,(local_shift,0))
# if local_shift != 0: 
#     window.blit(background,(local_shift - width,0))

left_bound = width / 40 
right_bound = width - left_bound
# if screen.rect.x > right_bound or screen.rect.x < left_bound: 
#     shift -= screen.rect.x 
# for s in all_sprites: 
#     screen.rect.x -= (maincharacter).x.speed 
#     display.update()
#     clock.tick(60)


flag = True
while flag:
    for e in event.get():
            if e.type == QUIT:
                flag = False
            if e.type == KEYDOWN: 
                if e.key == K_d:
                    speed = 5 
                elif e.key == K_a: 
                    speed = -5 
            elif e.type == KEYUP: 
                if e.key == K_d:
                    speed = 0 
                elif e.key == K_a: 
                    speed = 0
    window.blit(background,(0,0))
    display.update()
