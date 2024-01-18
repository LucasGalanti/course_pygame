import pygame

pygame.init()

#SET DISPLAY
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Adding Sounds')

#Load Sound Effects
sound_1 = pygame.mixer.Sound('basic_pygame/basic_tutorial_assets/basic_tutorial_assets/sound_1.wav')
sound_2 = pygame.mixer.Sound('basic_pygame/basic_tutorial_assets/basic_tutorial_assets/sound_2.wav')

#Play the sound effect
sound_1.play()

pygame.time.delay(2000)

sound_2.play()

pygame.time.delay(2000)

#Change the volume of a sound effect

sound_2.set_volume(0.1)
sound_2.play()

#Load background music
pygame.mixer.music.load('basic_pygame/basic_tutorial_assets/basic_tutorial_assets/music.wav')

#Play and stop the music
pygame.mixer.music.play(
    -1, #loop infinite
    0.0 #start at 0
    )
pygame.time.delay(5000)
pygame.mixer.music.stop()


#Set game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


#Quit game
pygame.quit()