import sys
import math
import datetime
import pygame

pygame.init()

WIDTH, HEIGHT = 640, 480

CENTER = (WIDTH // 2, HEIGHT // 2)
CLOCK_RADIUS = 200
SECOND_HAND_LENGTH = 180
MINUTE_HAND_LENGTH = SECOND_HAND_LENGTH
HOUR_HAND_LENGTH = 130
CENTER_CIRCLE_RADIUS = 10

BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 100, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


def calculate_hand_endpoint(center: tuple[int, int], angle_degrees: float, length: int) -> tuple[int, int]:
    """Calculates the end (x, y) coordinates for a clock hand based on its angle."""
    rad = math.radians(angle_degrees - 90)
    end_x = center[0] + length * math.cos(rad)
    end_y = center[1] + length * math.sin(rad)
    return (round(end_x), round(end_y))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = datetime.datetime.now()
    hours = now.hour
    minutes = now.minute
    seconds = now.second
    microseconds = now.microsecond

    pygame.display.set_caption(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

    sec_angle = seconds * 6
    min_angle = (minutes + seconds / 60) * 6
    hour_angle = ((hours % 12) + minutes / 60 + seconds / 3600) * 30

    sec_end = calculate_hand_endpoint(CENTER, sec_angle, SECOND_HAND_LENGTH)
    min_end = calculate_hand_endpoint(CENTER, min_angle, MINUTE_HAND_LENGTH)
    hour_end = calculate_hand_endpoint(CENTER, hour_angle, HOUR_HAND_LENGTH)

    screen.fill(BLACK)

    pygame.draw.circle(screen, RED, CENTER, CLOCK_RADIUS, width=4)
    pygame.draw.circle(screen, RED, CENTER, CENTER_CIRCLE_RADIUS)
    pygame.draw.line(screen, BLUE, CENTER, hour_end, width=3)
    pygame.draw.line(screen, BLUE, CENTER, min_end, width=2)
    pygame.draw.line(screen, BLUE, CENTER, sec_end, width=1)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()