import pygame
import random

pygame.init()

#region - Setting Display
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 1280
MIN_PLAYABLE_WIDTH = 100
MAX_PLAYABLE_WIDTH = WINDOW_WIDTH - MIN_PLAYABLE_WIDTH
MIN_PLAYABLE_HEIGHT = 233
MAX_PLAYABLE_HEIGHT = WINDOW_HEIGHT - MIN_PLAYABLE_WIDTH

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake')

#endregion

#region - Images and assets

colision_sprites = {
    'water1': pygame.Rect(210, 277, 329-208, 395-277),
    'water2': pygame.Rect(820, 308, 973-820, 396-308),
    'grass1': pygame.Rect(239, 626, 395-239, 781-626),
    'lava1':  pygame.Rect(754, 690, 907-754, 844-690)
}



#endregion

#region - Game Settings


START_SCORE = 0
SNAKE_SIZE = 20
SNAKE_VELOCITY = 20
FPS = 20

head_x = 600
head_y = 550

snake_dx = 0
snake_dy = 0
score = START_SCORE


clock = pygame.time.Clock()
#endregion

#region - Set Colors

GREEN = (0, 255, 0)
DARKGREEN = (10,50,10)
RED = (255,0,0)
DARKRED = (150, 0, 0)
WHITE = (255, 255, 255)

#endregion

#region - Set fonts and texts
title_font = pygame.font.SysFont('gabriola', 100, bold= True)
score_font = pygame.font.SysFont('gabriola', 50)


#set text
title_text = title_font.render('SNAKE', True, DARKGREEN)
title_rect = title_text.get_rect()
title_rect.centerx = WINDOW_WIDTH//2
title_rect.top = 30

score_text = score_font.render('Score:' + str(score) , True, GREEN)
score_rect = score_text.get_rect()
score_rect.topleft = (20,30)

game_over_text = title_font.render('GAME OVER', True, RED)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

continue_text = score_font.render('Press ESC to quit or any other key to continue', True, GREEN)
continue_rect = continue_text.get_rect()
continue_rect.center = game_over_rect.center
continue_rect.top = game_over_rect.bottom+1


#endregion

#region - Set song and music
##Background music
pygame.mixer.music.load('Snake/background_music.mp3')

#Sounds
eat_sound = pygame.mixer.Sound('Snake/eat_sound.wav')
game_over_sound = pygame.mixer.Sound('Snake/game_over_sound.wav')

#endregion

#region - Coordinates and rects (in this case, simple rects)

background = pygame.image.load('Snake/map.png')
background_rect = background.get_rect()
background_rect.topleft = (0,0)

apple_coord = (600,650, SNAKE_SIZE, SNAKE_SIZE)
apple_rect = pygame.draw.rect(display_surface, RED, apple_coord)

head_coord = (head_x,head_y, SNAKE_SIZE, SNAKE_SIZE)
head_rect = pygame.draw.rect(display_surface, (0,0,0), head_coord)

body_coords = []

#endregion

#region - Functions

def draw_colisions():
    for key in colision_sprites.keys():
        pygame.draw.rect(
            surface = display_surface,
            color =   (255,255,255), 
            rect =    colision_sprites[key],
            width =   1
        )

def create_invisible_colisions():
    invisible_colisions = (colision_sprites[key] for key in colision_sprites.keys())

def generate_apple_coordinates():
    while True:
        x = random.randint(MIN_PLAYABLE_WIDTH, MAX_PLAYABLE_WIDTH)
        y = random.randint(MIN_PLAYABLE_HEIGHT, MAX_PLAYABLE_HEIGHT)
        apple_rect = pygame.Rect(x, y, SNAKE_SIZE, SNAKE_SIZE)  # replace with your apple's width and height

        # Check for collision with snake
        if apple_rect.colliderect(head_rect):  # replace with your snake's rect
            continue

        # Check for collision with sprites
        if any(apple_rect.colliderect(sprite_rect) for sprite_rect in colision_sprites.values()):
            continue

        return (x, y, SNAKE_SIZE, SNAKE_SIZE)
    
def game_over_conditions():
    return(
        any(head_rect.colliderect(sprite_rect) for sprite_rect in colision_sprites.values()) or
        #(head_coord in body_coords) or
        (head_rect.top < MIN_PLAYABLE_HEIGHT) or
        (head_rect.bottom > MAX_PLAYABLE_HEIGHT) or
        (head_rect.left < MIN_PLAYABLE_WIDTH) or
        (head_rect.right > MAX_PLAYABLE_WIDTH)
        )

#endregion

#region - The main game loop

pygame.mixer.music.play(-1, 0)

running = True
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
        
        #Move the snake
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake_dx == 0: #só podemos virar para a esquerda se a cobra estiver indo para cima ou para baixo
                snake_dx = -SNAKE_VELOCITY
                snake_dy = 0
            if event.key == pygame.K_RIGHT and snake_dx == 0: #só podemos virar para a esquerda se a cobra estiver indo para cima ou para baixo
                snake_dx = SNAKE_VELOCITY
                snake_dy = 0
            if event.key == pygame.K_UP and snake_dy == 0: #só podemos virar para a esquerda se a cobra estiver indo para cima ou para baixo
                snake_dx = 0
                snake_dy = -SNAKE_VELOCITY
            if event.key == pygame.K_DOWN and snake_dy == 0: #só podemos virar para a esquerda se a cobra estiver indo para cima ou para baixo
                snake_dx = 0
                snake_dy = SNAKE_VELOCITY

    #Update the body position
    body_coords.insert(0, head_coord)   #coloca a coordenada da cabeça como primeiro elemento da lista
    body_coords.pop()                   #elimina o ultimo bloco da cobrinha 


    #region - Game Over
    if game_over_conditions():
        
        pygame.mixer.music.stop()
        game_over_sound.play()
        game_over = True
        body_coords.clear()
        display_surface.blit(background, background_rect)
        display_surface.blit(game_over_text,game_over_rect)
        display_surface.blit(continue_text,continue_rect)
        pygame.display.update()

        while game_over:
            for event in pygame.event.get():
                if ((event.key == pygame.K_ESCAPE) or (event.type == pygame.QUIT)):
                    game_over = False
                    running = False
                elif event.type == pygame.KEYDOWN:
                    head_x = 600
                    head_y = 550
                    snake_dx = 0
                    snake_dy = 0
                    score = START_SCORE
                    pygame.mixer.music.play(-1, 0)
                    game_over = False
    #endregion

    #Update the x,y position of the snake head
    head_x += snake_dx
    head_y += snake_dy
    head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)

    #Check for colisions
    #Collision with apple
    if head_rect.colliderect(apple_rect):
        score += 1
        eat_sound.play()
        apple_coord = generate_apple_coordinates()
        body_coords.append(head_coord)

    #Update HUD
    display_surface.blit(background, background_rect)
    display_surface.blit(title_text, title_rect)

    score_text = score_font.render('Score:' + str(score) , True, GREEN)
    display_surface.blit(score_text, score_rect)

    #Blit assets
    for body in body_coords:
        pygame.draw.rect(display_surface, DARKGREEN, body)
    
    head_rect = pygame.draw.rect(display_surface, (0,0,0), head_coord)
    apple_rect = pygame.draw.rect(display_surface, RED, apple_coord)


    create_invisible_colisions()
    pygame.display.update()
    clock.tick(FPS)

#endregion
            
pygame.quit()
