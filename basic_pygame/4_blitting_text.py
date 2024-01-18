import pygame

#Initialize Pygame
pygame.init()

#set display
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Blitting Images!')

#Define Colors
GREEN =     (0, 255, 0)
DARKGREEN = (10, 50, 10)
BLACK=      (0,0,0)

#See all available system fonts
#fonts = pygame.font.get_fonts()
#for font in fonts:
    #print(font)

#Define Fonts
system_font = pygame.font.SysFont('calibri',64)
custom_font = pygame.font.Font('basic_pygame/basic_tutorial_assets/basic_tutorial_assets/AttackGraffiti.ttf', 32)

#Define text
system_text = system_font.render('Dragons Rule', True, GREEN, DARKGREEN)
system_text_rect = system_text.get_rect()
system_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

custom_text = custom_font.render('Custom font text', True, GREEN, BLACK)
custom_text_rect = custom_text.get_rect()
custom_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 100)

#start_window
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Blit (copy) the text surfaces to the display surface
    display_surface.blit(system_text, system_text_rect)
    display_surface.blit(custom_text, custom_text_rect)

    #Update the display
    pygame.display.update()


#End the game
pygame.quit()

