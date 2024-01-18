import pygame

#Initialize pygame
pygame.init()

#Create Display
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Movement Restriction')


#Load Images
tima_image = pygame.image.load('tiemaaa.png')
tima_rect = tima_image.get_rect()
tima_rect.topleft = (25,25)

#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#Set game values
VELOCITY = 5


#Game Loop
running = True
while running:
    for event in pygame.event.get():
        
        #Check if user wants out
        if event.type == pygame.QUIT:
            running = False

##### Important part of this class
            
    #Get a list of all keys currently being held
    #This is not an event, it is a state
    keys = pygame.key.get_pressed()
    #Move the image continuously
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and tima_rect.left > 0: #adding limit to to where the image can go nd using the asdw keys as arrows
        tima_rect.x -= VELOCITY
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and tima_rect.right < WINDOW_WIDTH: #adding limit to to where the image can go nd using the asdw keys as arrows
        tima_rect.x += VELOCITY
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and tima_rect.top > 0: #adding limit to to where the image can go and using the asdw keys as arrows
        tima_rect.y -= VELOCITY
    if (keys[pygame.K_DOWN] or keys[pygame.K_s])and tima_rect.bottom < WINDOW_HEIGHT: #adding limit to to where the image can go nd using the asdw keys as arrows
        tima_rect.y += VELOCITY



    #Fill surface with black
    display_surface.fill((0,0,0))

    #Blit image
    display_surface.blit(tima_image, tima_rect)

    #Update display
    pygame.display.update()

    #Tick the clock
    clock.tick(FPS)

pygame.quit()
