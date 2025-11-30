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

platform_left = GameSprite("player-left.png", 50, 350)
platform_right = GameSprite("player-right.png", 800, 350)
ball = GameSprite("pball.png", 400, 350, width=100, height=100)

speed_x = 3
speed_y = 3

font.init()
text = font.Font(None, 60)
left_win = text.render('Left wins', True, (0, 100, 0))
right_win = text.render('Right wins', True, (0, 100, 0))

finish = False
clock = time.Clock()
game = True

while game:
    window.fill((200, 255, 200))
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        pressed = key.get_pressed()
        if pressed[K_UP] and platform_right.rect.y >= 0:
            platform_right.rect.y -= 10
        if pressed[K_DOWN] and platform_right.rect.y <= 800 - platform_right.rect.height:
            platform_right.rect.y += 10
        if pressed[K_w] and platform_left.rect.y >= 0:
            platform_left.rect.y -= 10
        if pressed[K_s] and platform_left.rect.y <= 800 - platform_left.rect.height:
            platform_left.rect.y += 10
        if ball.rect.y >= 800 - ball.rect.height or ball.rect.y <= 0:
            speed_y *= -1
        if sprite.collide_rect(ball, platform_left):
            speed_x *= -1
        if sprite.collide_rect(ball, platform_right):
            speed_x *= -1
        ball.rect.y += speed_y
        ball.rect.x += speed_x
    platform_left.draw()
    platform_right.draw()
    ball.draw()
    if ball.rect.x <= 0 - ball.rect.width:
            window.blit(right_win, (350, 325))
    if ball.rect.x >= 900:
        window.blit(left_win, (350, 325))
    display.update()
    clock.tick(60)