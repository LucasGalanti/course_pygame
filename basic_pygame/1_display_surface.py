import pygame

# Initialize pygame
pygame.init()

# Create a display surface and set its caption

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Hello World')
#The main game loop

running = True
while running:
    #Loopl through a list of Event objects that have occured
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False

# End the game

pygame.quit()