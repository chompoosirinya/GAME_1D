import pygame
from sys import exit
import random
import pickle
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption(("Catch-A-Cloud"))
clock = pygame.time.Clock()
game_font = pygame.font.SysFont("arialblack", 40)
game_active = True
score = 0
speed = 8
try:
  with open('HighScore', 'rb') as file:
    high_score = pickle.load(file)
except:
  high_score = 0
  
#SET UP OF IMAGES
#plane
plane_catch = pygame.image.load('graphic/plane.png').convert_alpha()
plane_catch = pygame.transform.scale(plane_catch, (90, 100))
plane_catch_rect = plane_catch.get_rect(midbottom=(640, 720))
plane_catch_how_to = pygame.transform.scale(plane_catch, (60,60))
plane_how_to_rect = plane_catch.get_rect(topright = (370,225))
#cloud
cloud = pygame.image.load('graphic/cloud.png').convert_alpha()
cloud = pygame.transform.scale(cloud, (80, 80))
cloud_rect = cloud.get_rect(topright=(random.randint(100, 1180), 0))
cloud_how_to = pygame.transform.scale(cloud,(50,40))
cloud_how_to_rect = cloud_how_to.get_rect(topright = (178,279))
#blackcloud
blackcloud = pygame.image.load('graphic/blackcloud.png').convert_alpha()
blackcloud = pygame.transform.scale(blackcloud, (80, 80))  
blackcloud_rect = blackcloud.get_rect(topright=(random.randint(100, 1280), 0))
blackcloud_how_to = pygame.transform.scale(blackcloud,(40,40))
blackcloud_how_to_rect = blackcloud_how_to.get_rect(topright = (178,279))
#lightning
lightning = pygame.image.load('graphic/lightning.png').convert_alpha()
lightning = pygame.transform.scale(lightning, (80, 80))
lightning_rect = lightning.get_rect(topright=(random.randint(50, 400), 0))
lighting_how_to = lightning.get_rect(midbottom = (260, 380))
#rainbow
rainbow = pygame.image.load('graphic/rainbow.png').convert_alpha()
rainbow = pygame.transform.scale(rainbow, (80, 50))
rainbow_rect = rainbow.get_rect(topright=(random.randint(50, 400), 0))
rainbow_how_to = rainbow.get_rect(topright = (182,375))

def background():
  background = pygame.image.load('graphic/bg.png').convert_alpha()
  background = pygame.transform.scale(background, (1280, 720))
  screen.blit(background, (0, 0))
def display_score(score):
  high_score_font = pygame.font.SysFont('arialblack', 30)
  score_surf = high_score_font.render(f"Score: {score}", False, 'deeppink')
  score_surf_rect = score_surf.get_rect(midbottom = (200,90))
  high_score_font = pygame.font.SysFont('arialblack', 30)
  high_score_surf = high_score_font.render(f"High Score: {high_score}", False, 'deeppink')
  high_score_surf_rect = high_score_surf.get_rect(midbottom = (200,50))
  screen.blit(high_score_surf,high_score_surf_rect)
  screen.blit(score_surf, score_surf_rect)  
  
def plane_movement():
  keys = pygame.key.get_pressed()

  if keys[pygame.K_d]:
    plane_catch_rect.x += speed
  elif keys[pygame.K_a]:
         plane_catch_rect.x -= speed
  elif keys[pygame.K_w]:
         plane_catch_rect.y -= speed
  elif keys[pygame.K_s]:
         plane_catch_rect.y += speed
  if plane_catch_rect.left <= 0:
          plane_catch_rect.left = 0
  if plane_catch_rect.right >= 1280:
          plane_catch_rect.right = 1280
  if plane_catch_rect.top <= 400:
          plane_catch_rect.top = 400
  if plane_catch_rect.bottom >= 720:
          plane_catch_rect.bottom = 720
  return screen.blit(plane_catch, plane_catch_rect)

def cloud_movement(cloud_rect_list):
    if cloud_rect_list:
        for cloud_rect in cloud_rect_list:
            cloud_rect.y += 4
            if cloud_rect.x <= 100:
                cloud_rect.x = 100
            if cloud_rect.x >= 1180:
                cloud_rect.x = 1180
            if cloud_rect.y >= 720:
                cloud_rect.y = 720
            screen.blit(cloud, cloud_rect)
        cloud_rect_list = [cloud for cloud in cloud_rect_list if cloud.y < 720]
        return cloud_rect_list
    else:
        return []

def blackcloud_movement(blackcloud_rect_list):
    if blackcloud_rect_list:
        for blackcloud_rect in blackcloud_rect_list:
            blackcloud_rect.y += 4
            if blackcloud_rect.x <= 100:
                blackcloud_rect.x = 100
            if blackcloud_rect.x >= 1180:
                blackcloud_rect.x = 1180
            if blackcloud_rect.y >= 720:
                blackcloud_rect.y = 720
            screen.blit(blackcloud, blackcloud_rect)
        blackcloud_rect_list = [blackcloud for blackcloud in blackcloud_rect_list if blackcloud.y < 720]
        return blackcloud_rect_list
    else:
        return []
def lightning_movement(lightning_rect_list):
    if lightning_rect_list:
        for lightning_rect in lightning_rect_list:
            lightning_rect.y += 5
            if lightning_rect.x <= 100:
                lightning_rect.x = 100
            if lightning_rect.x >= 1180:
                lightning_rect.x = 1180
            if lightning_rect.y >= 720:
                lightning_rect.y = 720
            screen.blit(lightning, lightning_rect)
        lightning_rect_list = [lightning for lightning in lightning_rect_list if lightning.y < 720]
        return lightning_rect_list
    else:
        return []
def rainbow_movement(rainbow_rect_list):
    if rainbow_rect_list:
        for rainbow_rect in rainbow_rect_list:
            rainbow_rect.y += 5
            if rainbow_rect.x <= 100:
                rainbow_rect.x = 100
            if rainbow_rect.x >= 1180:
                rainbow_rect.x = 1180
            if rainbow_rect.y >= 720:
                rainbow_rect.y = 720
            screen.blit(rainbow, rainbow_rect)
        rainbow_rect_list = [rainbow for rainbow in rainbow_rect_list if rainbow.y < 720]
        return rainbow_rect_list
    else:
        return []
def play_again_display():
  play_again = pygame.font.SysFont('arialblack', 40)
  play_again_surf = play_again.render("Press 'Enter' to play again!", False, 'deeppink')
  play_again_rect = play_again_surf.get_rect(center = (200,360))
  pygame.draw.ellipse(screen, 'plum2', play_again_rect)
  screen.blit(play_again_surf, play_again_rect)
def final_score_display(final_score, high_score):
  if final_score > high_score:
    new_high_score_font = pygame.font.SysFont('arialblack', 60)
    new_high_score = new_high_score_font.render(f"New High Score: {final_score}", False, 'deeppink')
    new_high_score_rect = new_high_score.get_rect(center = (200,300))
    pygame.draw.ellipse(screen, 'plum2', new_high_score_rect)
    screen.blit(new_high_score, new_high_score_rect)
    high_score = final_score
    with open('HighScore', 'wb') as file:
        pickle.dump(high_score, file)
  else:
    last_font = pygame.font.SysFont('arialblack', 60)
    score_surf = last_font.render(f"Final Score: {score}", False, 'deeppink')
    score_surf_rect = score_surf.get_rect(center = (200,300))
    pygame.draw.ellipse(screen, 'plum2', score_surf_rect)
    screen.blit(score_surf, score_surf_rect)
def end_of_game_display():
  kim_game_over = pygame.image.load('graphic/bg.png').convert_alpha()
  kim_game_over = pygame.transform.scale(kim_game_over, (400, 600))
  screen.blit(kim_game_over, (0,0))

def welcome_surf():
  welcome_font = pygame.font.SysFont('arialblack', 56)
  welcome_surf = welcome_font.render("Catch-A-Crunk", False, 'deeppink')
  welcome_surf_rect = welcome_surf.get_rect(midbottom = (200,170))
  how_to_font = pygame.font.SysFont('arialblack', 30)
  how_to = how_to_font.render("How To Play", False, 'deeppink')
  how_to_rect = how_to.get_rect(midbottom = (400, 460))
  screen.blit(how_to, how_to_rect)
  screen.blit(welcome_surf, welcome_surf_rect)
# def how_to_move():
#   how_to_play_font = pygame.font.SysFont('arialblack', 28)
#   how_to_play = how_to_play_font.render("Use the arrow keys to move", False, 'deeppink')
#   how_to_play_rect = how_to_play.get_rect(midbottom = (182,277))
#   screen.blit(plane_catch_how_to, plane_how_to_rect)
#   screen.blit(how_to_play, how_to_play_rect)
# def catching_cloud():
#   cloud_catch_font = pygame.font.SysFont('arialblack', 28)
#   cloud_catch = cloud_catch_font.render("Catch            to earn points!", False, 'deeppink')
#   cloud_catch_rect = cloud_catch.get_rect(midbottom = (200,325))
#   screen.blit(cloud_catch, cloud_catch_rect)
#   screen.blit(cloud, cloud_how_to_rect)
# def catching_blackcloud():
  # blackcloud_catch_font = pygame.font.SysFont('arialblack', 28)
  # blackcloud_catch = blackcloud_catch_font.render("Catch            to earn points!", False, 'deeppink')
  # blackcloud_catch_rect = blackcloud_catch.get_rect(midbottom = (200,325))
  # screen.blit(blackcloud_catch, blackcloud_catch_rect)
  # screen.blit(blackcloud, blackcloud_how_to_rect)
 
# def watch_out():
#   watch_out_font = pygame.font.SysFont('arialblack', 28)
#   watch_out_surf = watch_out_font.render("Watch out for", False, 'deeppink')
#   watch_out_surf_rect = watch_out_surf.get_rect(midbottom = (180,373))
#   screen.blit(watch_out_surf , watch_out_surf_rect)
#   screen.blit(lightning, lighting_how_to)

  
# def extra_points():
#   bodhi_font = pygame.font.SysFont('arialblack', 28)
#   bodhi_words = bodhi_font.render("Catch              for extra points!", False, 'deeppink')
#   bodhi_words_rect = rainbow.get_rect(midbottom = (97,435))
#   screen.blit(bodhi_words, bodhi_words_rect)
#   screen.blit(rainbow, rainbow_how_to)
def title_screen():
  welcome_surf()
  # how_to_move()
  # catching_cloud()
  # watch_out()
  # extra_points()



#Cloud Timer

def increase_difficulty(score,cloud_rect_list,blackcloud_rect_list, lightning_rect_list, rainbow_rect_list):
  if score >= 25:
    if cloud_rect_list:
      for cloud_rect in cloud_rect_list:
        cloud_rect.y += 2
    if blackcloud_rect_list:
      for blackcloud_rect in blackcloud_rect_list:
        blackcloud_rect.y += 2
    if lightning_rect_list:
      for lightning_rect in lightning_rect_list:
        lightning_rect.y += 2
    if rainbow_rect_list:
      for rainbow_rect in rainbow_rect_list:
        rainbow_rect.y += 2
  if score >= 50:
    if cloud_rect_list:
      for cloud_rect in cloud_rect_list:
        cloud_rect.y += 2
    if blackcloud_rect_list:
      for blackcloud_rect in blackcloud_rect_list:
        blackcloud_rect.y += 2
    if lightning_rect_list:
      for lightning_rect in lightning_rect_list:
        lightning_rect.y += 2
    if rainbow_rect_list:
      for rainbow_rect in rainbow_rect_list:
        rainbow_rect.y += 2
  if score >= 75:
    if cloud_rect_list:
      for cloud_rect in cloud_rect_list:
        cloud_rect.y += 2
    if blackcloud_rect_list:
      for blackcloud_rect in blackcloud_rect_list:
        blackcloud_rect.y += 2
    if lightning_rect_list:
      for lightning_rect in lightning_rect_list:
        lightning_rect.y += 2
    if rainbow_rect_list:
      for rainbow_rect in rainbow_rect_list:
        rainbow_rect.y += 2
  if score >= 100:
    if cloud_rect_list:
      for cloud_rect in cloud_rect_list:
        cloud_rect.y += 2
    if blackcloud_rect_list:
      for blackcloud_rect in blackcloud_rect_list:
        blackcloud_rect.y += 2
    if lightning_rect_list:
      for lightning_rect in lightning_rect_list:
        lightning_rect.y += 2
    if rainbow_rect_list:
      for rainbow_rect in rainbow_rect_list:
          rainbow_rect.y += 2



#cloud Timer
cloud_rect_list = []
cloud_timer = pygame.USEREVENT + 5
pygame.time.set_timer(cloud_timer, 1500)
#blackcloud Timer
blackcloud_rect_list = []
blackcloud_timer = pygame.USEREVENT + 1
pygame.time.set_timer(blackcloud_timer, 1750)
#lightning Timer
lightning_rect_list = []
lightning_timer = pygame.USEREVENT + 2
pygame.time.set_timer(lightning_timer, 2000)
#rainbow Timer
rainbow_rect_list = []
rainbow_timer = pygame.USEREVENT + 3
pygame.time.set_timer(rainbow_timer, 15000)
#How To Play Timer
how_to_play = 0
how_to_play_timer = pygame.USEREVENT + 4
pygame.time.set_timer(how_to_play_timer, 1000)
count_down = 5



SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("graphic/sky.png").convert_alpha()

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.SysFont('arialblack', size)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()          
        if game_active == False:
          if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            game_active = True
            rainbow_rect_list = []
            lightning_rect_list = []
            cloud_rect_list = []
            blackcloud_rect_list = []
            how_to_play = 0
            score = 0
            count_down = 5
            try:
              with open('HighScore', 'rb') as file:
                high_score = pickle.load(file)
            except:
                high_score = 0
        if event.type == how_to_play_timer:
          how_to_play += 1
          count_down -= 1
        #Falling Object Timers and Lists Action
        if game_active and how_to_play_timer >= 5:
          if event.type == cloud_timer and count_down <=0:
              cloud_rect_list.append(cloud.get_rect(midright=(random.randint(50, 1250), 0)))
          if event.type == blackcloud_timer and count_down <=0:
              blackcloud_rect_list.append(blackcloud.get_rect(midright=(random.randint(50, 1250), 0)))
          if event.type == lightning_timer and count_down <= -2:
              lightning_rect_list.append(lightning.get_rect(topright=(random.randint(50, 1250), 0)))
          if event.type == rainbow_timer and count_down <=0:
              rainbow_rect_list.append(rainbow.get_rect(topright=(random.randint(50, 1250), 0)))
    if game_active:
      if how_to_play < 5:
        background()
        title_screen()
      else:
        background()
        display_score(score)  
        #MOVEMENT
        cloud_movement(cloud_rect_list)
        blackcloud_movement(blackcloud_rect_list)
        rainbow_movement(rainbow_rect_list)
        lightning_movement(lightning_rect_list)
        plane_movement()
        increase_difficulty(score,cloud_rect_list,blackcloud_rect_list, lightning_rect_list, rainbow_rect_list)     
        #ADDING POINTS
        if rainbow_rect_list:
          for rainbow_rect in rainbow_rect_list:
            if plane_catch_rect.colliderect(rainbow_rect):
              score += 10
              rainbow_rect_list = []
              display_score(score)
        if cloud_rect_list:
          for cloud_rect in cloud_rect_list:
            if plane_catch_rect.colliderect(cloud_rect):
              score += 1
              cloud_rect.y = 720
              display_score(score)
        if blackcloud_rect_list:
          for blackcloud_rect in blackcloud_rect_list:
            if plane_catch_rect.colliderect(blackcloud_rect):
              score -= 1
              blackcloud_rect.y = 720
              display_score(score)
        #END OF GAME:
        if lightning_rect_list:
          for lightning_rect in lightning_rect_list:
            if plane_catch_rect.colliderect(lightning_rect):
              game_active = False
              final_score = score
    else:
      end_of_game_display()
      play_again_display()
      final_score_display(final_score, high_score) 
    pygame.display.update()
    clock.tick(60)