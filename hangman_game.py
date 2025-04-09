import pygame
pygame.init()

#window
width, height = 800,600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("The Hangman Quiz Game")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

screen.fill((0, 0, 0))

pygame.display.flip()