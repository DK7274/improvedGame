import pygame
pygame.init()

###setting up window###

win = pygame.display.set_mode((500,480))
pygame.display.set_caption("Improved Game")

###setting up animation and image loading###

walkRight = [pygame.image.load("images/R1.png"), pygame.image.load("images/R2.png"), pygame.image.load("images/R3.png"), pygame.image.load("images/R4.png"),
             pygame.image.load("images/R5.png"), pygame.image.load("images/R6.png"),
             pygame.image.load("images/R7.png"), pygame.image.load("images/R8.png"), pygame.image.load("images/R9.png")]
walkLeft = [pygame.image.load("images/L1.png"), pygame.image.load("images/L2.png"), pygame.image.load("images/L3.png"),
            pygame.image.load("images/L4.png"), pygame.image.load("images/L5.png"), pygame.image.load("images/L6.png"),
            pygame.image.load("images/L7.png"), pygame.image.load("images/L8.png"), pygame.image.load("images/L9.png")]
bg = pygame.image.load("images/bg.jpg")
char = pygame.image.load("images/standing.png")

#various other variable setup#
x = 50
y = 400
width = 40
height = 60
vel = 5

clock =pygame.time.Clock()

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0

#define redraw game window function and animate character and work out the walking done by it#
def redrawGameWindow():
    global walkCount

    win.blit(bg,(0,0))
    if walkCount + 1 >= 27:
        walkCount = 0
    if left:
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3],(x,y))
        walkCount += 1
    else:
        win.blit(char,(x,y))
        walkCount = 0
    pygame.display.update()

run = True
###main loop###
while run:
    clock.tick(27)

    for event in pygame.event.get(): #quit if cross is clicked
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed() #get keypress, IMPORTANT for literally any game

    if keys[pygame.K_LEFT] and x > vel: #if x is
        x -= vel
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < 500 - vel - width:
        x += vel
        left = False
        right = True

    else:
        left = False
        right = False
        walkCount = 0

    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            right = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False

    redrawGameWindow()


pygame.quit()