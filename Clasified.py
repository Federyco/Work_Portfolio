import subprocess
import pygame, sys
from pygame import mixer


pygame.init()
pygame.display.init()
pygame.display.set_caption("Secret Level")
# contienen el tamaño de la pantalla
global display_width
display_width = 728
global display_height
display_height = 520
#clock
clock = pygame.time.Clock()
# creacion de la pantalla de juego
global screen
screen_main_menu = pygame.display.set_mode((display_width,display_height), pygame.RESIZABLE)
# boleano que maneja el inicio y fin del juego
main_menu_on = True
# Icono
icon = pygame.image.load('images/lupa-32x32.png')
pygame.display.set_icon(icon)
# fondo pantalla
background_bloques = pygame.image.load('images/fondo_bloques.jpg')
# bloques
bloques = pygame.image.load('images/bloque.png')
#play button
play_button = pygame.image.load('images/Button_Start.png')
stop_button = pygame.image.load('images/Button_Stop.png')

# botones
sound1 = pygame.mixer.Sound('Music/sound1.wav')
sound2 = pygame.mixer.Sound('Music/sound2.wav')
sound3 = pygame.mixer.Sound('Music/sound3.wav')
sound4 = pygame.mixer.Sound('Music/sound4.wav')

def dibujo_main_menu():
    screen_main_menu.blit(background_bloques,(0,0))

mov=int(52)
def construccion_matriz_visual():
    global mov
    n_arriba=int(0)
    n_abajo=int(52)
    n_izq=int(52)
    n_derecha=int(52)
    #arriba
    for x in range(14):
        screen_main_menu.blit(bloques,(n_arriba,0))
        n_arriba= n_arriba + mov
        #abajo
        screen_main_menu.blit(bloques,(n_abajo,468))
        n_abajo= n_abajo + mov
    #izquierda
    for x in range(9):
        screen_main_menu.blit(bloques,(0,n_izq))
        n_izq = n_izq + mov
        # derecha
        screen_main_menu.blit(bloques,(676,n_derecha))
        n_derecha = n_derecha + mov
   

def botonera():
    # play_buttons
    screen_main_menu.blit(play_button,(36,35))
    screen_main_menu.blit(play_button,(420,35))
    screen_main_menu.blit(play_button,(420,250))
    screen_main_menu.blit(play_button,(36,250))
    # stop_button
    screen_main_menu.blit(stop_button,(195,100))
    
    
    


value_x=[128,200,515,586,128,199,509,588]
value_y=[128,208,134,203,349,410,350,413]
stop_x=[310,396]
stop_y=[215,309]

def where_i_click():
    global objeto
    global value_x
    global value_y
    whereImI = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if(event.type == pygame.MOUSEBUTTONDOWN and whereImI[0] >= stop_x[0] and whereImI[0] <= stop_x[1] and whereImI[1] >= stop_y[0] and whereImI[1] <= stop_y[1]):
            sound1.stop()
            sound2.stop()
            sound3.stop()
            sound4.stop()  
        if(event.type == pygame.MOUSEBUTTONDOWN and whereImI[0] >= value_x[0] and whereImI[0] <= value_x[1] and whereImI[1] >= value_y[0] and whereImI[1] <= value_y[1]):
                sound1.play()
        if(event.type == pygame.MOUSEBUTTONDOWN and whereImI[0] >= value_x[2] and whereImI[0] <= value_x[3] and whereImI[1] >= value_y[2] and whereImI[1] <= value_y[3]):
                sound2.play()
        if(event.type == pygame.MOUSEBUTTONDOWN and whereImI[0] >= value_x[4] and whereImI[0] <= value_x[5] and whereImI[1] >= value_y[4] and whereImI[1] <= value_y[5]):
                sound3.play()
        if(event.type == pygame.MOUSEBUTTONDOWN and whereImI[0] >= value_x[6] and whereImI[0] <= value_x[7] and whereImI[1] >= value_y[6] and whereImI[1] <= value_y[7]):
                sound4.play()
        
        if(event.type == pygame.QUIT):
            special_move=0
            game_on = False #game_off   
            pygame.quit()
            sys.exit()
            

while main_menu_on:
    dibujo_main_menu()
    construccion_matriz_visual()
    where_i_click()
    botonera()
    pygame.display.update()
