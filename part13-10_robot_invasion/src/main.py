import random
import pygame
from typing import Literal

TRobotType = tuple[float, float, Literal["falling", "walking"], Literal[1, -1]]

pygame.init()
window_width = 640
window_height = 480
window = pygame.display.set_mode((window_width, window_height))

robot = pygame.image.load("robot.png")
robot_width = robot.get_width()
robot_height = robot.get_height()

ground_y = window_height - robot_height

robots: list[TRobotType] = []

fall_speed = 1.0
walk_speed = 1.0

spawn_timer = 0
spawn_interval = 40  # Frames between new spawns

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    spawn_timer += 1

    if spawn_timer >= spawn_interval:
        spawn_timer = 0
        spawn_x = random.randint(0, window_width - robot_width)
        spawn_y = -robot_height

        if spawn_x + robot_width / 2 < window_width / 2:
            direction = -1
        else:
            direction = 1

        robots.append((spawn_x, spawn_y, "falling", direction))

    remaining_robots: list[TRobotType] = []
    
    for r in robots:
        x, y, state, direction = r

        if state == "falling":
            y += fall_speed
            if y >= ground_y:
                y = ground_y
                state = "walking"
        elif state == "walking":
            x += direction * walk_speed

        if -robot_width <= x <= window_width:
            remaining_robots.append((x, y, state, direction))

    robots = remaining_robots

    # Render
    window.fill((0, 0, 0))
    for r in robots:
        window.blit(robot, (r[0], r[1]))
    pygame.display.flip()

    clock.tick(60)