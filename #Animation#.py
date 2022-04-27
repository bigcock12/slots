#Animation#
import pygame
import time
screen = pygame.display.set_mode((600,400))
first_slot = pygame.image.load("7_slots.jpg")


while True:
    for i in range(1,100):
        screen.blit(first_slot, (100,i)) 
        pygame.time.wait(3)
        pygame.display.flip()
    screen.blit(first_slot, (100,100))
    pygame.display.flip()
    time.sleep(4) 

