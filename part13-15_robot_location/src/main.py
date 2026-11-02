import pygame
from random import randint

pygame.init()
window_width = 640
window_height = 480
window = pygame.display.set_mode((window_width, window_height))

robot = pygame.image.load("robot.png")
robot_width = robot.get_width()
robot_height = robot.get_height()

robot_x = (window_width // 2) - (robot_width // 2)
robot_y = (window_height // 2) - (robot_height // 2)

clock = pygame.time.Clock()

def is_robot_area(x: int, y: int) -> bool:
    return robot_x <= x <= robot_x + robot_width and robot_y <= y <= robot_y + robot_height

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and is_robot_area(event.pos[0], event.pos[1]):
            robot_x = randint(0, window_width - robot_width)
            robot_y = randint(0, window_height - robot_height)

        if event.type == pygame.QUIT:
            exit(0)

    window.fill((0, 0, 0))
    window.blit(robot, (robot_x, robot_y))
    pygame.display.flip()

    clock.tick(60)