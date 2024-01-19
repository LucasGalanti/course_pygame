import pygame
import random

#Initialize Pygame
pygame.init()

#region - Display Settings
WINDOW_WIDTH = 1270
WINDOW_HEIGHT = 856
MIN_PLAYABLE_HEIGHT = 120
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('Catch the tima')

#endregion

#region - Define Colors

BLACK =  (0,0,0)
RED =    (255, 0, 0)
GREEN =  (0, 255, 0)
BACKGROUND =   (25, 0, 0)
YELLOW = (255, 255, 0)
CYAN =   (0, 255, 255)
MAGENTA = (255, 0, 255)
WHITE =  (255, 255, 255)
BLUE =   (0, 0, 255)

#endregion

#region - Images

#Tima
tima_image = pygame.image.load('Catch the tima/tima_3.png')
tima_rect = tima_image.get_rect()
tima_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

#Background
background_image = pygame.image.load('Catch the tima/background.png')
background_rect = background_image.get_rect()
background_rect.topleft = (0,0)


#endregion

#region - Game Settings

##CONSTANTS
INITIAL_SPEED = 5
ACCELARATION = 1
INITIAL_LIVES = 5
INITIAL_SCORE = 0

##Variables

lives = INITIAL_LIVES
score = INITIAL_SCORE

tima_speed = INITIAL_SPEED
tima_dx = random.choice([-1,1])
tima_dy = random.choice([-1,1])

#FPS and Clock
FPS = 60
clock = pygame.time.Clock()

#endregion

#region - Fonts and text
##FONTS
system_font = pygame.font.SysFont('calibri', 25)
coca_font = pygame.font.Font('Catch the tima/coca_font.ttf', 100)
hud_font = pygame.font.Font('Catch the Tima/Franxurter.ttf', 50)

##TEXT
title_text = coca_font.render('Catch the Tima', True, RED)
title_rect = title_text.get_rect()
title_rect.centerx = WINDOW_WIDTH//2
title_rect.top = 10


lives_text = hud_font.render('Lives:'+str(lives), True, RED)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 10, title_rect.centery)

score_text = hud_font.render('Score:'+str(score), True, RED)
score_rect = score_text.get_rect()
score_rect.topleft = (10, title_rect.centery)


game_over_text = coca_font.render('Game Over', True, RED, BACKGROUND)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2-50)

continue_text = system_font.render('Press ESC to quit or other key to continue', True, RED, BACKGROUND)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

#endregion

#region - Defining functions
def update_hud():
        
        #Update values and rects
        lives_text = hud_font.render('Lives:'+str(lives), True, RED)
        lives_rect = lives_text.get_rect()
        lives_rect.topright = (WINDOW_WIDTH - 10, title_rect.centery)

        score_text = hud_font.render('Score:'+str(score), True, RED)
        score_rect = score_text.get_rect()
        score_rect.topleft = (10, title_rect.centery)
        
        #Blit HUD
        display_surface.blit(background_image,background_rect)
        display_surface.blit(title_text, title_rect)
        display_surface.blit(lives_text, lives_rect)
        display_surface.blit(score_text, score_rect)
        pygame.draw.line(display_surface, RED, (0, MIN_PLAYABLE_HEIGHT), (WINDOW_WIDTH, MIN_PLAYABLE_HEIGHT))
#endregion

#region - Sound and Music

background_music = pygame.mixer.music.load('Catch the tima/musica_fundo.wav')

hit_sound = pygame.mixer.Sound('Catch the tima/click_sound.wav')
miss_sound = pygame.mixer.Sound('Catch the tima/miss_sound.wav')
miss_sound.set_volume(0.3)
game_over_sound = pygame.mixer.Sound('Catch the tima/game_over_sound.wav')
#endregion

#region - GAME LOOP ####
pygame.mixer.music.play(-1,0.0)
running = True
while running:
    #region Check events
    for event in pygame.event.get():
        
        #Check if player wants out
        if event.type == pygame.QUIT:
            running = False

        #Check if player clicked somewhere
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]

            #The tima was clicked
            if tima_rect.collidepoint(mouse_x, mouse_y):
                hit_sound.play()
                score += 1
                tima_speed += ACCELARATION
                #changing 
                previous_dx = tima_dx
                previous_dy = tima_dy
                while (tima_dx == previous_dx and tima_dy == previous_dy):
                    tima_dx = random.choice([-1,1])
                    tima_dy = random.choice([-1,1])
            
            else:
                miss_sound.play()
                lives -= 1
    
    #endregion

    #region - Tima movement
    #Move the tima
    tima_rect.x += tima_dx*tima_speed
    tima_rect.y += tima_dy*tima_speed

    #Bounce the tima on the edges
    if tima_rect.left <= 0 or tima_rect.right >= WINDOW_WIDTH:
        tima_dx = -tima_dx

    if tima_rect.top <= MIN_PLAYABLE_HEIGHT or tima_rect.bottom >= WINDOW_HEIGHT:
        tima_dy = -tima_dy

    #endregion

    #region - check for game over
    
    if lives <= 0:
        pygame.mixer.music.stop()
        game_over_sound.play()

        update_hud()
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        pygame.display.update()

        game_stop = True
        while game_stop:
            for event in pygame.event.get():
                #Check if the player wants to continue
                if (event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN) :
                    pygame.mixer.music.play(-1,0.0)
                    tima_speed = INITIAL_SPEED
                    score = INITIAL_SCORE
                    lives = INITIAL_LIVES
                    game_stop = False

                #Check if player wants out
                if event.type == pygame.QUIT or ((event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE)):
                    running = False
                    game_stop = False
    
    #endregion

    #region - Display Update
    update_hud()
    #Blit assets
    display_surface.blit(tima_image, tima_rect)

    pygame.display.update()
    clock.tick(FPS)
    #endregion

#endregion

pygame.quit()