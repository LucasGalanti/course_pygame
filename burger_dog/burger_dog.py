import pygame
import random

pygame.init()

#region - Display Settings
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Burger_dog')

#endregion

#region - Colors
BLACK =  (0,0,0)
RED =    (255, 0, 0)
GREEN =  (0, 255, 0)
BACKGROUND =   (25, 0, 0)
YELLOW = (255, 255, 0)
CYAN =   (0, 255, 255)
MAGENTA = (255, 0, 255)
WHITE =  (255, 255, 255)
BLUE =   (0, 0, 255)
ORANGE = (246, 170, 54)


#endregion

#region - Game Settings
##CONSTANT VALUES

FPS = 60
clock = pygame.time.Clock()
PLAYER_STARTING_LIVES = 3
PLAYER_NORMAL_VELOCITY = 5
PLAYER_BOOST_VELOCITY = 10
STARTING_BOOST_LEVEL = 100
STARTING_BURGER_VELOCITY = 3
BURGER_ACCELERATION = .25
BUFFER_DISTANCE = 100
PLAYER_STARTING_POSITION = (WINDOW_WIDTH//2,WINDOW_HEIGHT - 30)

##Variables
score = 0
burger_points = 0
burgers_eaten = 0

player_lives = PLAYER_STARTING_LIVES
player_velocity = PLAYER_STARTING_LIVES
boost_level = STARTING_BOOST_LEVEL
burger_velocity = STARTING_BURGER_VELOCITY

#endregion

#region - Fonts & Texts

system_font = pygame.font.SysFont('Calibri', 25)
personal_font = pygame.font.Font('burger_dog/WashYourHand.ttf', 32)
title_font = pygame.font.Font('burger_dog/WashYourHand.ttf', 50)

#Title
title_text = title_font.render('Burger Dog', True, ORANGE)
title_rect = title_text.get_rect()
title_rect.centerx = WINDOW_WIDTH//2
title_rect.top = 10

#Burger Points
points_text = personal_font.render('Burger Points: ' +str(burger_points), True, ORANGE)
points_rect = points_text.get_rect()
points_rect.topleft = (10,10)

#Score
score_text = personal_font.render('Score: ' +str(score), True, ORANGE)
score_rect = score_text.get_rect()
score_rect.topleft = (10,points_rect.bottom + 10)

#Burgers Eaten
eaten_text = personal_font.render('Burgers Eaten: ' +str(burgers_eaten), True, ORANGE)
eaten_rect = eaten_text.get_rect()
eaten_rect.centerx = title_rect.centerx
eaten_rect.top = title_rect.bottom + 10

#Lives
lives_text = personal_font.render('Lives: ' +str(player_lives), True, ORANGE)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 10,10)

#Boost
boost_text = personal_font.render('Boost: ' +str(boost_level), True, ORANGE)
boost_rect = boost_text.get_rect()
boost_rect.topright = (WINDOW_WIDTH - 10,lives_rect.bottom + 10)

#Game Over Text
game_over_text = personal_font.render('FINAL SCORE: ' + str(score), True, ORANGE)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

continue_text = personal_font.render('Press any key to play again', True, ORANGE)
continue_rect = continue_text.get_rect()
continue_rect.centerx = WINDOW_WIDTH//2
continue_rect.top = game_over_rect.bottom+1

#endregion

#region - Music and sounds
pygame.mixer.music.load('burger_dog/bd_background_music.wav')
bark_sound = pygame.mixer.Sound('burger_dog/bark_sound.wav')
miss_sound = pygame.mixer.Sound('burger_dog/miss_sound.wav')
game_over_sound = pygame.mixer.Sound('burger_dog/game_over_sound.wav')
#endregion

#region -Set images
#player Images
player_image_right = pygame.image.load("burger_dog/dog_right.png")
player_image_left = pygame.image.load("burger_dog/dog_left.png")

player_image = player_image_left
player_rect = player_image.get_rect()
player_rect.center = PLAYER_STARTING_POSITION

#burger Image
burger_image = pygame.image.load('burger_dog/burger.png')
burger_rect = burger_image.get_rect()
burger_rect.topleft = (random.randint(0, WINDOW_WIDTH - 32), - BUFFER_DISTANCE)

#endregion

#region - Game Loop
running = True
pygame.mixer.music.play(-1,0)
while running:

    #region - Effect of any clicking
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #endregion
            
    #region - Effect of Keys pressed
    keys = pygame.key.get_pressed()

    #Engage Boost
    if keys[pygame.K_SPACE] and boost_level>0:
        player_velocity = PLAYER_BOOST_VELOCITY
        boost_level -= 1
    else:
        player_velocity = PLAYER_NORMAL_VELOCITY

    #Move the player
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= player_velocity
        player_image = player_image_left
    if keys[pygame.K_RIGHT] and player_rect.right < WINDOW_WIDTH:
        player_rect.x += player_velocity
        player_image = player_image_right
    if keys[pygame.K_UP] and player_rect.top > 100:
        player_rect.y -= player_velocity
    if keys[pygame.K_DOWN] and player_rect.bottom < WINDOW_HEIGHT:
        player_rect.y += player_velocity

    #endregion

    #region - update positions and values
    
    #Move the Burger and update its value
    burger_rect.y += burger_velocity
    burger_points = int(burger_velocity*(WINDOW_HEIGHT - burger_rect.y + 100)) #the lowest the burger is, the lower the score

    #Player missed the burger
    if burger_rect.top > WINDOW_HEIGHT:
        player_lives -= 1
        miss_sound.play()
        burger_rect.x = random.randint(10, WINDOW_WIDTH-10)
        burger_rect.y = BUFFER_DISTANCE
        burger_velocity = STARTING_BURGER_VELOCITY

    #Player got the burger
    if player_rect.colliderect(burger_rect):
        score += burger_points
        burgers_eaten += 1
        bark_sound.play()
        burger_rect.x = random.randint(10, WINDOW_WIDTH-10)
        burger_rect.y = BUFFER_DISTANCE
        burger_velocity += BURGER_ACCELERATION
        boost_level += 25

    #Cap Boost level at starting level
    if boost_level > STARTING_BOOST_LEVEL:
        boost_level = STARTING_BOOST_LEVEL

    #endregion

    #region - GAME OVER
    if player_lives <= 0:
        game_over = True
        pygame.mixer.music.stop()
        game_over_sound.play()
        
        #update HUB
        display_surface.fill(BLACK)
        display_surface.blit(title_text, title_rect)
        pygame.draw.line(display_surface, WHITE, (0,100), (WINDOW_WIDTH, 100), 3)

        #Update game_over text
        game_over_text = personal_font.render('FINAL SCORE: ' + str(score), True, ORANGE)
        game_over_rect = game_over_text.get_rect()
        game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)

        #update display
        pygame.display.update()
        while game_over:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                    game_over = False
                    running = False
            
                if event.type == pygame.KEYDOWN:
                    player_lives = PLAYER_STARTING_LIVES
                    burger_velocity = STARTING_BURGER_VELOCITY
                    boost_level = STARTING_BOOST_LEVEL
                    player_rect.center = PLAYER_STARTING_POSITION
                    burgers_eaten = 0
                    score = 0
                    pygame.mixer.music.play()
                    game_over = False
            
    #endregion

    #region - Update surface

    #Fill the surface
    display_surface.fill(BLACK)

    #Update text
    boost_text = personal_font.render('Boost: ' +str(boost_level), True, ORANGE)
    lives_text = personal_font.render('Lives: ' +str(player_lives), True, ORANGE)
    eaten_text = personal_font.render('Burgers Eaten: ' +str(burgers_eaten), True, ORANGE)
    score_text = personal_font.render('Score: ' +str(score), True, ORANGE)
    points_text = personal_font.render('Burger Points: ' +str(burger_points), True, ORANGE)

    #Blit the HUD
    display_surface.blit(points_text, points_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(lives_text, lives_rect)
    display_surface.blit(boost_text,boost_rect)
    display_surface.blit(score_text,score_rect)
    display_surface.blit(eaten_text, eaten_rect)
    pygame.draw.line(display_surface, WHITE, (0,100), (WINDOW_WIDTH, 100), 3)

    #Blit assets
    display_surface.blit(player_image, player_rect)
    display_surface.blit(burger_image, burger_rect)

    #Update display and tick clock
    pygame.display.update()
    clock.tick(FPS)

    #endregion


#endregion

pygame.quit()