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
ship = pygame.transform.scale(ship,(width,height))

###positioning the rect in the middle###

###position the rect in the middle and at the bottom
x = 250 # position of the rect
y = 250 # position on y of rect

vel = 10 #velocity or attack value
jumpMax = 10 #set number of iterations for jump maths

isJump = False #routine for jump
jumpCount = jumpMax

###Begin of defining functions###

#screen refresh function#
def redrawGameWindow():
    win.blit(bg, (0,0))
    win.blit(ship,(x,y))
    pygame.display.update()

run = True

while run:
    pygame.time.delay(60) #setting game run speed

    for event in pygame.event.get(): #listen for events
        if event.type == pygame.QUIT: #quit
            run = False

    keys = pygame.key.get_pressed() #variable for keypress

    if keys[pygame.K_LEFT]: #add the   fucking x > vel here later dumbass
        x -= vel
        # if pressing left and position of rect is greater than velocity - movement speed in pixels
    if keys[pygame.K_RIGHT] and x < 500 - vel - width:
        x += vel
    if not(isJump):
        if keys[pygame.K_UP] and y > vel:
            y -= vel

        if keys[pygame.K_DOWN] and y < 500 - height - vel:
            y += vel

        if keys[pygame.K_SPACE]:
            isJump = True

    else:
        if jumpCount >= -jumpMax:
            y -= (jumpCount * abs(jumpCount))
            print("jump grav", y) #show the meth
            jumpCount -= 2
            print("rect position", (jumpCount - y))
        else:
            jumpCount = jumpMax
            isJump = False
    #win.fill((0,0,0))
    redrawGameWindow()
pygame.quit()