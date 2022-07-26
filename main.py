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

    def draw(self, win):
        if self.walkCount + 1 > 27:
            self.walkCount = 0

        if self.left:
            win.blit(walkLeft[self.walkCount//3],(self.x,self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        else:
            win.blit(char,(self.x,self.y))

#define redraw game window function and animate character and work out the walking done by it#
def redrawGameWindow():

    win.blit(bg,(0,0))
    man.draw(win)
    static_man.draw(win)
    pygame.display.update()

run = True
###main loop###

man = player(200,410,64,64) #sets x,y,width height of player
static_man = player(400,410,64,64) #sets x,y,width,height of static fellow

while run:
    clock.tick(27)

    for event in pygame.event.get(): #quit if cross is clicked
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed() #get keypress, IMPORTANT for literally any game

    if keys[pygame.K_LEFT] and man.x > man.vel: #if x cannot move any further left then it wont move
        man.x -= man.vel
        man.left = True
        man.right = False

    elif keys[pygame.K_RIGHT] and man.x < 500 - man.vel - man.width: #if right side cant move any further right it wont move
        man.x += man.vel
        man.left = False
        man.right = True

    else: #idle statement
        man.left = False
        man.right = False
        man.walkCount = 0

    if not(man.isJump): #if not in air already
        if keys[pygame.K_SPACE]:
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