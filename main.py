import pygame
pygame.init()

###setting up window###

x = 0 #initialise x
y = 0 #initialise y

width = 40 #size of rect
height = 40 #size of rect

winx = 500
winy = 300
win = pygame.display.set_mode((winx,winy))
pygame.display.set_caption("Improved Game")

##basic graphics setup###

bg = pygame.image.load("Images/background.png")
bg = pygame.transform.scale(bg,(winx,winy))

ship = pygame.image.load("Images/mario.png")
ship = pygame.transfom.scale(ship,(width,height))

###positioning the rect in the middle###