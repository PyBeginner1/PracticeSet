import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("SN")  # title
icon = pygame.image.load('mouth.png')
pygame.display.set_icon(icon)

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

def show_score(x,y):
    score = font.render("Score :" +str(score_value), True, (255,255,255))
    screen.blit(score, (x,y))


background = pygame.image.load('space.jpg')  # backgrnd img

playerImg = pygame.image.load('spacecraft.png')  # creating player
playerX = 370
playerY = 480
playerX_change = 0  # movement on pressing keys
playerY_change = 0

enemyImg = pygame.image.load('ufo.png')  # creating enemy
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 0.3
enemyY_change = 40

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480                               # 480 because playerY=480(bullet comin top off spaceship
bulletX_change = 0                             # no horizontal movement
bulletY_change = 1
bullet_state = "ready"                      # 2 states, ready - bullet not shot & fire - bullet shot


def player(x, y):
    screen.blit(playerImg, (x, y))          # bilt - draw image onto screen. (x,y) co-ords


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,
                (x + 16, y + 10))           # x+16 because space ship is 32px & bullet looks like its coming from centre of it


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:  # 27 px
        return True
    else:
        return False


running = True
while running:
    screen.fill((255, 0, 0))                # Red,Green,Blue  -Background colour
    screen.blit(background, (0, 0))         # adding background
    for win in pygame.event.get():          #    event.get() - stores any event like quit or keystrokes
        if win.type == pygame.QUIT:         #     quit or close event create
            running = False

        if win.type == pygame.KEYDOWN:      # keydown is pressing key
            if win.key == pygame.K_LEFT:
                playerX_change = -0.3
            if win.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if win.key == pygame.K_SPACE:
                if bullet_state == "ready":     # bullet cant be shot until it reaches the border
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

            if win.key == pygame.K_UP:      # dont need as we dont need vertical movement for the game
                playerY_change = -0.1
            if win.key == pygame.K_DOWN:
                playerY_change = 0.1

        if win.type == pygame.KEYUP:        # keyup is releasing key
            if win.key == pygame.K_LEFT or pygame.K_RIGHT or pygame.K_RIGHT or pygame.K_DOWN:
                playerX_change = 0
                playerY_change = 0
    playerX += playerX_change
    playerY += playerY_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        player = 736

    enemyX += enemyX_change                 # enemy movement

    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change             # to move enemy downward after hitting border on either sides(x-coord)
    elif enemyX >= 736:
        enemyX_change = -0.3
        enemyY += enemyY_change

    if bulletY <= 0:            # <0 because after being shot the bullet travels outside the border forever so with 480 it will reset to space ship
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score_value += 1
        enemyX = random.randint(0, 800)         # respawns enemy
        enemyY = random.randint(50, 150)

    player(playerX, playerY)
    show_score(textX,textY)
    enemy(enemyX, enemyY)
    pygame.display.update()
