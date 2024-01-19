import pygame
import random

#Initiate the game
pygame.init()

#region - Initiate the display  ####
WINDOW_WIDTH = 1800
WINDOW_HEIGHT = 900
MAX_PLAYABLE_HEIGHT = 200

display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT),pygame.SCALED)
pygame.display.toggle_fullscreen()
pygame.display.set_caption("Feed the Tima")
#endregion

#region - Define Colors
BLACK =  (0,0,0)
RED =    (255, 0, 0)
GREEN =  (0, 255, 0)
BLUE =   (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN =   (0, 255, 255)
MAGENTA = (255, 0, 255)
WHITE =  (255, 255, 255)
#endregion

#region - Game Settings

#FPS and Clock
FPS = 60
clock = pygame.time.Clock()

#Game Values
##FIXED
PLAYER_STARTING_LIVES = 5
PLAYER_VELOCITY = 5
COCA_START_VELOCITY = 7
COCA_ACCELERATION = 1
BUFFER_DISTANCE = 100 #how far the coin start from the edge of the screen

##Starting variables
score = 0
player_lives = PLAYER_STARTING_LIVES
coca_velocity = COCA_START_VELOCITY

#endregion

#region - Fonts and Text
#fonts
title_font = pygame.font.Font('feed_the_tima/coca_font.ttf', 150)
system_font = pygame.font.SysFont('Calibri', 50)

#texts
title_text = title_font.render('Coquinha Huuuum 2', True, RED)
title_rect = title_text.get_rect()
title_rect.centerx = WINDOW_WIDTH//2
title_rect.y = 10

score_text = system_font.render('Score = ' + str(score), True, RED)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

life_text = system_font.render('Vidas = ' + str(player_lives), True, RED)
life_rect  = life_text.get_rect()
life_rect.topright = (WINDOW_WIDTH-10, 10)

game_over_text = title_font.render('Game Over', True, RED)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

continue_text = system_font.render('Press Any key to play again or ESC to quit', True, RED)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 60)


#endregion

#region - Sounds and Music

#SOUNDS
drink_sound = pygame.mixer.Sound('feed_the_tima/gulp.mp3')
miss_sound = pygame.mixer.Sound('feed_the_tima/sound_1.wav')

#BACKGROUND MUSIC
pygame.mixer.music.load('feed_the_tima/musica_yuri.wav')

#endregion

#region - Images and Assets

tima_image = pygame.image.load('feed_the_tima/tima_2.png')
tima_rect = tima_image.get_rect()
tima_rect.x = 50
tima_rect.top = (MAX_PLAYABLE_HEIGHT+WINDOW_HEIGHT)//2



coca_image = pygame.image.load('feed_the_tima/coquinha_hum.png')
coca_rect = coca_image.get_rect()
coca_rect.center = (WINDOW_WIDTH+BUFFER_DISTANCE, random.randint(MAX_PLAYABLE_HEIGHT+10, WINDOW_HEIGHT-10))

#endregion

#region - Game loop

pygame.mixer.music.play(
    -1, #loop infinite
    0.0 #start at 0
    )

running = True
while running:
    #region - Events

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #endregion

    keys = pygame.key.get_pressed()

    #region - Control Keys

    if keys[pygame.K_UP] and tima_rect.top > MAX_PLAYABLE_HEIGHT :
        tima_rect.y -= PLAYER_VELOCITY
    if keys[pygame.K_DOWN] and tima_rect.bottom < WINDOW_HEIGHT :
        tima_rect.y += PLAYER_VELOCITY

    #endregion
        
    #region - coca movement

    if coca_rect.x < 0: #tima não pegou a coca
        player_lives -= 1
        miss_sound.play()
        coca_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
        coca_rect.y = random.randint(MAX_PLAYABLE_HEIGHT+10, WINDOW_HEIGHT-10)
    else:
        #Move the coin
        coca_rect.x -= coca_velocity

    #endregion

    #region - Check for colisions
        
    if tima_rect.colliderect(coca_rect):
        score += 1
        drink_sound.play()
        coca_velocity += COCA_ACCELERATION
        coca_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
        coca_rect.y = random.randint(MAX_PLAYABLE_HEIGHT+10, WINDOW_HEIGHT-10)
    
    #endregion

    #region - Display
        
    ##Update HUD
    score_text = system_font.render('Score = ' + str(score), True, RED)
    life_text = system_font.render('Vidas = ' + str(player_lives), True, RED)

    ##Check for GAMEOVER

    if player_lives == 0 :
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text,continue_rect)
        pygame.display.update()

        #Pause the game until player presses a key, then reset game
        pygame.mixer.music.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                #The player wants to play again
                if event.type == pygame.KEYDOWN:
                    score = 0
                    player_lives = PLAYER_STARTING_LIVES
                    coca_velocity = COCA_START_VELOCITY
                    tima_rect.y = (MAX_PLAYABLE_HEIGHT+WINDOW_HEIGHT)//2
                    pygame.mixer.music.play(-1,0.0)
                    is_paused = False

                #If the player wants out
                if (event.type == pygame.QUIT) or ((event.type ==pygame.KEYDOWN) and event.key == pygame.K_ESCAPE):
                    is_paused = False
                    running = False
                

    ##FILL the display
    display_surface.fill(BLACK)

    ##Blit the HUD
    display_surface.blit(score_text, score_rect)
    display_surface.blit(life_text, life_rect)
    display_surface.blit(title_text,title_rect)
    pygame.draw.line(display_surface,RED,(0,MAX_PLAYABLE_HEIGHT-10),(WINDOW_WIDTH,MAX_PLAYABLE_HEIGHT-10),3)

    ##Blit the images
    display_surface.blit(tima_image, tima_rect)
    display_surface.blit(coca_image, coca_rect)

    ##Update the display
    pygame.display.update()
    clock.tick(FPS)

    #endregion

#endregion

pygame.quit()