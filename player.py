import pygame
import random
class Player(pygame.sprite.Sprite):
   def __init__(self,pos,constraintx,constrainty,speed):
      super().__init__()
      self.image = pygame.image.load('graphic/plane.png').convert_alpha()
      self.rect = self.image.get_rect(midbottom = pos)
      self.speed = speed
      self.max_x_constraint = constraintx
      self.max_y_constraint = constrainty

   def get_input(self):
      keys = pygame.key.get_pressed()

      if keys[pygame.K_d]:
         self.rect.x += self.speed
      elif keys[pygame.K_a]:
         self.rect.x -= self.speed
      elif keys[pygame.K_w]:
         self.rect.y -= self.speed
      elif keys[pygame.K_s]:
         self.rect.y += self.speed

      

   def constraint(self):
      if self.rect.left <= 0:
          self.rect.left = 0
      if self.rect.right >= self.max_x_constraint:
          self.rect.right = self.max_x_constraint
      if self.rect.top <= 450:
          self.rect.top = 450
      if self.rect.bottom >= self.max_y_constraint:
          self.rect.bottom = self.max_y_constraint

   
   def cloud_movement(cloud_rect_list,screen,):
      carolyn = pygame.image.load('graphic/cloud.png').convert_alpha()
      carolyn = pygame.transform.scale(carolyn, (50, 50))
      carolyn_rect = carolyn.get_rect(topright=(random.randint(50, 400), 0))
      
      if cloud_rect_list:
         for cloud_rect in carolyn_rect_list:
               cloud_rect.y += 4
               if cloud_rect.x <= 0:
                  cloud_rect.x = 0
               if cloud_rect.x >= 400:
                  cloud_rect.x = 400
               if cloud_rect.y >= 480:
                  cloud_rect.y = 600
               screen.blit(carolyn, cloud_rect)
         carolyn_rect_list = [carolyn for carolyn in carolyn_rect_list if carolyn.y < 600]
         return carolyn_rect_list
      else:
         return []


   def update(self):
       self.get_input()
       self.constraint()
         
    
