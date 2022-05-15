#Создай собственный Шутер!===================================================================================================
from pygame import *
from random import randint
#music===================================================================================================
mixer.init()
mixer.music.load("подлая еврейская музыка.mp3")
mixer.music.play()
#не music
font.init()
font = font.SysFont("Arial", 70)
win = font.render("YOU WINa", True, (232,204,4))
looser = font.render("LOSSER", True, (232,204,4))
#фон===================================================================================================
window1 = 700
window2 = 500
window = display.set_mode((window1, window2))
display.set_caption("shuter apparat")
apparat = transform.scale(image.load("rosha.jpg"),(window1, window2))

huskars = sprite.Group()

#класс гаме спрайте===================================================================================================
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (60, 60))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#класс игрока===================================================================================================
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_d]:
            self.rect.x += 20
        if keys_pressed[K_a]:
            self.rect.x -= 20
    def fire(self):
        bullet = Bullet("ammo.png", self.rect.centerx,self.rect.top, 6)
        bullets.add(bullet)
#класс вражины===================================================================================================
class Enemy(GameSprite):
    def update(self):   
        self.rect.y += self.speed
        if self.rect.y >= window2:
            self.rect.y = 0
            self.rect.x = randint(0,650)
            global loos
            loos += 1
#класс снарядов===================================================================================================
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:          
            self.kill()

bullets = sprite.Group()

#спрайтики===================================================================================================
appartik = Player("apparat.png", 20, 400, 15)
huskar = Enemy("huskar.png", randint(0,650), 0, 1)
huskars.add(huskar)
huskar = Enemy("huskar.png", randint(0,650), 0, 2)
huskars.add(huskar)
huskar = Enemy("huskar.png", randint(0,650), 0, 3)
huskars.add(huskar)
huskar = Enemy("huskar.png", randint(0,650), 0, 4)
huskars.add(huskar)
#щётчик очков
score = 0
loos = 0
#цикл===================================================================================================
clock = time.Clock()
FPS = 60

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                #fire_sound.play()
                appartik.fire()
            #game = False
    if finish != True:
        window.blit(apparat , (0, 0))
        sprites_list = sprite.spritecollide(appartik, huskars, False)
        if (len(sprites_list)) > 0:
            finish = True
            window.blit(looser , (350, 200))
        sprites_list = sprite.groupcollide(huskars, bullets, True, True)
        for i in sprites_list:
            huskar = Enemy("huskar.png", randint(0,650), 0, 4)
            huskars.add(huskar)
            score = score + 1
        if score >= 50:
            finish = True
            window.blit(win , (350, 200))
        if loos > 3:
            finish = True
            window.blit(looser , (350, 200))

        kill = font.render("kill:"+str(score), True, (232,204,4))
        miss = font.render("miss:"+str(loos), True, (232,204,4))
        window.blit(kill, (50, 100))
        window.blit(miss, (50, 150))
        appartik.update()
        appartik.reset()
        huskars.update()
        huskars.draw(window)
        bullets.update()
        bullets.draw(window)
        display.update()

    clock.tick(FPS)



#ZXC
    #ZXC
#ZXC    #ZXC
    #ZXC    #ZXC
#ZXC    #ZXC    #ZXC
    #ZXC    #ZXC    #ZXC
#ZXC    #ZXC    #ZXC    #ZXC
    #ZXC    #ZXC    #ZXC    #ZXC
#ZXC    #ZXC    #ZXC    #ZXC    #ZXC
    #ZXC    #ZXC    #ZXC    #ZXC    #ZXC
#ZXC    #ZXC    #ZXC    #ZXC    #ZXC    #ZXC
    #ZXC    #ZXC    #ZXC    #ZXC    #ZXC    #ZXC
#ZXC    #ZXC    #ZXC    #ZXC    #ZXC    #ZXC
    #ZXC    #ZXC    #ZXC    #ZXC    #ZXC
#ZXC    #ZXC    #ZXC    #ZXC    #ZXC
    #ZXC    #ZXC    #ZXC    #ZXC
#ZXC    #ZXC    #ZXC    #ZXC
    #ZXC    #ZXC    #ZXC
#ZXC    #ZXC    #ZXC
    #ZXC    #ZXC
#ZXC    #ZXC
    #ZXC
#ZXC
#wAvE===================================================================================================