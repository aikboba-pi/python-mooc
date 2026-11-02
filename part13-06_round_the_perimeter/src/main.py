import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

max_x = 640 - robot.get_width()
max_y = 480 - robot.get_height()

x = 0
y = 0
speed = 2

direction = "right"

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    match direction:
        case "right":
            x += speed
            if x >= max_x:
                x = max_x
                direction = "down"

        case "down":
            y += speed
            if y >= max_y:
                y = max_y
                direction = "left"

        case "left":
            x -= speed
            if x <= 0:
                x = 0
                direction = "up"

        case "up":
            y -= speed
            if y <= 0:
                y = 0
                direction = "right"

    clock.tick(60)