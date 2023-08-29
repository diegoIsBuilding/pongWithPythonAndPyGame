import pygame
import random

pygame.init()


#Initial window
WIDTH, HEIGHT = 1000, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
#Change the pygame window name
pygame.display.set_caption("Pongg")
run = True 

#Ball Direction
direction = [0,1]
#Ball Angles 
angles = [0,1,2]
#Ball Color
WHITE = (255,255,255)
#Ball ReDraw
BLACK = (0,0,0)
#Smash Element Indicator
RED = (255,0,0)
#Ball Position on window
radius = 15
ball_x = WIDTH/2 - radius
ball_y = HEIGHT/2 - radius
#Ball Movement
ballVelocityX = 1
ballVelocityY = 1

#Paddle Positions and Dimensions 
paddleWidth = 20
paddleHeight = 120
#Left Paddle
leftPaddleX = 100 - paddleWidth/2
leftPaddleY = HEIGHT/2 - paddleHeight/2
#Right Paddle
rightPaddleX = WIDTH - (100 - paddleWidth/2)
rightPaddleY = HEIGHT/2 - paddleHeight/2
#Paddle Velocity
rightPaddleVelocity = 0
leftPaddleVelocity = 0

#Smash and Flash Element 
leftSmashElement = 0
rightSmashElement = 0
leftSmashElementRemaining = 3
rightSmashElementRemaining = 3


while run: 
    #Make the ball look like it is moving by removing the previous position and redrawing the new position
    window.fill(BLACK)
    #This stores all the events that the user inputs - example is the quite but 
    #Code below is main loop
    for i in pygame.event.get():
        print (i)
        if i.type == pygame.QUIT:
            run = False
    #Check keystrokes
    #Right paddles
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                rightPaddleVelocity = -4
            if i.key == pygame.K_DOWN:
                rightPaddleVelocity = 4
            #Smash Element Activation
            if i.key == pygame.K_RIGHT and rightSmashElementRemaining > 0:
                rightSmashElement = 1
            #Flash Element Activation
            if i.key == pygame.K_LEFT and rightSmashElementRemaining > 0:
                rightSmashElement == 2
    #Left Paddle
            if i.key == pygame.K_w:
                leftPaddleVelocity = -4
            if i.key == pygame.K_s:
                leftPaddleVelocity = 4
            #Smash Element Activiation
            if i.key == pygame.K_d and leftSmashElementRemaining > 0:
                leftSmashElement = 1
            #Flash Element Activation
            if i.key == pygame.K_a and leftSmashElementRemaining > 0:
                leftSmashElement == 2
        
        if i.type == pygame.KEYUP:
            rightPaddleVelocity = 0
            leftPaddleVelocity = 0

            
    #Ball movement controls
    #Create conditionals to check it the balls position is at y=0 or y=600
    if ball_y <= 0 + radius or ball_y >= HEIGHT - radius:
        ballVelocityY *= -1
    #Player turns
    if ball_x >= WIDTH - radius:
        ball_x = WIDTH/2 - radius
        ball_y = HEIGHT/2 - radius
        randomDirection = random.choice(direction)
        randomAngles = random.choice(angles)
        #Up Direction
        if randomDirection == 0:
            if randomAngles == 0:
                ballVelocityX = 1
                ballVelocityY = -1.5
            if randomAngles == 1:
                ballVelocityX = 1
                ballVelocityY = -1
            if randomAngles == 2:
                ballVelocityX = 1.5
                ballVelocityY = -1
        #Down Direction
        if randomDirection == 1:
            if randomAngles == 0:
                ballVelocityX = 1
                ballVelocityY = 1.5
            if randomAngles == 1:
                ballVelocityX = 1
                ballVelocityY = 1
            if randomAngles == 2:
                ballVelocityX = 1.5
                ballVelocityY = 1
        ballVelocityX *= -1

    if ball_x <= 0 + radius:
        ball_x = WIDTH/2 - radius
        ball_y = HEIGHT/2 - radius
        randomDirection = random.choice(direction)
        randomAngles = random.choice(angles)
        #Up Direction
        if randomDirection == 0:
            if randomAngles == 0:
                ballVelocityX = 1
                ballVelocityY = -1.5
            if randomAngles == 1:
                ballVelocityX = 1
                ballVelocityY = -1
            if randomAngles == 2:
                ballVelocityX = 1.5
                ballVelocityY = -1
        #Down Direction
        if randomDirection == 1:
            if randomAngles == 0:
                ballVelocityX = 1
                ballVelocityY = 1.5
            if randomAngles == 1:
                ballVelocityX = 1
                ballVelocityY = 1
            if randomAngles == 2:
                ballVelocityX = 1.5
                ballVelocityY = 1

    #Paddle Movement Restrictions
    if leftPaddleY >= HEIGHT - paddleHeight:
        leftPaddleY = HEIGHT - paddleHeight
    if leftPaddleY <= 0:
        leftPaddleY = 0
    if rightPaddleY >= HEIGHT - paddleHeight:
        rightPaddleY = HEIGHT - paddleHeight
    if rightPaddleY <= 0:
        rightPaddleY = 0
    
    #Left Paddle Collision
    if leftPaddleX <= ball_x <= leftPaddleX + paddleWidth:
        if leftPaddleY <= ball_y <= leftPaddleY + paddleHeight:
            ball_x = leftPaddleX + paddleWidth
            ballVelocityX *= -1

    #Right Paddle Collision
    if rightPaddleX <= ball_x <= rightPaddleX + paddleWidth:
        if rightPaddleY <= ball_y <= rightPaddleY + paddleHeight:
            ball_x = rightPaddleX 
            ballVelocityX *= -1
    
    #Smash Element Active
    if leftSmashElement == 1:
        if leftPaddleX <= ball_x <= leftPaddleX + paddleWidth:
            if leftPaddleY <= ball_y <= leftPaddleY + paddleHeight:
                ball_x = leftPaddleX + paddleWidth
                ballVelocityX *= -3.5
                leftSmashElement = 0
                leftSmashElementRemaining -= 1
    #Flash Element Active
    elif leftSmashElementRemaining == 2:
        leftPaddleY = ball_y
        leftSmashElement = 0
        leftSmashElementRemaining -= 1

    #Smash Element Active
    if rightSmashElement == 1:
        if rightPaddleX <= ball_x <= rightPaddleX + paddleWidth:
            if rightPaddleY <= ball_y <= rightPaddleY + paddleHeight:
                ball_x = rightPaddleX 
                ballVelocityX *= 3.5
                rightSmashElement = 0
                leftSmashElementRemaining -= 1
    #Flash Element Active
    elif rightSmashElementRemaining == 2:
        leftPaddleY = ball_y
        rightSmashElement = 0
        rightSmashElementRemaining -= 1
    #Movement Section
    ball_x += ballVelocityX
    ball_y += ballVelocityY
    rightPaddleY += rightPaddleVelocity
    leftPaddleY += leftPaddleVelocity


    #Draw pygame objects with pygame.draw...
    #Draw Ball
    pygame.draw.circle(window, WHITE, (ball_x, ball_y), radius)
    #Draw Paddles
    pygame.draw.rect(window, WHITE, pygame.Rect(leftPaddleX, leftPaddleY, paddleWidth, paddleHeight))
    pygame.draw.rect(window, WHITE, pygame.Rect(rightPaddleX, rightPaddleY, paddleWidth, paddleHeight))

    #Smash Element Indicator 
    if leftSmashElement == 1:
        pygame.draw.circle(window, RED, (leftPaddleX + 10, leftPaddleY + 10), 4)
    if rightSmashElement == 1:
        pygame.draw.circle(window, RED, (rightPaddleX + 10, rightPaddleY + 10), 4)    
    #To see ojects in the window we must update the display
    pygame.display.update()