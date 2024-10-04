import pygame

pygame.init()
screen = pygame.display.set_mode((1200,800)) 

pygame.display.set_caption("This is ki ami jani nah")
icon = pygame.image.load("ghost-costume.png")
pygame.display.set_icon(icon)

playerImage = pygame.image.load("ghost-costume.png")
playerX = 340 #if value increase, image will move right direction
playerY = 200 #if value increase, image will move down direction

def player(x, y):
    screen.blit(playerImage, (x, y))

running = True
while running:
    #RGB = Red, Blue, Green. You can choose it from 0 to 255
    screen.fill((255,255,0))
    #playerX += 5
    if playerX > 1200:
        playerX = -350
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #if keystroke is pressed, check whether its left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left arrow key is pressed")
                playerX -= 50
                if playerX < -400:
                    playerX = 1150
            if event.key == pygame.K_RIGHT:
                print("Right arrow key is pressed")  
                playerX += 50
                if playerX > 1200:
                    playerX = -350
            if event.key == pygame.K_UP:
                print("Top arrow key is pressed") 
                playerY -= 70
                if playerY < -500:
                    playerY = 850 
            if event.key == pygame.K_DOWN:
                print("Bottom arrow key is pressed") 
                playerY += 70 
                if playerY > 900:
                    playerY = -450       
    player(playerX, playerY)
    pygame.display.update()      
