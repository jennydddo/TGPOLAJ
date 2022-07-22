from pygame import * 

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

window = display.set_mode((1000,670))
background = transform.scale(image.load("scifi background.webp"),(1000,670))
clock = time.Clock()

flag = True
while flag:
    for e in event.get():
            if e.type == QUIT:
                flag = False
    window.blit(background,(0,0))

    display.update()
    clock.tick(60)