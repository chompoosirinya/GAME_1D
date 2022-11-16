import pygame, os, random, csv, button, sys
from pygame import mixer
from score import ScoreInput

mixer.init()
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Taijaaginmha')

#set framerate
clock = pygame.time.Clock()
FPS = 60

#define game variables
GRAVITY = 0.75
SCROLL_THRESH = 200
ROWS = 16
COLS = 150
TILE_SIZE = SCREEN_HEIGHT // ROWS
TILE_TYPES = 21
MAX_LEVELS = 2
screen_scroll = 0
bg_scroll = 0
level = 1
start_game = False
start_intro = False
base_font = pygame.font.Font(None, 32)
base_font2 = pygame.font.Font(None, 56)


#define player action variables
moving_left = False
moving_right = False
shoot = False
grenade = False
grenade_thrown = False



def draw_score():
    text_score = base_font.render("SCORE : " + str(score + player.temp_score), True, (255, 255, 255))
    screen.blit(text_score, (600,20))

def draw_name():
    screen.fill('WHITE')
    
    text_name = base_font2.render("INPUT YOUR NAME", True, (0, 0, 0))
    screen.blit(text_name, (SCREEN_HEIGHT//2 - text_name.get_width()//2 + 85, 50))
    
    text_surface = base_font.render(player_name, True, (0, 0, 0))
    pygame.draw.rect(screen, 'WHITE', pygame.Rect(SCREEN_WIDTH//2 - text_surface.get_width()//2-5, SCREEN_HEIGHT//2 - text_surface.get_height()//2-5, text_surface.get_width()+10, text_surface.get_height()+5),  2)
    screen.blit(text_surface,(SCREEN_WIDTH//2 - text_surface.get_width()//2, SCREEN_HEIGHT//2 - text_surface.get_height()//2))

def draw_menu():
    
    text_name = base_font2.render("Taijaaginmha", True, (235, 65, 54))
    screen.blit(text_name, (SCREEN_WIDTH//2 - text_name.get_width()//2, 50))
    
    text_surface = base_font.render("65011003 Wisapat Pattanapun", True, (235, 65, 54))
    screen.blit(text_surface,(SCREEN_WIDTH - text_surface.get_width()-5, SCREEN_HEIGHT - text_surface.get_height()-5)) 

sctxt =open("scorebar.txt",'r')
pltxt =open("player.txt",'r')
scin =sctxt.read()
plin =pltxt.read()
            
scorex =""
scorelist =[]
scindex =-1

playerx=""
playerlist =[]
plindex =-1

for x in scin:
    scindex +=1
    scorex += x
    if x =='\n' or scindex == len(scin)-1:
        scorelist.append(scorex)
        scorex= ""

for x in plin:
    plindex +=1
    playerx += x
    if x =='\n' or plindex == len(plin)-1:
        playerlist.append(playerx)
        playerx= ""
sctxt.close()
pltxt.close()   
tran = True   

class Scoreboard():
    
    def read (self):
        sctxt = open("scorebar.txt",'r')
        pltxt = open("player.txt",'r')
        scin = sctxt.read()
        plin = pltxt.read()
            
        scorex =""
        scorelist =[]
        scindex =-1

        playerx=""
        playerlist =[]
        plindex =-1

        for x in scin:
            scindex +=1
            scorex += x
            if x =='\n' or scindex == len(scin)-1:
                scorelist.append(scorex)
                scorex= ""

        for x in plin:
            plindex +=1
            playerx += x
            if x =='\n' or plindex == len(plin)-1:
                playerlist.append(playerx)
                playerx= ""

        self.playername_first = ScoreInput(screen,"1. "+playerlist[0],(0,0,0),20,150,3)
        self.playername_second = ScoreInput(screen,"2. "+playerlist[1],(0,0,0),20,250,3)
        self.playername_third = ScoreInput(screen,"3. "+playerlist[2],(0,0,0),20,350,3)
        self.playername_fourth = ScoreInput(screen,"4. "+playerlist[3],(0,0,0),20,450,3)
        self.playername_fifth = ScoreInput(screen,"5. "+playerlist[4],(0,0,0),20,550,3)
        
        self.score_first = ScoreInput(screen,scorelist[0],(0,0,0),500,150,3)
        self.score_second = ScoreInput(screen,scorelist[1],(0,0,0),500,250,3)
        self.score_third = ScoreInput(screen,scorelist[2],(0,0,0),500,350,3)
        self.score_fourth = ScoreInput(screen,scorelist[3],(0,0,0),500,450,3)
        self.score_fifth = ScoreInput(screen,scorelist[4],(0,0,0),500,550,3)

        sctxt.close()
        pltxt.close()
    
    def display_score(self):
        self.read()
        self.playername_first.draw()
        self.playername_second.draw()
        self.playername_third.draw()
        self.playername_fourth.draw()
        self.playername_fifth.draw()
        self.score_first.draw()
        self.score_second.draw()
        self.score_third.draw()
        self.score_fourth.draw()
        self.score_fifth.draw()
    
    def run(self):
        screen.fill('WHITE')
        self.display_score()

#creat screen fades
intro_fade = ScreenFade(1, WHITE, 4)
death_fade = ScreenFade(2, WHITE, 4)

#create buttons
start_button = button.Button(SCREEN_WIDTH // 2 - 115, SCREEN_HEIGHT // 2 - 200, start_img, 1)
exit_button = button.Button(SCREEN_WIDTH // 2 - 110, SCREEN_HEIGHT // 2 + 100, exit_img, 1)
restart_button = button.Button(SCREEN_WIDTH // 2 - 115, SCREEN_HEIGHT // 2 - 50, restart_img, 1)
scoreboard_button =  button.Button(SCREEN_WIDTH // 2 - 110, SCREEN_HEIGHT // 2 -50, scoreboard_img, 1)
home_button = button.Button(SCREEN_WIDTH - 292, SCREEN_HEIGHT // 2 - 280, home_img, 0.5)
home_button1 = button.Button(SCREEN_WIDTH //  2 - 96, SCREEN_HEIGHT // 2 + 75, home_img, 1)
home_button2 = button.Button(SCREEN_WIDTH //  2 - 96, SCREEN_HEIGHT // 2 + 75, home_img, 1)


#create sprite groups
enemy_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
grenade_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()
item_box_group = pygame.sprite.Group()
decoration_group = pygame.sprite.Group()
water_group = pygame.sprite.Group()
exit_group = pygame.sprite.Group()



#create empty tile list
world_data = []
for row in range(ROWS):
    r = [-1] * COLS
    world_data.append(r)
#load in level data and create world
with open(f'level{level}_data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for x, row in enumerate(reader):
        for y, tile in enumerate(row):
            world_data[x][y] = int(tile)
world = World()
player, health_bar = world.process_data(world_data)

player_name = ''
player_name_confirm = False
pause = False
start_game = False
scoreboard_show = False
scoreboard = Scoreboard()
score = 0


run = True
while run:
    
    clock.tick(FPS)
    if start_game == False:
        #draw menu
        screen.fill(WHITE)
        draw_menu()
        #add buttons
        if start_button.draw(screen):
            start_game = True
            start_intro = True
        if exit_button.draw(screen):
            run = False
        if scoreboard_button.draw(screen):
            scoreboard_show = True

        if scoreboard_show == True:
            scoreboard.run()
            if home_button.draw(screen):
                scoreboard_show = False

    
    else:
        
        if player_name_confirm:
            #update background
            draw_bg()
            #draw world map
            world.draw()
            #show player health
            health_bar.draw(player.health)
            draw_score()
            #show ammo
            draw_text('AMMO: ', font, WHITE, 10, 35)
            for x in range(player.ammo):
                screen.blit(bullet_img, (90 + (x * 10), 40))
            #show grenades
            draw_text('GRENADES: ', font, WHITE, 10, 60)
            for x in range(player.grenades):
                screen.blit(grenade_img, (135 + (x * 15), 55))


            player.update()
            player.draw()

            for enemy in enemy_group:
                enemy.ai()
                enemy.update()
                enemy.draw()

            #update and draw groups
            bullet_group.update()
            grenade_group.update()
            explosion_group.update()
            item_box_group.update()
            decoration_group.update()
            water_group.update()
            exit_group.update()
            bullet_group.draw(screen)
            grenade_group.draw(screen)
            explosion_group.draw(screen)
            item_box_group.draw(screen)
            decoration_group.draw(screen)
            water_group.draw(screen)
            exit_group.draw(screen)

            #show intro
            if start_intro == True:
                if intro_fade.fade():
                    start_intro = False
                    intro_fade.fade_counter = 0

            #update player actions
            if player.alive:
                #shoot bullets
                if shoot:
                    player.shoot()
                #throw grenades
                elif grenade and grenade_thrown == False and player.grenades > 0:
                    grenade = Grenade(player.rect.centerx + (0.3 * player.rect.size[0] * player.direction),\
                                player.rect.top, player.direction)
                    grenade_group.add(grenade)
                    #reduce grenades
                    player.grenades -= 1
                    grenade_thrown = True
                if player.in_air:
                    player.update_action(2)#2: jump
                elif moving_left or moving_right:
                    player.update_action(1)#1: run
                else:
                    player.update_action(0)#0: idle
                screen_scroll, level_complete = player.move(moving_left, moving_right)
                bg_scroll -= screen_scroll
                #check if player has completed the level
                if level_complete:
                    start_intro = True
                    score += player.temp_score
                    level += 1
                    bg_scroll = 0
                    world_data = reset_level()
                    if level <= MAX_LEVELS:
                        #load in level data and create world
                        with open(f'level{level}_data.csv', newline='') as csvfile:
                            reader = csv.reader(csvfile, delimiter=',')
                            for x, row in enumerate(reader):
                                for y, tile in enumerate(row):
                                    world_data[x][y] = int(tile)
                        world = World()
                        player, health_bar = world.process_data(world_data) 
            
                    if level > MAX_LEVELS:
                            start_game = False
                            for x in range(len(scorelist)) :
                                if score >= int(scorelist[x]) and tran == True :
                                    scorelist.insert(x,str(score)+'\n')
                                    scorelist.pop(len(scorelist)-1)
                                    playerlist.insert(x,player_name+'\n')
                                    playerlist.pop(len(playerlist)-1)
                                    tran = False
                            plsend = ""
                            scsend = ""
                            for i in playerlist:
                                plsend += i
                            for i in scorelist:
                                scsend += i
                                
                            sctxt = open("scorebar.txt",'w') 
                            pltxt = open("player.txt",'w')
                            sctxt.write(scsend)
                            pltxt.write(plsend)
                            sctxt.close()
                            pltxt.close()
                            score_board_show = True
                            if home_button.draw(screen):
                                score_board_show = False
            else:
                screen_scroll = 0
                if death_fade.fade():
                    if restart_button.draw(screen):
                        death_fade.fade_counter = 0
                        start_intro = True
                        bg_scroll = 0
                        world_data = reset_level()
                        #load in level data and create world
                        with open(f'level{level}_data.csv', newline='') as csvfile:
                            reader = csv.reader(csvfile, delimiter=',')
                            for x, row in enumerate(reader):
                                for y, tile in enumerate(row):
                                    world_data[x][y] = int(tile)
                        world = World()
                        player, health_bar = world.process_data(world_data)
        else:
            draw_name()
            for event in pygame.event.get():
                if event.type == quit:
                   run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        player_name = player_name[:-1]
                    elif len(player_name) <= 20 and event.key != pygame.K_RETURN:
                        player_name += event.unicode
                    if event.key == pygame.K_RETURN and len(player_name) >= 1:
                        player_name_confirm = True

    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False
        #keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_SPACE:
                shoot = True
            if event.key == pygame.K_q:
                grenade = True
            if event.key == pygame.K_w and player.alive:
                player.jump = True
                jump_fx.play()
            if event.key == pygame.K_ESCAPE:
                run = False


        #keyboard button released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_SPACE:
                shoot = False
            if event.key == pygame.K_q:
                grenade = False
                grenade_thrown = False


    pygame.display.update()

pygame.quit()