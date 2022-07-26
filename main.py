import pygame
pygame.init()

###setting up window###

win = pygame.display.set_mode((500,480))
pygame.display.set_caption("Improved Game")

###setting up animation and image loading###

walkRight = [pygame.image.load("images/R1.png"), pygame.image.load("images/R2.png"), pygame.image.load("images/R3.png"), pygame.image.load("images/R4.png"),
             pygame.image.load("images/R5.png"), pygame.image.load("images/R6.png"),
             pygame.image.load("images/R7.png"), pygame.image.load("images/R8.png"), pygame.image.load("images/R9.png")] #added animations for walking right
walkLeft = [pygame.image.load("images/L1.png"), pygame.image.load("images/L2.png"), pygame.image.load("images/L3.png"),
            pygame.image.load("images/L4.png"), pygame.image.load("images/L5.png"), pygame.image.load("images/L6.png"),
            pygame.image.load("images/L7.png"), pygame.image.load("images/L8.png"), pygame.image.load("images/L9.png")]#added animations for walking left
bg = pygame.image.load("images/bg.jpg")
char = pygame.image.load("images/standing.png")

clock =pygame.time.Clock()

###Classes###

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True

    def draw(self, win): #function for character animation and direction faced
        if self.walkCount + 1 > 27:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3],(self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3],(self.x,self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0],(self.x,self.y))
            else:
                win.blit(walkLeft[0],(self.x,self.y))


#class for bullets#
class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8*facing
    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)

#define redraw game window function and animate character and work out the walking done by it#
def redrawGameWindow():

    win.blit(bg,(0,0))
    man.draw(win)
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()


###main loop###
shootLoop = 0
man = player(200,410,64,64) #sets x,y,width height of player
bullets = []
run = True
while run:
    clock.tick(27)

    if shootLoop >= 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    for event in pygame.event.get(): #quit if cross is clicked
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel #moves bullet by its velocity
        else:
            bullets.pop(bullets.index(bullet)) #removes bullet off screen

    keys = pygame.key.get_pressed() #get keypress, IMPORTANT for literally any game

    if keys[pygame.K_SPACE] and shootLoop == 0:
        if man.left:
            facing = -1
        else:
            facing=1

        if len(bullets) < 5:
            bullets.append(projectile(round(man.x + man.width // 2), round(man.y + man.height//2), 6, (0,0,0),facing))

    if keys[pygame.K_LEFT] and man.x > man.vel: #if x cannot move any further left then it wont move
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False #so that man faces direction instead of facing us

    elif keys[pygame.K_RIGHT] and man.x < 500 - man.vel - man.width: #if right side cant move any further right it wont move
        man.x += man.vel
        man.left = False
        man.right = True
        man.standing = False

    else: #idle statement
        man.standing = True
        man.walkCount = 0

    if not(man.isJump): #if not in air already
        if keys[pygame.K_UP]:
            man.isJump = True #makes character jump
            man.left = False
            man.right = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10: #weird algorithm for making jump work smoothly
            man.y -= (man.jumpCount * abs(man.jumpCount)) * 0.5
            man.jumpCount -= 1
        else: #resets jump if nothing else added
            man.jumpCount = 10
            man.isJump = False

    redrawGameWindow()


pygame.quit()