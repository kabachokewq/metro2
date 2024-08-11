from pygame import *
from random import randint
from time import time as timer




wn = display.set_mode((640*1.5,243*1.5))
clock = time.Clock()
display.set_caption("Шутер")
background = transform.scale(image.load("metro1.png"),(640*1.5,243*1.5))
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self,pl_image,pl_x,pl_y,size_x,size_y,pl_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(pl_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = pl_x
        self.rect.y = pl_y
        self.speed = pl_speed
        self.size_x = size_x
    def reset(self):
        wn.blit(self.image,(self.rect.x,self.rect.y))
        
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 700 - self.size_x:
            self.rect.x += self.speed


class Enemy(GameSprite):
    
    
    def update(self):
        global lose

        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y = -50
            self.rect.x = randint(80,620)
            self.speed = randint(1,5)
            
game = True
finish = False
hero = Player("hero.png", 100,150,132,132,5)
enemy1 = Enemy("enemy1.png", 650,150,132,132,5)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        
    if not finish:
        wn.blit(background,(0,0))
        hero.reset()
        hero.update()
        enemy1.reset()
    
    
    clock.tick(FPS)
    display.update()