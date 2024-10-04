import pygame
import random
pygame.init()

win_wid = 1200
win_ht = 800
screen = pygame.display.set_mode((win_wid,win_ht)) 

pygame.display.set_caption("GolaGoli in space")
icon = pygame.image.load("jet.png")
background = pygame.image.load("background.png")
pygame.display.set_icon(icon)

#ghost player
playerImage = pygame.image.load("JET.png")
playerImage = pygame.transform.scale(playerImage, (100, 100))
playerX = 500 #if value increase, image will move right direction
playerY = 650 #if value increase, image will move down direction

#monster enemy
enemyImage = pygame.image.load("spaceship.png")
enemyImage = pygame.transform.scale(enemyImage, (100, 100))
enemyX = 40   #random.randint(0, win_wid) 
enemyY = 100  #random.randint(0, win_ht) 

#bullet
bullet = pygame.image.load("computer.png")
bullet = pygame.transform.scale(bullet, (100,70))
bullet_X = 0
bullet_Y = playerY
bullet_Ychange = 10
bullet_state = "ready"


def player(x, y):
    screen.blit(playerImage, (x, y))

def enemy(x, y):
    screen.blit(enemyImage, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (x, y))        

running = True
while running:
    #RGB = Red, Blue, Green. You can choose it from 0 to 255
    screen.fill((0,0,0))
    screen.blit(background, (0,0))

    enemyX += 2
    if enemyX > win_wid:
        enemyX = 0
        enemyY += 5   
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #if keystroke is pressed, check whether its left or right
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
                bullet_X = playerX 
                bullet_Y = playerY 
                fire_bullet(bullet_X, bullet_Y)

    if bullet_state == "fire":
        fire_bullet(bullet_X, bullet_Y)
        bullet_Y -= bullet_Ychange

    if bullet_Y <= 0:
        bullet_Y = playerY
        bullet_state = "ready"                       

    player(playerX, playerY)
    enemy(enemyX, enemyY)

    pygame.display.update() 

print("Thanks for wasting time")
