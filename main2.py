import pygame
import sys
import random
from player import Player
from cloud import Cloud
# from backgroud import Background

class Game:
    def __init__(self):
        # Player setup
        player_sprite = Player((screen_width /2 ,screen_height),screen_width,screen_height,8)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        cloud_sprite = Cloud()
        self.cloud = pygame.sprite.GroupSingle(cloud_sprite)


        # background_sprite = Background(screen_width,screen_height)
        # self.background = pygame.sprite.GroupSingle(background_sprite)

        # obstacle setup
        # obstacle_sprite = obstacle()




    def run(self):
        self.player.update()
        self.player.draw(screen)
        self.cloud.update()
        self.cloud.draw(screen)
        # self.background.draw(screen)
        # self.blocks.draw(screen)
        # update all sprite groups
        # draw all sprite groups


if __name__ == '__main__':
    pygame.init()
    screen_width = 1280
    screen_height = 720
    screen = pygame.display.set_mode((screen_width,screen_height))
    bg = pygame.image.load('graphic/sky.png').convert()
    clock = pygame.time.Clock()

    game = Game()

    while True:

        clock.tick(60)
        screen.blit(bg,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        
        
        game.run ()
        
        pygame.display.flip()


        clock.tick(60)
