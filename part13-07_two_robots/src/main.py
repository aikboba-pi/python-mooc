import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
robot_width = robot.get_width()
robot_height = robot.get_height()

max_x = 640 - robot_width

x1 = 0
y1 = robot_height
speed1 = 1

x2 = 0
y2 = y1 + robot_height + 20
speed2 = speed1 * 2

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))

    window.blit(robot, (x1, y1))
    window.blit(robot, (x2, y2))
    pygame.display.flip()

    x1 += speed1

    if speed1 > 0 and x1 >= max_x:
        x1 = max_x
        speed1 = -speed1
    elif speed1 < 0 and x1 <= 0:
        x1 = 0
        speed1 = -speed1

    x2 += speed2

    if speed2 > 0 and x2 >= max_x:
        x2 = max_x
        speed2 = -speed2
    elif speed2 < 0 and x2 <= 0:
        x2 = 0
        speed2 = -speed2

    clock.tick(60)