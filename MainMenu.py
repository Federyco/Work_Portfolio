import subprocess
import pygame, sys
import time
from datetime import datetime
from pygame import mixer


pygame.init()
pygame.display.set_caption("Main Menu")
# contienen el tamaño de la pantalla
global display_width
display_width = 1240
global display_height
display_height = 900
#clock
clock = pygame.time.Clock()
#relojito
relojito = time.strftime("%H %M %S")
# creacion de la pantalla de juego
global screen
screen_main_menu = pygame.display.set_mode((display_width,display_height), pygame.RESIZABLE)
# boleano que maneja el inicio y fin del juego
main_menu_on = True
# Icono
icon = pygame.image.load('images/lupa-32x32.png')
pygame.display.set_icon(icon)
# fondo pantalla
MainMenuBack = pygame.image.load('images/MainMenuBack.png')
secret_level=False


#musica
mixer.music.load('Music/Welcome home sir.wav')
mixer.music.play(-1)

def dibujo_main_menu():
    screen_main_menu.blit(MainMenuBack,(0,0))


puntaje_up= int(0)
def tecla_up():
    global puntaje_up
    puntaje_up = puntaje_up + 1
    
puntaje_down=int(0)
def tecla_down():
    global puntaje_down
    puntaje_down = puntaje_down + 1

puntaje_left=int(0)
def tecla_left():
    global puntaje_left
    puntaje_left = puntaje_left + 1

puntaje_right=int(0)
def tecla_right():
    global puntaje_right
    puntaje_right = puntaje_right + 1


def another_level():
    if (secret_level == True):
        game3= "Scripts/Clasified.exe"
        subprocess.Popen(game3)


    
imagenes_X= [1035, 1091, 693, 864, 702,890]
imagenes_Y= [364, 415, 740, 808, 839,895]
def where_i_click():
    global secret_level
    global puntaje_up
    global puntaje_down
    global puntaje_left
    global puntaje_right
    global special_move_1_X
    global special_move_1_Y
    whereImI = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_UP):
                tecla_up()
            if(event.key == pygame.K_DOWN):
                tecla_down()
            if(event.key == pygame.K_LEFT):
                tecla_left()
            if(event.key == pygame.K_RIGHT):
                tecla_right()
        if (event.type == pygame.MOUSEBUTTONDOWN and whereImI[1] >= imagenes_Y[0] and whereImI[1] <= imagenes_Y[1] and whereImI[0] >= imagenes_X[0] and whereImI[0] <= imagenes_X[1]):
            game_on = False #game_off
            pygame.quit()
            sys.exit()
        if (event.type == pygame.MOUSEBUTTONDOWN and whereImI[1] >= imagenes_Y[2] and whereImI[1] <= imagenes_Y[3] and whereImI[0] >= imagenes_X[2] and whereImI[0] <= imagenes_X[3]):
            game1= "Scripts/FindMe.exe"
            subprocess.Popen(game1)
        if (event.type == pygame.MOUSEBUTTONDOWN and whereImI[1] >= imagenes_Y[4] and whereImI[1] <= imagenes_Y[5] and whereImI[0] >= imagenes_X[4] and whereImI[0] <= imagenes_X[5]):
            game2= "Scripts/DiferenceMe.exe"
            subprocess.Popen(game2)
        
        if(event.type == pygame.QUIT):
            special_move=0
            game_on = False #game_off   
            pygame.quit()
            sys.exit()
        #if event.type == pygame.VIDEORESIZE:
          #      screen_main_menu = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
    ## special moves
    if(puntaje_up == 2 and puntaje_down == 2 and puntaje_left == 2 and puntaje_right == 2):
            secret_level=True
            

    
relojitoX= 828
relojitoY= 460
relojito_text=(45,200,107)
def relojito(x,y):
    now = datetime.now()
    font_size= 22
    font = pygame.font.Font("fonts/Carnevalee Freakshow.ttf", font_size)
    scores = font.render("%s:%s:%s" % (now.hour,now.minute,now.second), True, relojito_text)
    screen_main_menu.blit(scores, (x,y))     

while main_menu_on:
    dibujo_main_menu()
    where_i_click()
    if(secret_level == True):
        another_level()
        break
    else:
        secret_level = False
    relojito(relojitoX,relojitoY)
    pygame.display.update()
    
        


