# We import pygame and start pygame!
import pygame # We import pygame!
pygame.init() # We initialize pygame!

# We Set up the screen!
screen = pygame.display.set_mode((600, 600)) # We set the size of the screen!
pygame.display.set_caption('Tutorial 1') # We set the name of the program!
screen.fill((255,255,255)) # We set the background for our program!
pygame.display.flip() # We update the screen!

# We set the game loop!
running = True # We set the value of the loop of our program!
while running: # We chech if running is true or false!
  for event in pygame.event.get(): # We check if we type something!
    if event.type == pygame.QUIT: # We check if we click the close button!
      running = False # We exit our program!