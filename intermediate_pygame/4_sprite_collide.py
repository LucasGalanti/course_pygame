import pygame
import random

#Initialize pygame
pygame.init()

#Set display surface
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Sprite Groups!')

#Set FPS clock
FPS = 60
clock = pygame.time.Clock()

#Define Classes

class Player(pygame.sprite.Sprite):
    """A simple class to represent a player who fights monsters"""
    def __init__(self, x, y, enemies):
        super().__init__()
        self.image = pygame.image.load("intermediate_pygame/knight.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.velocity = 5

        self.enemies = enemies
    
    def update(self):
         """Update the player"""
         self.move()
         self.check_collisions()
         
    def move(self):
        """Move the player"""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.velocity
        if keys[pygame.K_UP]:
            self.rect.y -= self.velocity
        if keys[pygame.K_DOWN]:
            self.rect.y += self.velocity
        
    def check_collisions(self):
        """Check for collisions between player (self) and the monster group"""
        if pygame.sprite.spritecollide(self, self.enemies, dokill= True):
            #dokill = true makes the monster collided to 
            print(len(self.enemies))

         

class Monster(pygame.sprite.Sprite):
    #pygame.sprite.Sprite is going to be the super class or the parent class
    """A simple class to represent a spooky monster"""
    def __init__(self, x, y):
            super().__init__()
            self.image = pygame.image.load('intermediate_pygame/blue_monster.png')
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)

            self.velocity = random.randint(1, 10)
    
    def update(self):
         """Update and move the monster"""
         self.rect.y += self.velocity


#Create a monster group and add 10 monsters
monster_group = pygame.sprite.Group()
for i in range(10):
     monster = Monster(i*64, 10) #giving x and y 
     monster_group.add(monster)


#Create a player group and add a player
player_group = pygame.sprite.Group()
player = Player(500,500, enemies = monster_group)
player_group.add(player)



#Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Fill the display
    display_surface.fill((0,0,0))

    #Update and Draw assets

    monster_group.update()
    monster_group.draw(display_surface)

    player_group.update()
    player_group.draw(display_surface)

    #update the display and tick the clock
    pygame.display.update()
    clock.tick(FPS)

#End the game
pygame.quit()