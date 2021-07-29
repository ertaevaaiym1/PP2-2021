import pygame, random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WIDTH = 600
HEIGHT = 600
score = 0
FPS = 60

class Lion(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = WIDTH/2 , HEIGHT/2

    def update(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_DOWN]:
            self.rect.y += 10
        if pressed[pygame.K_UP]:
            self.rect.y -= 10
        if pressed[pygame.K_LEFT]:
            self.rect.x -= 10
        if pressed[pygame.K_RIGHT]:
            self.rect.x += 10

class Green_s(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = random.randint(1,WIDTH), random.randint(1,HEIGHT)
        
    def update(self):
        self.rect.x += random.randint(-2,2)
        if self.rect.x > HEIGHT:
            self.rect.center = random.randint(1,600), random.randint(1,40)
        
class Red_s(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = random.randint(1,WIDTH), random.randint(1,HEIGHT)
        
    def update(self):
        self.rect.y += 2
        if self.rect.y > HEIGHT:
            self.rect.center = random.randint(1,600), random.randint(1,40)
        

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GAME: HUNGRY LION")
clock = pygame.time.Clock()
red = pygame.sprite.Group()
green = pygame.sprite.Group()
blue = pygame.sprite.Group()

for x in range(20):
    x = Red_s()
    red.add(x)

for f in range(40):
    f = Green_s()
    green.add(f)

lion = Lion()
blue.add(lion)

while True:

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            quit()
        
    red.update()
    blue.update()
    green.update()
    
    screen.fill(WHITE)

    red.draw(screen)
    blue.draw(screen)
    green.draw(screen)
    
    for f in green:
        if pygame.sprite.spritecollide(lion, green, True):
            score += 1
        
    for x in red:
        if pygame.sprite.spritecollide(lion, red, True):
            score -= 1
            red.add(Red_s())
            
    font = pygame.font.SysFont('Elephant', 50)
    txt = font.render(f'SCORE : {score}', 1, (0, 0, 0))
    screen.blit(txt, (20, 20))

    pygame.display.flip()

pygame.quit()
