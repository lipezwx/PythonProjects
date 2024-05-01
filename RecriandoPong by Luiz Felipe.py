import pygame, sys, random

#Variable declaration
player_speed = 0
opponent_speed = 7


#Ball movement
def ballAnimation():
    global ball_speed_x, ball_speed_y

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ballRestart()

    #Collisions
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def playerAnimation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponentAI():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def ballRestart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width / 2, screen_height / 2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))

#General Setup
pygame.init()
clock = pygame.time.Clock()

#Setting up the main window.
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

#Game Rectangle(Sprites)
ball = pygame.Rect(screen_width / 2 - 15,screen_height / 2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height / 2 - 70, 10, 140)

bg_color = pygame.Color(243, 247, 235)
purple = pygame.Color(81, 32, 145)

ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))

#Main loop
while True:
    #Handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:  #Interação com usuário, mover para baixo
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:  #Interação com usuário, mover para cima
            if event.key == pygame.K_UP:
                player_speed += 7
            if event.key == pygame.K_DOWN:
                player_speed -= 7
    
    ballAnimation()
    playerAnimation()
    opponentAI()

    #Visuals
    screen.fill(bg_color)

    pygame.draw.rect(screen, purple, player)
    pygame.draw.rect(screen, purple, opponent)
    pygame.draw.ellipse(screen, purple, ball)
    pygame.draw.aaline(screen, purple, (screen_width / 2, 0), (screen_width / 2, screen_height))



    #Updating the window
    pygame.display.flip()
    clock.tick(60)