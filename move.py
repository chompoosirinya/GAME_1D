# import pygame module in this program 
import pygame

  
# activate the pygame library .  
# initiate pygame and give permission  
# to use pygame's functionality.  
pygame.init()
  
# create the display surface object  
# of specific dimension..e(500, 500).  
screen = pygame.display.set_mode((800, 800))

  
# set the pygame window name 
pygame.display.set_caption("Moving rectangle")

bg = pygame.image.load("graphic/bg.png")
  
# object current co-ordinates 
x = 250
y = 400
  
# dimensions of the object 
width = 20
height = 20
  
# velocity / speed of movement
vel = 2 
  
# Indicates pygame is running
run = True
  
# infinite loop 
while run:
    # creates time delay of 10ms 
    pygame.time.delay(10)
      
    # iterate over the list of Event objects  
    # that was returned by pygame.event.get() method.  
    for event in pygame.event.get():
          
        # if event object type is QUIT  
        # then quitting the pygame  
        # and program both.  
        if event.type == pygame.QUIT:
              
            # it will make exit the while loop 
            run = False
    # stores keys pressed 
    keys = pygame.key.get_pressed()
      
    # if left arrow key is pressed
    if keys[pygame.K_a] and x>0:
          
        # decrement in x co-ordinate
        x -= vel
          
    # if left arrow key is pressed
    if keys[pygame.K_d] and x<500-width:
          
        # increment in x co-ordinate
        x += vel
         
    # if left arrow key is pressed   
    if keys[pygame.K_w] and y>400:
          
        # decrement in y co-ordinate
        y -= vel
          
    # if left arrow key is pressed   
    if keys[pygame.K_s] and y<600-height:
        # increment in y co-ordinate
        y += vel
         
              
    # completely fill the surface object  
    # with black colour  
    screen.fill((0, 0, 0))
      
    # drawing object on screen which is rectangle here 
    pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))

    screen.blit(bg,(0,0))
      
    # it refreshes the window
    pygame.display.update() 
  
# closes the pygame window 
pygame.quit()