import pygame

pygame.init()
robot = pygame.image.load("robot.png")

window_width = 640
window_height = 480
robot_width = robot.get_width()
robot_height = robot.get_height()

window = pygame.display.set_mode((window_width, window_height))
window.fill((0,0,0))

for i in range(10):
    for k in range(10):
        window.blit(robot, ((robot_width * (k + 1) - (k * 10)) + (i * 10), robot_height + (i * 20)))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
