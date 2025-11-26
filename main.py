from pygame import *

window = display.set_mode((900, 800))

class GameSprite(sprite.Sprite):
    def __init__(self, filename, x, y, width=30, height=200):
        super().__init__()
        self.image = transform.scale(image.load(filename), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

clock = time.Clock()
game = True

while game:
    window.fill((200, 255, 200))
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(60)