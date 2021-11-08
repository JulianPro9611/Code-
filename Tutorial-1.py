# Please sub to the channel (https://www.youtube.com/channel/UC2BqQBtfd56WYXYVUF1Wx6Q) and like my vid (https://www.youtube.com/watch?v=Bhk4QdLRUVI)!!

# Steps to creating a window in pygame:
# 1. Importing pygame and initializing pygame (Note: It is needed for every pygame program.)
# 2. Setting up the screen (Note: It includes the size of the window, the color of the background, and the name.)
# 3. Setting up the game loop (Note: Without the game loop, the program would instantly close.)

# Step 1, We import pygame and start pygame!
import pygame # We import pygame!
pygame.init() # We initialize pygame!

# Step 2, We Set up the screen!
screen = pygame.display.set_mode((600, 600)) # We set the size of the screen!
pygame.display.set_caption('Tutorial 1') # We set the name of the program! (Note: The values are RGB, that is Red, Green, and Blue)
screen.fill((255,255,255)) # We set the background for our program!
pygame.display.flip() # We update the screen!

# Step 3, We set the game loop!
running = True # We set the value of the loop of our program!
while running: # We chech if running is true or false!
  for event in pygame.event.get(): # We check if we type something!
    if event.type == pygame.QUIT: # We check if we click the close button!
      running = False # We exit our program!

# Please sub to the channel (https://www.youtube.com/channel/UC2BqQBtfd56WYXYVUF1Wx6Q) and like my vid (https://www.youtube.com/watch?v=Bhk4QdLRUVI)!!
