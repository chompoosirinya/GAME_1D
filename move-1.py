import pygame, random

pygame.init()

screen_width = 800
screen_height = 600


window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Test')
time = pygame.time.Clock()
bg_color1 = (135, 142, 142)  # MAIN BG COLOR
bg_color2 = (255, 0, 0)  # red
bg_color3 = (255, 255, 0)  # yellow
UFO = pygame.image.load('graphic/plane.png')
bg_pic = pygame.image.load('graphic/background.png')
clock = pygame.time.Clock()
# playerImg = pygame.image.load('graphic/plane.png')
playerX = random.randrange(0, screen_width)
playerY = -50
playerX_change = 0
player_speed = 5


# def player(x, y):
#     window.blit(playerImg, (playerX, playerY))


crashed = False

rect = UFO.get_rect()
obstacle = pygame.Rect(400, 200, 80, 80)

menu = True
playerY = playerY + player_speed
if playerY > screen_height:
    playerX = random.randrange(0,screen_width)
    playerY = -10


def ufo(x, y):
    window.blit(UFO, (x, y))


while menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                menu = False
    window.fill((0, 0, 0))
    time.tick(30)
    window.blit(bg_pic, (0, 0))
    pygame.display.update()
x = (screen_width * 0.45)
y = (screen_height * 0.8)
x_change = 0
car_speed = 0
y_change = 0

while not crashed:
    x += x_change
    if x < 0:
        x = 0
    elif x > screen_width - UFO.get_width():
        x = screen_width - UFO.get_width()

    y += y_change
    if y < 0:
        y = 0
    elif y > screen_height - UFO.get_height():
        y = screen_height - UFO.get_height()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        ############SIDE TO SIDE################
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
        ###########UP AND DOWN#################
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_change = -5
            elif event.key == pygame.K_DOWN:
                y_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = 0
    ##
    x += x_change
    y += y_change
    ##
    window.fill(bg_color1)
    ufo(x, y)
    # player(playerX, playerY)
    pygame.display.update()
    clock.tick(100)

pygame.quit()
quit()