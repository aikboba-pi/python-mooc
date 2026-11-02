import pygame

pygame.init()
window_width = 640
window_height = 480
window = pygame.display.set_mode((window_width, window_height))

robot = pygame.image.load("robot.png")
robot_width = robot.get_width()
robot_height = robot.get_height()
window = pygame.display.set_mode((window_width, window_height))

robot = pygame.image.load("robot.png")
x = (window_width // 2) - (robot_width // 2)
y = (window_height // 2) - (robot_height // 2)

to_right = False
to_left = False
to_up = False
to_down = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
            if event.key == pygame.K_UP:
                to_up = True
            if event.key == pygame.K_DOWN:
                to_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_UP:
                to_up = False
            if event.key == pygame.K_DOWN:
                to_down = False

        if event.type == pygame.QUIT:
            exit()

    if to_right:
        if x + 2 > window_width - robot_width:
            to_right = False
            continue
        x += 2
    if to_left:
        if x - 2 < 0:
            to_left = False
            continue
        x -= 2
    if to_up:
        if y - 2 < 0:
            to_up = False
            continue
        y -= 2
    if to_down:
        if y + 2 > window_height - robot_height:
            to_down = False
            continue
        y += 2

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    clock.tick(60)