import pygame

pygame.init()


#Initial window
WIDTH, HEIGHT = 1000, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
#Change the pygame window name
pygame.display.set_caption("Pongg")

run = True 

#Ball Color
WHITE = (255,255,255)
#Ball ReDraw
BLACK = (0,0,0)
#Ball Position on window
radius = 15
ball_x = WIDTH/2 - radius
ball_y = HEIGHT/2 - radius
#Ball Movement
ballVelocityX = 3
ballVelocityY = 3

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
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                rightPaddleVelocity = -4
            if i.key == pygame.K_DOWN:
                rightPaddleVelocity = 4
            if i.key == pygame.K_w:
                leftPaddleVelocity = -4
            if i.key == pygame.K_s:
                leftPaddleVelocity = 4
        
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
        ballVelocityX *= -1
        ballVelocityY *= -1
    if ball_x <= 0 + radius:
        ball_x = WIDTH/2 - radius
        ball_y = HEIGHT/2 - radius
        ballVelocityX = 2
        ballVelocityY = 2
    #Movement Section
    ball_x += ballVelocityX
    ball_y += ballVelocityY
    rightPaddleY += rightPaddleVelocity
    leftPaddleY += leftPaddleVelocity

    #Paddle Movement Restrictions
    if leftPaddleY >= HEIGHT - paddleHeight:
        leftPaddleY >= HEIGHT - paddleHeight
        
    #Draw pygame objects with pygame.draw...
    #Draw Ball
    pygame.draw.circle(window, WHITE, (ball_x, ball_y), radius)
    #Draw Paddles
    pygame.draw.rect(window, WHITE, pygame.Rect(leftPaddleX, leftPaddleY, paddleWidth, paddleHeight))
    pygame.draw.rect(window, WHITE, pygame.Rect(rightPaddleX, rightPaddleY, paddleWidth, paddleHeight))
    #To see ojects in the window we must update the display
    pygame.display.update()