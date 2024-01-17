import pygame

#initialize game

pygame.init()

#create a dsiplay surface and set its caption

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption('Drawing Objects')

#Define colors as RGB tuples

BLACK =  (0,0,0)

RED =    (255, 0, 0)
GREEN =  (0, 255, 0)
BLUE =   (0, 0, 255)

YELLOW = (255, 255, 0)
CYAN =   (0, 255, 255)
MAGENTA = (255, 0, 255)
WHITE =  (255, 255, 255)

#Give a background color to the display
display_surface.fill(BLUE)

#Draw various shapes on our display
#Line(surface, color, starting point, ending point, thickness)
pygame.draw.line(
    surface =   display_surface,
    color =     RED,
    start_pos = (0,0),
    end_pos =   (100,100),
    width =     5
)

pygame.draw.line(surface = display_surface, color = GREEN, start_pos = (100,100), end_pos =   (200,300), width = 5)

#Circle (surface, color, center, radius, thickness)
pygame.draw.circle(
    surface =   display_surface,
    color =     MAGENTA,
    center =    (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), ##This way we put the center in the center of the window as weell
    radius =    200,
    width =     5
)

pygame.draw.circle(
    surface =   display_surface,
    color =     YELLOW,
    center =    (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), ##This way we put the center in the center of the window as weell
    radius =    300,
    width =     0   #Width of 0 fills the draw
)

#Rectangle(surface, color, (top-left x, top-left y, width, height))

pygame.draw.rect(
    surface = display_surface,
    color =   CYAN, 
    rect =    (500, 0, 100, 100), #(top-left x, top-left y, width, height)
    width =   3
)

pygame.draw.rect(
    surface = display_surface,
    color =   WHITE, 
    rect =    (500, 100, 50, 100), #(top-left x, top-left y, width, height)
)


#The main game loop
running = True
while running:
    for event  in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Update the display
    pygame.display.update()


# End the game
pygame.quit()