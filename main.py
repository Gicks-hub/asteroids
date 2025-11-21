import pygame
from constants import *
from logger import log_state
from player import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    dt = 0
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_running = True
    player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))


    while game_running:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
        screen.fill("black")
        pygame.display.flip()
        dt =(clock.tick(60)/1000)
        player.draw(screen)


if __name__ == "__main__":
    main()

