import pygame
import random
pygame.init()
 
# WHITE = [255, 255, 255]
# GREEN  = [0,255,0]
# SIZE = [400, 400]

class Cloud(pygame.sprite.Sprite):
  
    def check(self):
        snowFall = []
        for i in range(50):
            x = random.randrange(0, 720)
            y = random.randrange(0, 720)
            snowFall.append([x, y])
        
        clock = pygame.time.Clock()
        done = False
        while not done:
        
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    done = True
            
            for i in range(len(snowFall)):
                pygame.image.load('graphic/plane.png').convert_alpha()
        
                snowFall[i][1] += 1
                if snowFall[i][1] > 720:
                    y = random.randrange(-50, -10)
                    snowFall[i][1] = y
                
                    x = random.randrange(0, 720)
                    snowFall[i][0] = x
        
            # pygame.display.flip()
            # clock.tick(20)

    def update(self):
       self.check()        
        