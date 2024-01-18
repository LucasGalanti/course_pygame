import pygame
import random

#initialize pygame
pygame.init()

#Create our display
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('Collision Detection')

RED =    (255, 0, 0)

############SOUND##################
sound_1 = pygame.mixer.Sound('gulp.mp3')


############MUSIC##################
pygame.mixer.music.load('musica fundo.mp3')
#Play and stop the music
pygame.mixer.music.play(
    -1, #loop infinite
    0.0 #start at 0
    )

##############IMAGE###############
#load image
tima_image = pygame.image.load('tiemaaa.png')
tima_rect = tima_image.get_rect()
tima_rect.topleft = (100,100)


coca_image = pygame.image.load('coquinha_hum.png')
coca_rect = coca_image.get_rect()
coca_rect.topleft = (300,300)


########### TEXT #################
#Define Fonts
system_font = pygame.font.SysFont('calibri',64)
huum_font = pygame.font.SysFont('calibri',20)
score_font = pygame.font.SysFont('calibri',30)

title_text = system_font.render('COQUINHA HUUUM', True, RED)
title_text_rect = title_text.get_rect()
title_text_rect.center = (WINDOW_WIDTH//2, 50)

#Huum text with max of 2 seconds

huum_text = huum_font.render('Huuum...', True, RED)
huum_rect = huum_text.get_rect()
huum_rect.center = (WINDOW_WIDTH//2, 100000)
max_huum_time = 2000 #miliseconds

#Coquinhas no dia

score = 0
score_text = score_font.render('COQUINHAS TOMADAS: '+str(score), True, RED)
score_rect = score_text.get_rect()
score_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT - 100)
max_huum_time = 2000 #miliseconds


#####Setting FPS and Velocity################
FPS = 60
VELOCITY = 5
clock = pygame.time.Clock()
#Setting clock

start_huum_time = pygame.time.get_ticks()+max_huum_time

#Create GameLoop
running = True
while running == True:

    #get current time
    current_time = pygame.time.get_ticks()


    for event in pygame.event.get():
        #Check if the user wants out
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and tima_rect.left > 0:
        tima_rect.x -= VELOCITY
    if keys[pygame.K_RIGHT] and tima_rect.right < WINDOW_WIDTH:
        tima_rect.x += VELOCITY
    if keys[pygame.K_UP] and tima_rect.top > 0:
        tima_rect.y -= VELOCITY    
    if keys[pygame.K_DOWN] and tima_rect.bottom < WINDOW_HEIGHT:
        tima_rect.y += VELOCITY


    #Check for collision between two rects
    if tima_rect.colliderect(coca_rect):
        start_huum_time = pygame.time.get_ticks()
        sound_1.play()
        score +=1
        score_text = score_font.render('COQUINHAS TOMADAS: '+str(score), True, RED)
        #print huuuum
        huum_rect.bottom = tima_rect.top + 2
        huum_rect.left = tima_rect.right + 2

        #change coca place
        coca_rect.x = random.randint(0, WINDOW_WIDTH - 32)
        coca_rect.y = random.randint(250, WINDOW_HEIGHT - 64)

    #fill the surface
    display_surface.fill((0,0,0))

    #Draw rectangles to represent the rect of each object
    #pygame.draw.rect(display_surface, (255,0,0), tima_rect, 1)
    #pygame.draw.rect(display_surface, (255,0,0), coca_rect, 1)

    #blit the image
    display_surface.blit(tima_image, tima_rect)
    display_surface.blit(coca_image, coca_rect)

    #blit the huuum
    if current_time - start_huum_time <= max_huum_time:
        display_surface.blit(huum_text, huum_rect)

    #blit the text
    display_surface.blit(title_text, title_text_rect)
    display_surface.blit(score_text, score_rect)

    #update the display
    pygame.display.update()

    #Tick the clock
    clock.tick(FPS)

pygame.quit()
