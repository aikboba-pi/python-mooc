import pygame
from random import randint

pygame.init()
robot = pygame.image.load("robot.png")

window_width = 640
window_height = 480
robot_width = robot.get_width()
robot_height = robot.get_height()

window = pygame.display.set_mode((window_width, window_height))
window.fill((0,0,0))

for i in range(1000):
    window.blit(robot, (randint(0, window_width - robot_width), randint(0, window_height - robot_height)))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()