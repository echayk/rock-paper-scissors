import pygame
import random
import time
options = ["rock","paper","scissors"]
pygame.init()
#variables and constants
BGCOLOR = "#cccccc"
player_1 = ""
#initialize
screen = pygame.display.set_mode([800, 600])
#assets
rock_image = pygame.image.load("Assets/rock.png")
rock_image = pygame.transform.scale(rock_image,(200,200))
paper_image = pygame.image.load("Assets/paper.png")
paper_image = pygame.transform.scale(paper_image,(200,200))
scissors_image = pygame.image.load("Assets/scissors.png")
scissors_image = pygame.transform.scale(scissors_image,(200,200))
#object functions
def rpsWinner(player1, player2):
  winner = ""
  if player1 == 'rock':
    if player2 == 'paper':
      winner = "Computer"
    elif player2 == 'scissors':
      winner = "player one"
    else: 
      winner = "tie"
  elif player1 == 'paper':
    if player2 == 'scissors':
      winner = "Computer"
    elif player2 == 'rock':
      winner = "player one"
    else:
      winner = "tie"
  elif player1 == 'scissors':
    if player2 == 'rock':
      winner = "Computer"
    elif player2 == 'paper':
      winner = "player one"
  else:
    winner = "tie"
  return winner
def rock(x,y):
    screen.blit(rock_image,(x,y))
def paper(x,y):
    screen.blit(paper_image,(x,y))
def scissors(x,y):
    screen.blit(scissors_image,(x,y))
def player_choice(text):
    set_my_font = pygame.font.SysFont("arial",60)
    textSurface = set_my_font.render(text, True, "black")
    screen.blit(textSurface, (100, 300))
def computer_choice(text):
    set_my_font = pygame.font.SysFont("arial",60)
    textSurface = set_my_font.render(text, True, "black")
    screen.blit(textSurface, (100, 400))
def winner_display(text):
    set_my_font = pygame.font.SysFont("arial",60)
    textSurface = set_my_font.render(text, True, "black")
    screen.blit(textSurface, (100, 500))
active = True
while active:
    #get input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                player_1 = "Rock"
            if event.key == pygame.K_p:
                player_1 = "Paper"
            if event.key == pygame.K_s:
                player_1 = "Scissors"
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if mouse_x >= 100 and mouse_x <= 300 and mouse_y >= 100 and mouse_y <= 300:
                player_1 = "rock"
            if mouse_x >= 300 and mouse_x <= 500 and mouse_y >= 100 and mouse_y <= 300:
                player_1 = "paper"
            if mouse_x >= 500 and mouse_x <= 700 and mouse_y >= 100 and mouse_y <= 300:
                player_1 = "scissors"
    #process input

    #update game state
    screen.fill(BGCOLOR)
    rock(100,100)
    paper(300,100)
    scissors(500,100)
    if player_1 != "":
        player_choice("You selected " + player_1)
        player2 = random.choice(options)
        computer_choice("Computer selected " + player2)
        winner = rpsWinner(player_1,player2)
        winner_display(winner + " has won")
        pygame.display.update()
        pygame.time.wait(3000)
        player_1 = ""
        
        

    #draw screen
    pygame.display.flip()



pygame.quit()
