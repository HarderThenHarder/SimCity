import time
import pygame
from pygame.locals import *
from sys import exit

def time_steper():
    since = time.time()
    time.sleep(5)
    time_elapsed = time.time() - since
    print("{:.0f}m {:.0f}s".format(time_elapsed // 60, time_elapsed % 60))

pygame.init()
pygame.display.set_caption("SimCity v1.0")
screen = pygame.display.set_mode([100, 50])
clock = pygame.time.Clock()

tick_elapsed = 0
second = 0
minute = 0

while True:
    since = time.time()
    clock.tick(60)
    # screen.blit(background, (0, 0))
    screen.fill(color=(255, 255, 255))
    tick_elapsed += time.time() - since
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if tick_elapsed >= 1:
        tick_elapsed = 0
        second += 1
        print(second)



