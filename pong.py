import pygame
import random

pygame.init()

elementPair = 1
choice = int(input("Enter your choice: 1 for Smash and Flash and 2 for Ball Clone"))

if choice == 1:
    elementPair = 1
elif choice == 2:
    elementPair = 2

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
#Cloning Ball Postion and Movement
cloneBall_x = WIDTH/2 - radius
cloneBall_y = HEIGHT/2 - radius
cloneBallVelocityX = 1
cloneBallVelocityY = 1

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

#Smash Element Variables
leftSmashElement = 0
rightSmashElement = 0
leftSmashElementRemaining = 3
rightSmashElementRemaining = 3

#Flash Element Variables
leftFlashElement = 0
rightFlashElement = 0
leftFlashElementRemaining = 3
rightFlashElementRemaining = 3

#Clone Element Variable
leftCloneElement = 0
rightCloneElement = 0
leftCloneElementRemaining = 3
rightCloneElementRemaining = 3

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
            #Flash Element Activation Right Paddle
            # 
            if i.key == pygame.K_RIGHT and rightFlashElementRemaining > 0:
                rightFlashElement = 1
            #
    #Left Paddle
            if i.key == pygame.K_w:
                leftPaddleVelocity = -4
            if i.key == pygame.K_s:
                leftPaddleVelocity = 4
            #Smash Element Activiation
            if i.key == pygame.K_d and leftSmashElementRemaining > 0:
                leftSmashElement = 1
            #Flash Element Activation Left Paddle
            #
            if i.key == pygame.K_a and leftFlashElementRemaining > 0:
                leftFlashElement = 1
            #
        
        if i.type == pygame.KEYUP:
            rightPaddleVelocity = 0
            leftPaddleVelocity = 0

            
    #Ball movement controls
    #Create conditionals to check it the balls position is at y=0 or y=600
    if ball_y <= 0 + radius or ball_y >= HEIGHT - radius:
        ballVelocityY *= -1
    if cloneBall_y <= 0 + radius or cloneBall_y >= HEIGHT - radius:
        cloneBallVelocityY *= -1
    #Player turns
    if ball_x >= WIDTH - radius:
        ball_x = WIDTH/2 - radius
        ball_y = HEIGHT/2 - radius
        #Retrieve the position for the cloned ball
        cloneBall_x = WIDTH/2 - radius
        cloneBall_y = HEIGHT/2 - radius
        randomDirection = random.choice(direction)
        randomAngles = random.choice(angles)
        #Up Direction
        if randomDirection == 0:
            if randomAngles == 0:
                ballVelocityX = 0.7
                ballVelocityY = -1.4
                # Clone Ball Directions
                cloneBallVelocityX = 0.7
                cloneBallVelocityY = -1.4
            if randomAngles == 1:
                ballVelocityX = 0.7
                ballVelocityY = -0.7
                # Clone Ball Direction
                cloneBallVelocityX = 0.7
                cloneBallallVelocityY = -0.7
            if randomAngles == 2:
                ballVelocityX = 1.4
                ballVelocityY = -0.7
                # Clone Ball Direction
                cloneBallVelocityX = 1.4
                cloneBallallVelocityY = -0.7
        #Down Direction
        if randomDirection == 1:
            if randomAngles == 0:
                ballVelocityX = 0.7
                ballVelocityY = 1.4
                # Clone Ball Direction
                cloneBallVelocityX = 0.7
                cloneBallVelocityY = 1.4
            if randomAngles == 1:
                ballVelocityX = 0.7
                ballVelocityY = 0.7
                # Clone Ball Direction
                cloneBallVelocityX = 0.7
                cloneBallVelocityY = 0.7
            if randomAngles == 2:
                ballVelocityX = 1.4
                ballVelocityY = 0.7
                # Clone Ball Direction
                cloneBallVelocityX = 1.4
                cloneBallVelocityY = 0.7
        ballVelocityX *= -1
        # Change the direction of the clone ball
        cloneBallVelocityX *= -1

    if ball_x <= 0 + radius:
        ball_x = WIDTH/2 - radius
        ball_y = HEIGHT/2 - radius
        #Clone Ball
        cloneBall_x = WIDTH/2 - radius
        cloneBall_y = HEIGHT/2 - radius
        randomDirection = random.choice(direction)
        randomAngles = random.choice(angles)
        #Up Direction
        if randomDirection == 0:
            if randomAngles == 0:
                ballVelocityX = 0.7
                ballVelocityY = -1.4
                #Clone
                cloneBallVelocityX = 0.7
                cloneBallVelocityY = -1.4
            if randomAngles == 1:
                ballVelocityX = 0.7
                ballVelocityY = -1
                #Clone
                cloneBallVelocityX = 0.7
                cloneBallVelocityY = -1
            if randomAngles == 2:
                ballVelocityX = 1.4
                ballVelocityY = -0.7
                #Clone
                cloneBallVelocityX = 1.4
                cloneBallVelocityY = -0.7
        #Down Direction
        if randomDirection == 1:
            if randomAngles == 0:
                ballVelocityX = 0.7
                ballVelocityY = 1.4
                #Clone
                cloneBallVelocityX = 0.7
                cloneBallVelocityY = 1.4
            if randomAngles == 1:
                ballVelocityX = 0.7
                ballVelocityY = 0.7
                #Clone
                cloneBallVelocityX = 0.7
                cloneBallVelocityY = 0.7
            if randomAngles == 2:
                ballVelocityX = 1.4
                ballVelocityY = 0.7
                #Clone
                cloneBallVelocityX = 1.4
                cloneBallVelocityY = 0.7
    #Paddle Movement Controls
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
            cloneBall_x = leftPaddleX + paddleWidth
            ballVelocityX *= -1
            cloneBallVelocityX *= -1

    #Right Paddle Collision
    if rightPaddleX <= ball_x <= rightPaddleX + paddleWidth:
        if rightPaddleY <= ball_y <= rightPaddleY + paddleHeight:
            ball_x = rightPaddleX
            cloneBall_x = rightPaddleX  
            ballVelocityX *= -1
            cloneBallVelocityX *= -1
    
    #Smash Element Active For Left Paddle
    if leftSmashElement == 1:
        if leftPaddleX <= ball_x <= leftPaddleX + paddleWidth:
            if leftPaddleY <= ball_y <= leftPaddleY + paddleHeight:
                ball_x = leftPaddleX + paddleWidth
                ballVelocityX *= -3.5
                cloneBallVelocityX *= -3.5
                leftSmashElement = 0
                leftSmashElementRemaining -= 1
    #Flash Element Active For Left Paddle
    if leftFlashElement == 1:
        leftPaddleY = ball_y - paddleHeight // 2
        leftFlashElement = 0
        leftFlashElementRemaining -= 1
    #
    #

    #Smash Element Active For Right Paddle 
    if elementPair == 1:
        if rightSmashElement == 1:
            if rightPaddleX <= ball_x <= rightPaddleX + paddleWidth:
                if rightPaddleY <= ball_y <= rightPaddleY + paddleHeight:
                    ball_x = rightPaddleX 
                    ballVelocityX *= -3.5
                    cloneBallVelocityX *= -3.5
                    rightSmashElement = 0
                    leftSmashElementRemaining -= 1
        #Flash Element Active For Right Paddle
        if rightFlashElement == 1:
            leftPaddleY = ball_y - paddleHeight // 2
            rightFlashElement = 0
            rightFlashElementRemaining -= 1
        #
        #
        #
    elif elementPair == 2:
        if leftCloneElement == 1: 
            if leftPaddleX <= ball_x <= leftPaddleX + paddleWidth:
                if leftPaddleY <= ball_y <= leftPaddleY + paddleHeight:
                    ball_x = leftPaddleX + paddleWidth
                    loneBall_x = leftPaddleX + paddleWidth
                    ballVelocityX *= -1
                    cloneBallVelocityX *= -1
                    cloneBallVelocityY *= -1
                    leftCloneElement = 0
                    leftCloneElementRemaining -= 1

        if rightCloneElement == 1:
            if rightPaddleX <= ball_x <= rightPaddleX + paddleWidth:
                if rightPaddleY <= ball_y <= rightPaddleY + paddleHeight:
                    ball_x = rightPaddleX
                    cloneBall_x = rightPaddleX  
                    ballVelocityX *= -1
                    cloneBallVelocityX *= -1
                    cloneBallVelocityY *= -1
                    rightCloneElement = 0
                    rightCloneElementRemaining -= 1


        #Movement Section
        ball_x += ballVelocityX
        ball_y += ballVelocityY
        cloneBall_x += cloneBallVelocityX
        cloneBall_y += cloneBallVelocityY
        rightPaddleY += rightPaddleVelocity
        leftPaddleY += leftPaddleVelocity


    #Draw pygame objects with pygame.draw...
    #Draw Ball
    pygame.draw.circle(window, WHITE, (ball_x, ball_y), radius)
    #Draw Paddles
    pygame.draw.rect(window, WHITE, pygame.Rect(leftPaddleX, leftPaddleY, paddleWidth, paddleHeight))
    pygame.draw.rect(window, WHITE, pygame.Rect(rightPaddleX, rightPaddleY, paddleWidth, paddleHeight))
    #Draw Clone Ball
    pygame.draw.circle(window, WHITE, (cloneBall_x, cloneBall_y), radius)
    #Smash Element Indicator (little red circle on each paddle)
    if leftSmashElement == 1:
        pygame.draw.circle(window, RED, (leftPaddleX + 10, leftPaddleY + 10), 4)
    if rightSmashElement == 1:
        pygame.draw.circle(window, RED, (rightPaddleX + 10, rightPaddleY + 10), 4)    
    #To see ojects in the window we must update the display
    pygame.display.update()