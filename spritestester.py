import pygame
import random


BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (0, 255,0)


##class Block(pygame.sprite.Sprite):
##
##    # Constructor. Pass in the color of the block,
##    # and its x and y position
##    def __init__(self, color, width, height):
##       # Call the parent class (Sprite) constructor
##       pygame.sprite.Sprite.__init__(self)
##
##       # Create an image of the block, and fill it with a color.
##       # This could also be an image loaded from the disk.
##       self.image = pygame.Surface([width, height])
##       self.image.fill(color)
##
##       # Fetch the rectangle object that has the dimensions of the image
##       # Update the position of this object by setting the values of rect.x and rect.y
##       self.rect = self.image.get_rect()
##
##
##       # -- Methods
##    def __init__(self, x, y):
##        """Constructor function"""
##        # Call the parent's constructor
##        #super().__init__()
## 
##        # Set height, width
##        self.image = pygame.Surface([15, 15])
##        self.image.fill(BLACK)
## 
##        # Make our top-left corner the passed-in location.
##        self.rect = self.image.get_rect()
##        self.rect.x = x
##        self.rect.y = y
## 
##        # -- Attributes
##        # Set speed vector
##        self.change_x = 0
##        self.change_y = 0
## 
##    def changespeed(self, x, y):
##        """ Change the speed of the player"""
##        self.change_x += x
##        self.change_y += y
## 
##    def update(self):
##        """ Find a new position for the player"""
##        self.rect.x += self.change_x
##        self.rect.y += self.change_y
##
##        if self.rect.x > 685:
##            self.rect.x =685
##           
##        if self.rect.x <0 :
##            self.rect.x =0
##          
##        if self.rect.y > 385:
##            self.rect.y = 385
##          
##        if self.rect.y < 0:
##            self.rect.y =0


class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """
 
    # -- Methods
    def __init__(self, x, y):
        """Constructor function"""
        # Call the parent's constructor
        #super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(BLACK)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
        # -- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
 
    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y
 
    def update(self):
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        if self.rect.x > 685:
            self.rect.x =685
           
        if self.rect.x <0 :
            self.rect.x =0
           
        if self.rect.y > 385:
            self.rect.y = 385
          
        if self.rect.y < 0:
            self.rect.y =0
            
        








#initializing pygame
pygame.init()

# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])


block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()



# Create the player object
player = Player(50, 50)
all_sprites_list.add(player)


# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()




# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
 
        # Set the speed based on the key pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 3)
 
        # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -3)

      
 
    # Clear the screen
    screen.fill(WHITE)

     # This actually moves the player block based on the current speed
    player.update()
    # Draw all the spites
    all_sprites_list.draw(screen)
    all_sprites_list.update()

    screen.blit(text, [25, 25])
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)
 
pygame.quit()
