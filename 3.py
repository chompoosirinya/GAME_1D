import pygame
import sys
from sys import exit
import random
import pickle
from button import Button
pygame.init()


def Rungame():
  screen = pygame.display.set_mode((1280, 720))
  pygame.display.set_caption(("Catch-A-Cloud"))
  clock = pygame.time.Clock()
  # game_font = pygame.font.SysFont("arialblack", 40)
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
  
  #cloud
  cloud = pygame.image.load('graphic/cloud.png').convert_alpha()
  cloud = pygame.transform.scale(cloud, (80, 80))
  cloud_rect = cloud.get_rect(topright=(random.randint(100, 1180), 0))
  
  #blackcloud
  blackcloud = pygame.image.load('graphic/blackcloud.png').convert_alpha()
  blackcloud = pygame.transform.scale(blackcloud, (80, 80))  
  blackcloud_rect = blackcloud.get_rect(topright=(random.randint(100, 1280), 0))
  
  #lightning
  lightning = pygame.image.load('graphic/lightning.png').convert_alpha()
  lightning = pygame.transform.scale(lightning, (80, 80))
  
  #rainbow
  rainbow = pygame.image.load('graphic/rainbow.png').convert_alpha()
  rainbow = pygame.transform.scale(rainbow, (80, 50))
  

  def background():
    background = pygame.image.load('graphic/bg.png').convert_alpha()
    background = pygame.transform.scale(background, (1280, 720))
    screen.blit(background, (0, 0))
  def display_score(score):
    high_score_font = pygame.font.SysFont('arialblack', 30)
    score_surf = high_score_font.render(f"Score: {score}", False, 'deeppink')
    score_surf_rect = score_surf.get_rect(midbottom = (640,90))
    high_score_font = pygame.font.SysFont('arialblack', 30)
    high_score_surf = high_score_font.render(f"High Score: {high_score}", False, 'deeppink')
    high_score_surf_rect = high_score_surf.get_rect(midbottom = (640,50))
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
    play_again_rect = play_again_surf.get_rect(center = (640,360))
    pygame.draw.rect(screen, 'White', play_again_rect)
    screen.blit(play_again_surf, play_again_rect)
  def final_score_display(final_score, high_score):
    if final_score > high_score:
      new_high_score_font = pygame.font.SysFont('arialblack', 60)
      new_high_score = new_high_score_font.render(f"New High Score: {final_score}", False, 'deeppink')
      new_high_score_rect = new_high_score.get_rect(center = (640,300))
      pygame.draw.rect(screen, 'White', new_high_score_rect)
      screen.blit(new_high_score, new_high_score_rect)
      high_score = final_score
      with open('HighScore', 'wb') as file:
          pickle.dump(high_score, file)
    else:
      last_font = pygame.font.SysFont('arialblack', 60)
      score_surf = last_font.render(f"Final Score: {score}", False, 'deeppink')
      score_surf_rect = score_surf.get_rect(center = (640,300))
      pygame.draw.rect(screen, 'White', score_surf_rect)
      screen.blit(score_surf, score_surf_rect)
  
  def welcome_surf():
    welcome_font = pygame.font.SysFont('arialblack', 70)
    welcome_surf = welcome_font.render("Catch-A-Cloud", False, 'deeppink')
    welcome_surf_rect = welcome_surf.get_rect(midbottom = (650,360))
    pygame.draw.rect(screen, 'White', welcome_surf_rect)
    screen.blit(welcome_surf, welcome_surf_rect)
     
  def title_screen():
    welcome_surf()
    
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
  cloud_timer = pygame.USEREVENT + 1
  pygame.time.set_timer(cloud_timer, 1500)
  #blackcloud Timer
  blackcloud_rect_list = []
  blackcloud_timer = pygame.USEREVENT + 5
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
  count_down = 2




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
      if how_to_play < 2:
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
      play_again_display()
      final_score_display(final_score, high_score) 
    pygame.display.update()
    clock.tick(60)

def score():
  screen = pygame.display.set_mode((1280, 720))
  clock = pygame.time.Clock()
  gamerun = Rungame(screen, 1280, 720)
  font = pygame.font.SysFont('arialblack', 20)
  # music = pygame.mixer.music.load("graphics/music/bg.mp3")
  # pygame.mixer.music.play(-1)
  game_status = 1
  prev_player_score = 0
  new_player_score = 0
  scores = []
  rankscores = []
  show = 0
  def display_text(text, size, color, pos, screen):
      font = pygame.font.Font('graphics/font/PressStart2P-vaV7.ttf', size)
      text_surf = font.render(f'{text}', False, color)
      text_rect = text_surf.get_rect(center=pos)
      screen.blit(text_surf, text_rect)
  def draw_text_rank(text, color, size, screen, pos):
      font = pygame.font.Font('graphics/font/PressStart2P-vaV7.ttf', size)
      textobj = font.render(text, False, color)
      textrect = textobj.get_rect(midleft = pos)
      screen.blit(textobj, textrect)
  def ranking():
      global scores, rankscores, show
      if show != 1:
          scores = []
          rankscores = []
          with open('score.txt') as file:
              for line in file:
                  name, score = line.split(',')
                  score = int(score)
                  scores.append((name, score))
              scores.sort(key=lambda s: s[1])
              scores.reverse()
              for num in range(0, 5):
                  rankscores.insert(num,scores[num])
              file.flush()
              show = 1
  def display_rank():
      ranking()
      space = 0
      for i in range(0, 5):
          draw_text_rank(f'{rankscores[i][0]}', ('black'), 20, screen, (1280 / 2 - 250, 230 + space))
          space += 50
      space = 0
      for i in range(0, 5):
          draw_text_rank(f'{rankscores[i][1]}', ('black'), 20, screen, (1280 / 2 + 200, 230 + space))
          space += 50
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("graphic/sky.png").convert_alpha()

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.SysFont('arialblack', size)

def play():
  while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))       

        PLAY_TEXT = get_font(45).render("Enter Your Name.", True, "Black")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 200))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="PLAY", font=get_font(75), base_color="Black", hovering_color="Blue")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    Rungame()

        pygame.display.update()

def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        START_BUTTON = Button(image=pygame.image.load("graphic/start.png"), pos=(640, 80), 
                            text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        SCORE_BUTTON = Button(image=pygame.image.load("graphic/score.png"), pos=(640, 268), 
                            text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        EXIT_BUTTON = Button(image=pygame.image.load("graphic/exit.png"), pos=(640, 450), 
                            text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [START_BUTTON, SCORE_BUTTON, EXIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if START_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if SCORE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if EXIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()