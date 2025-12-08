import pygame
from constants import *
from logger import log_state, log_event
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot
import sys

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    dt = 0
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_running = True
    screen_mid_x = SCREEN_WIDTH/2
    screen_mid_y = SCREEN_HEIGHT/2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    player = Player(screen_mid_x, screen_mid_y)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroidfield = AsteroidField()
    while game_running:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
        screen.fill("black")
        updatable.update(dt)
        for asters in asteroids:
            if player.collides_with(asters):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for asters in asteroids:
            for bullet in shots:
                if bullet.collides_with(asters):
                    log_event("asteroid_shot")
                    asters.kill()
                    bullet.kill()
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        dt =(clock.tick(60)/1000)



if __name__ == "__main__":
    main()


