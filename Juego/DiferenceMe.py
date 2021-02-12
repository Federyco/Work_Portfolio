import pygame, sys
from pygame import mixer

# inicializando el pygame
pygame.init()
# titulo de pantalla
pygame.display.set_caption("Find Me")
# contienen el tamaño de la pantalla
global display_width
display_width = 728
global display_height
display_height = 974
# creacion de la pantalla de juego
global screen
screen = pygame.display.set_mode((display_width,display_height))
# si quiero full screen asi es
#screen = pygame.display.set_mode((display_width,display_height), pygame.FULLSCREEN)
# reloj
clock = pygame.time.Clock()
# boleano que maneja el inicio y fin del juego
game_on = True

# Icono
icon = pygame.image.load('images/lupa-32x32.png')
pygame.display.set_icon(icon)
# fondo pantalla
background = pygame.image.load('images/DiferenceMe.png')
# Musica
mixer.music.load('Music/Master_History.wav')
mixer.music.play(-1)

global mouse
mouse = pygame.mouse.get_pos()


click_derecho = pygame.mouse.get_pressed()


def dibujo_el_fondo():
     screen.blit(background, (0,0))


score_actual = int(0)
def score():
     global score_actual
     score_actual = score_actual + 1

font_size= 32
font = pygame.font.Font("fonts/Carnevalee Freakshow.ttf", font_size)

textX= 18
textY= 415

black_text=(220,220,109)
#funcion que muestra el score en pantalla
def show_score(x,y):
     scores = font.render("Score: " + str(score_actual), True, black_text)
     screen.blit(scores, (x,y))

objetos= [ True, True, True, True, True, True, True, True, True]
def enable_object_0():    
     global objetos
     if(objetos[0] == True):
          objetos[0] = False
     if(objetos[0] == False):
          return objetos[0]
def enable_object_1():    
     if(objetos[1] == True):
          objetos[1] = False
     if(objetos[1] == False):
          return objetos[1]
def enable_object_2():   
     if(objetos[2] == True):
          objetos[2] = False
     if(objetos[2] == False):
          return objetos[2]
def enable_object_3():   
     if(objetos[3] == True):
          objetos[3] = False
     if(objetos[3] == False):
          return objetos[3]
def enable_object_4():   
     if(objetos[4] == True):
          objetos[4] = False
     if(objetos[4] == False):
          return objetos[4]
def enable_object_5():   
     if(objetos[5] == True):
          objetos[5] = False
     if(objetos[5] == False):
          return objetos[5]
def enable_object_6():
     if(objetos[6] == True):
          objetos[6] = False
     if(objetos[6] == False):
          return objetos[6]
def enable_object_7():
     if(objetos[7] == True):
          objetos[7] = False
     if(objetos[7] == False):
          return objetos[7]
def enable_object_8():
     if(objetos[8] == True):
          objetos[8] = False
     if(objetos[8] == False):
          return objetos[8]



font_size_win= 28
textX_win = 90
textY_win = 490
black_text_win=(54,155,45)
font_win = pygame.font.Font("fonts/Druid.ttf", font_size_win)
def show_win_msg(x,y):
     win_msg = font_win.render("Has encontrado las 9 Diferencias, Felicitaciones! ", True, black_text_win)
     screen.blit(win_msg, (x,y))

     
def you_win(value):
     if(int(value) == 9):
          show_win_msg(textX_win,textY_win)

          
situar_imagen_X=[308,323,276,450,485,602,643,648,598]
situar_imagen_Y=[55,203,407,241,275,290,358,438,90]
def situar_imagen(x,y):
     imagen_situada = pygame.image.load('images/encontrado.png')     
     screen.blit(imagen_situada, (x,y))

     
     
imagenes_X= [316, 355, 338, 361, 287,324,458,496,498,522,614,643,659,675,662,686,603,651]
imagenes_Y= [61, 102, 217,234, 426,451, 250,279,291,314,312,320,382,399,461,468,103,131]
def score_up():
     global imagenes_X
     global imagenes_Y
     show_score(textX,textY)
     whereImI = pygame.mouse.get_pos()
     for event in pygame.event.get():
          # si el evento registrado es un click en la zona, suma 1
          if (event.type == pygame.MOUSEBUTTONDOWN and whereImI[1] >= imagenes_Y[0] and whereImI[1] <= imagenes_Y[1] and whereImI[0] >= imagenes_X[0] and whereImI[0] <= imagenes_X[1]):
               situar_imagen(situar_imagen_X[0],situar_imagen_Y[0])
               if(objetos[0] == True):
                    enable_object_0()    
                    score()
                    you_win(score_actual)                    
          if (event.type == pygame.MOUSEBUTTONDOWN and whereImI[1] >= imagenes_Y[2] and whereImI[1] <= imagenes_Y[3] and whereImI[0] >= imagenes_X[2] and whereImI[0] <= imagenes_X[3]):         
               if(objetos[1] == True):
                    enable_object_1()    
                    score()
                    you_win(score_actual)
          if (event.type == pygame.MOUSEBUTTONDOWN and whereImI[1] >= imagenes_Y[4] and whereImI[1] <= imagenes_Y[5] and whereImI[0] >= imagenes_X[4] and whereImI[0] <= imagenes_X[5]):         
               if(objetos[2] == True):
                    enable_object_2()    
                    score()
                    you_win(score_actual)
          if (event.type == pygame.MOUSEBUTTONDOWN and whereImI[1] >= imagenes_Y[6] and whereImI[1] <= imagenes_Y[7] and whereImI[0] >= imagenes_X[6] and whereImI[0] <= imagenes_X[7]):         
               if(objetos[3] == True):
                    enable_object_3()    
                    score()
                    you_win(score_actual)
          if (event.type == pygame.MOUSEBUTTONDOWN and whereImI[1] >= imagenes_Y[8] and whereImI[1] <= imagenes_Y[9] and whereImI[0] >= imagenes_X[8] and whereImI[0] <= imagenes_X[9]):         
               if(objetos[4] == True):
                    enable_object_4()    
                    score()
                    you_win(score_actual)
          if (event.type == pygame.MOUSEBUTTONDOWN and whereImI[1] >= imagenes_Y[10] and whereImI[1] <= imagenes_Y[11] and whereImI[0] >= imagenes_X[10] and whereImI[0] <= imagenes_X[11]):         
               if(objetos[5] == True):
                    enable_object_5()    
                    score()
                    you_win(score_actual)
          if (event.type == pygame.MOUSEBUTTONDOWN and whereImI[1] >= imagenes_Y[12] and whereImI[1] <= imagenes_Y[13] and whereImI[0] >= imagenes_X[12] and whereImI[0] <= imagenes_X[13]):         
               if(objetos[6] == True):
                    enable_object_6()    
                    score()
                    you_win(score_actual)
          if (event.type == pygame.MOUSEBUTTONDOWN and whereImI[1] >= imagenes_Y[14] and whereImI[1] <= imagenes_Y[15] and whereImI[0] >= imagenes_X[14] and whereImI[0] <= imagenes_X[15]):         
               if(objetos[7] == True):
                    enable_object_7()    
                    score()
                    you_win(score_actual)
          if (event.type == pygame.MOUSEBUTTONDOWN and whereImI[1] >= imagenes_Y[16] and whereImI[1] <= imagenes_Y[17] and whereImI[0] >= imagenes_X[16] and whereImI[0] <= imagenes_X[17]):         
               if(objetos[8] == True):
                    enable_object_8()    
                    score()
                    you_win(score_actual)
          else:
               if event.type == pygame.QUIT:
                 game_on = False #game_off
                 pygame.quit()
                 sys.exit()

     if(int(score_actual) == 9):
          show_win_msg(textX_win,textY_win)
          mixer.music.fadeout(10000)
     if(objetos[0] == False):
          situar_imagen(situar_imagen_X[0],situar_imagen_Y[0])
     if(objetos[1] == False):
          situar_imagen(situar_imagen_X[1],situar_imagen_Y[1])
     if(objetos[2] == False):
          situar_imagen(situar_imagen_X[2],situar_imagen_Y[2])
     if(objetos[3] == False):
          situar_imagen(situar_imagen_X[3],situar_imagen_Y[3])
     if(objetos[4] == False):
          situar_imagen(situar_imagen_X[4],situar_imagen_Y[4])
     if(objetos[5] == False):
          situar_imagen(situar_imagen_X[5],situar_imagen_Y[5])
     if(objetos[6] == False):
          situar_imagen(situar_imagen_X[6],situar_imagen_Y[6])
     if(objetos[7] == False):
          situar_imagen(situar_imagen_X[7],situar_imagen_Y[7])
     if(objetos[8] == False):
          situar_imagen(situar_imagen_X[8],situar_imagen_Y[8])
     
     
               

while game_on:
    dibujo_el_fondo()
    score_up()
    pygame.display.flip()
