import pygame
import random
import math
from pygame import mixer

pygame.init()

win_wid = 1200
win_ht = 800
score = 0

screen = pygame.display.set_mode((win_wid, win_ht))
icon = pygame.image.load("spaceship.png")
background = pygame.image.load("background.png")
mixer.music.load("battle.mp3")
mixer.music.play(-1)

pygame.display.set_caption("GolaGoli in space")
pygame.display.set_icon(icon)

# Player (ghost)
playerImage = pygame.image.load("JET.png")
playerImage = pygame.transform.scale(playerImage, (100, 100))
playerX = 500
playerY = 650

# Enemy (UFOs)
enemyImage = []
enemyX = []
enemyY = []
num_of_enemies = 3

# Load and scale enemy images
for i in range(num_of_enemies):
    enemyImage.append(pygame.transform.scale(pygame.image.load("ufo.png"), (100, 100)))
    enemyX.append(40)   # You can randomize this value for variety if you want
    enemyY.append(100)

# Bullet
bullet = pygame.image.load("computer.png")
bullet = pygame.transform.scale(bullet, (100, 70))
bullet_X = 0
bullet_Y = playerY
bullet_Ychange = 6
bullet_state = "ready"

font = pygame.font.Font('freesansbold.ttf', 32)
text_x = 10
text_y = 10


# Functions
def show_score(x, y):
    sc = font.render("Score: "+ str(score), True, (255, 255, 255))
    screen.blit(sc, (x, y))

def player(x, y):
    screen.blit(playerImage, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImage[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (x, y))

def isCollition(enemyX, enemyY, bullet_X, bullet_Y):
    distance = math.sqrt(math.pow(enemyX - bullet_X, 2) + math.pow(enemyY - bullet_Y, 2)) 
    return distance < 35  # If the distance is smaller than 35, collision happens

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for i in range(num_of_enemies):
        enemyX[i] += 2
        if enemyX[i] > win_wid:
            enemyX[i] = 0
            enemyY[i] += 5

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX -= 50
                if playerX < 0:
                    playerX = win_wid

            if event.key == pygame.K_RIGHT:
                playerX += 50
                if playerX > win_wid:
                    playerX = 0

            if event.key == pygame.K_UP:
                playerY -= 70
                if playerY < 0:
                    playerY = win_ht 

            if event.key == pygame.K_DOWN:
                playerY += 70 
                if playerY > win_ht:
                    playerY = 0 

            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_sound = mixer.Sound("missile_fire.mp3")
                bullet_sound.play()
                bullet_X = playerX 
                bullet_Y = playerY 
                fire_bullet(bullet_X, bullet_Y)

    if bullet_state == "fire":
        fire_bullet(bullet_X, bullet_Y)
        bullet_Y -= bullet_Ychange

    if bullet_Y <= 0:
        bullet_Y = playerY
        bullet_state = "ready"

    for i in range(num_of_enemies):
        collision = isCollition(enemyX[i], enemyY[i], bullet_X, bullet_Y)
        if collision:  # What will happen after collision
            bullet_Y = playerY
            blast = mixer.Sound("big_blast.mp3")
            blast.play()
            bullet_state = "ready"
            score += 1
            print(f"You hit {score} time!!")
            enemyX[i] = random.randint(1, win_wid - 100)
            enemyY[i] = random.randint(5, 400)

        enemy(enemyX[i], enemyY[i], i)

    player(playerX, playerY)
    show_score(text_x, text_y)
    pygame.display.update()

print(f"Your Score: {score}")
print("Thanks for wasting time")
