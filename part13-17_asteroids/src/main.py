import sys
import pygame
from random import randint
import uuid

type T_ROCKS = dict[str, tuple[int, int]]

pygame.init()

WIDTH, HEIGHT = 640, 480
ROCK_SPEED = 1
ADD_ROCK_EVENT = pygame.event.custom_type()

window = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont("Arial", 24)

robot = pygame.image.load("robot.png")
rock = pygame.image.load("rock.png")

robot_width = robot.get_width()
robot_height = robot.get_height()
rock_width = rock.get_width()
rock_height = rock.get_height()

x = (WIDTH // 2) - (robot_width // 2)
y = HEIGHT - robot_height

to_right = False
to_left = False

clock = pygame.time.Clock()

def is_rects_collision(rect1: tuple[int, int, int, int], rect2: tuple[int, int, int, int]) -> bool:
    x1, y1, w1, h1 = rect1
    x2, y2, w2, h2 = rect2
    
    return (
        x1 < x2 + w2 and
        x1 + w1 > x2 and
        y1 < y2 + h2 and
        y1 + h1 > y2
    )

def update_rocks() -> T_ROCKS:
    new_rocks: T_ROCKS = {}

    for rock_id in game.rocks:
        if (rock_id in game.rocks):
            if game.rocks[rock_id][1] + ROCK_SPEED > HEIGHT - rock_height:
                game.stop_game()
                continue
            elif is_rects_collision((game.rocks[rock_id][0], game.rocks[rock_id][1], rock_width, rock_height), (x, y, robot_width, robot_height)):
                game.score += 1
                continue
            else:
                new_rocks[rock_id] = game.rocks[rock_id]

    return new_rocks

class GameSet:
    def __init__(self):
        self.is_playing = False
        self.score = 0
        self.rocks: T_ROCKS = {}

    def build_rock(self) -> tuple[int, int]:
        return (randint(0, WIDTH - rock_width), -rock_height)

    def add_rock(self):
        self.rocks[uuid.uuid4().hex] = self.build_rock()

    def schedule_next_rock(self):
        if self.is_playing:
            random_interval = randint(1000, 5000)
            pygame.time.set_timer(ADD_ROCK_EVENT, random_interval)
        else:
            pygame.time.set_timer(ADD_ROCK_EVENT, 0)

    def stop_game(self):
        self.is_playing = False
        self.score = 0
        self.rocks = {}
        pygame.time.set_timer(ADD_ROCK_EVENT, 0)

    def start_game(self):
        self.is_playing = True
        self.add_rock()
        self.schedule_next_rock()

game = GameSet()
game.start_game()

running = True
while running:
    for event in pygame.event.get():
        if event.type == ADD_ROCK_EVENT:
            if game.is_playing:
                game.add_rock()
                game.schedule_next_rock()

        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = event.type == pygame.KEYDOWN
            if event.key == pygame.K_RIGHT:
                to_right = event.type == pygame.KEYDOWN

        if event.type == pygame.QUIT:
            running = False

    if to_right:
        if x + 2 > WIDTH - robot_width:
            to_right = False
            continue
        x += 2
    if to_left:
        if x - 2 < 0:
            to_left = False
            continue
        x -= 2

    window.fill((0, 0, 0))

    text_surface = font.render(f"Pisteet: {game.score}", True, (255, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect.top = 20
    text_rect.right = WIDTH - 20

    window.blit(text_surface, text_rect)

    for rock_id in game.rocks:
        window.blit(rock, (game.rocks[rock_id][0], game.rocks[rock_id][1]))
        game.rocks[rock_id] = (game.rocks[rock_id][0], game.rocks[rock_id][1] + ROCK_SPEED)

    window.blit(robot, (x, y))
    pygame.display.flip()

    game.rocks = update_rocks()

    clock.tick(60)

pygame.quit()
sys.exit()