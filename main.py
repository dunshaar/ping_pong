from pygame import *

window = display.set_mode((900, 800))

clock = time.Clock()

game = True

while game:
    window.fill((200, 255, 200))
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(60)