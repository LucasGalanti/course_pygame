import pygame

pygame.init()

#creating our display
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('Mouse Movement')

#Load Images

tima_image = pygame.image.load('basic_pygame/tiemaaa.png')
tima_rect = tima_image.get_rect()
tima_rect.topleft = (25,25)

#Creating Game Loop
running = True
while running:
    for event in pygame.event.get():
        #Check if user wants out
        if event.type == pygame.QUIT:
            running = False
        
        #Check for mouse movement
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event)
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            tima_rect.centerx = mouse_x
            tima_rect.centery = mouse_y

        #Drage the object when the mouse button is clicked (Hold)
        if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1: #buttons[0] means left  button
            print(event)
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            tima_rect.centerx = mouse_x
            tima_rect.centery = mouse_y

    #Fill the displays
    display_surface.fill((0,0,0))

    #Blit assets
    display_surface.blit(tima_image, tima_rect)

    #Update the display
    pygame.display.update()

#quitting game
pygame.quit()