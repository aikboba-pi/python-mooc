import pygame

pygame.init()
window_width = 640
window_height = 480
window = pygame.display.set_mode((window_width, window_height))

robot = pygame.image.load("robot.png")
robot_2 = pygame.image.load("robot.png")
robot_width = robot.get_width()
robot_height = robot.get_height()

x_2 = (window_width // 3) - (robot_width // 2)
y_2 = (window_height // 2) - (robot_height // 2)
x = (window_width // 3) + (window_width // 3) - (robot_width // 2)
y = (window_height // 2) - (robot_height // 2)

to_right = False
to_left = False
to_up = False
to_down = False
to_right_2 = False
to_left_2 = False
to_up_2 = False
to_down_2 = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = event.type == pygame.KEYDOWN
            if event.key == pygame.K_RIGHT:
                to_right = event.type == pygame.KEYDOWN
            if event.key == pygame.K_UP:
                to_up = event.type == pygame.KEYDOWN
            if event.key == pygame.K_DOWN:
                to_down = event.type == pygame.KEYDOWN

            if event.key == pygame.K_a:
                to_left_2 = event.type == pygame.KEYDOWN
            if event.key == pygame.K_d:
                to_right_2 = event.type == pygame.KEYDOWN
            if event.key == pygame.K_w:
                to_up_2 = event.type == pygame.KEYDOWN
            if event.key == pygame.K_s:
                to_down_2 = event.type == pygame.KEYDOWN

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

    if to_right_2:
        if x_2 + 2 > window_width - robot_width:
            to_right_2 = False
            continue
        x_2 += 2
    if to_left_2:
        if x_2 - 2 < 0:
            to_left_2 = False
            continue
        x_2 -= 2
    if to_up_2:
        if y_2 - 2 < 0:
            to_up_2 = False
            continue
        y_2 -= 2
    if to_down_2:
        if y_2 + 2 > window_height - robot_height:
            to_down_2 = False
            continue
        y_2 += 2

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    window.blit(robot_2, (x_2, y_2))
    pygame.display.flip()

    clock.tick(60)