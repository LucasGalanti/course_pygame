import pygame

#initialize pygame
pygame.init()

#Create display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode(size = (WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Blitting Images!')

#Create Images...return a surface object with the image drawn on it
#We can then get the rect of the surface and use the rect to position the image.

dragon_left_image = pygame.image.load('basic_pygame/basic_tutorial_assets/basic_tutorial_assets/dragon_left.png')
dragon_left_rect = dragon_left_image.get_rect()
dragon_left_rect.topleft = (0,0)

dragon_right_image = pygame.image.load('basic_pygame/basic_tutorial_assets/basic_tutorial_assets/dragon_right.png')
dragon_right_rect = dragon_right_image.get_rect()
dragon_right_rect.topright = (WINDOW_WIDTH, 0)

#The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Blit (copy) a surface object at the given coordinates to our display
    display_surface.blit(dragon_left_image, dragon_left_rect)
    display_surface.blit(dragon_right_image, dragon_right_rect)

    pygame.draw.line(display_surface, (255,255,255),(0,100),(WINDOW_WIDTH,100), 5)

    #Update the display
    pygame.display.update()

#End the game
pygame.quit()