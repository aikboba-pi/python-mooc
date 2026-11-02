import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

ball = pygame.image.load("ball.png")
ball_width = ball.get_width()
ball_height = ball.get_height()

max_x = 640 - ball_width
max_y = 480 - ball_height

x = 0
y = 0

x_speed = 2
y_speed = 2

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    x += x_speed
    y += y_speed

    if x_speed > 0 and x >= max_x:
        x = max_x
        x_speed = -x_speed
    elif x_speed < 0 and x <= 0:
        x = 0
        x_speed = -x_speed

    if y_speed > 0 and y >= max_y:
        y = max_y
        y_speed = -y_speed
    elif y_speed < 0 and y <= 0:
        y = 0
        y_speed = -y_speed

    window.fill((0, 0, 0))
    window.blit(ball, (x, y))
    pygame.display.flip()

    clock.tick(60)