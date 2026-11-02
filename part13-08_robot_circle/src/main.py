import math
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
robot_width = robot.get_width()
robot_height = robot.get_height()

center_x = 640 // 2
center_y = 480 // 2

radius = 130

robot_count = 10
angle = 0.0
speed = 0.01

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))

    for i in range(robot_count):
        robot_angle = angle + (2 * math.pi / robot_count) * i

        x = center_x + radius * math.cos(robot_angle) - robot_width / 2
        y = center_y + radius * math.sin(robot_angle) - robot_height / 2

        window.blit(robot, (x, y))

    pygame.display.flip()

    angle += speed

    clock.tick(60)