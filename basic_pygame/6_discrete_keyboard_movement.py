import pygame

#Initialize pygame

pygame.init()

#Create our display Surface
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('Discrete Keyboard Movement')

#Set game values
VELOCITY = 10

#Load in images
dragon_image = pygame.image.load('basic_pygame/tiemaaa.png')
dragon_rect = dragon_image.get_rect()
dragon_rect.centerx = WINDOW_WIDTH//2
dragon_rect.bottom = WINDOW_HEIGHT


#Game Running Loop
running = True
while running:
    for event in pygame.event.get():
        print(event)

        #Check if user wants to quit
        if event.type == pygame.QUIT:
            running = False

        #Check for discrete movement
        if event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dragon_rect.x -= VELOCITY       #Change the x position of the rect horizontally and negativelly by 10 (velocity value) values each press
            if event.key == pygame.K_RIGHT:
                dragon_rect.x += VELOCITY       #Change the x position of the rect horizontally and positivelly by 10 (velocity value) values each press
            if event.key == pygame.K_UP:
                dragon_rect.y -= VELOCITY       #Change the y position of the rect horizontally and negativelly by 10 (velocity value) values each press
            if event.key == pygame.K_DOWN:
                dragon_rect.x += VELOCITY       #Change the y position of the rect horizontally and negativelly by 10 (velocity value) values each press



    #Fill the display surface to cover old images
    display_surface.fill((0,0,0))
    #Blit (copy) assets to screen
    display_surface.blit(dragon_image,dragon_rect)

    #Update the display
    pygame.display.update()



#Quit Game
pygame.quit()