import pygame

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

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            robot_x = event.pos[0]-robot.get_width()/2
            robot_y = event.pos[1]-robot.get_height()/2

        if event.type == pygame.QUIT:
            exit(0)

    window.fill((0, 0, 0))
    window.blit(robot, (robot_x, robot_y))
    pygame.display.flip()

    clock.tick(60)