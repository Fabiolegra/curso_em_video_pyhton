import time
import pygame_sdl2

pygame_sdl2.import_as_pygame()
import pygame

pygame.init()
pygame.mixer.music.load('audio_(11).mp3')
pygame.mixer.music.play()
pygame.event.wait()
time.sleep(30)
