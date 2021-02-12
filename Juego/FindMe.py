import pygame, sys
from pygame import mixer

# inicializando el pygame
pygame.init()
# titulo de pantalla
pygame.display.set_caption("Find Me")
# contienen el tamaño de la pantalla
global display_width
display_width = 1240
global display_height
display_height = 900
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
background = pygame.image.load('images/Background.png')
# Musica
mixer.music.load('Music/muse_algorithm.wav')
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

textX= 1070
textY= 10
black_text=(0,0,0)
#funcion que muestra el score en pantalla
def show_score(x,y):
     scores = font.render("Score: " + str(score_actual), True, black_text)
     screen.blit(scores, (x,y))

objetos= [ True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
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
def enable_object_9():
     if(objetos[9] == True):
          objetos[9] = False
     if(objetos[9] == False):
          return objetos[9]
def enable_object_10():
     if(objetos[10] == True):
          objetos[10] = False
     if(objetos[10] == False):
          return objetos[10]
def enable_object_11():
     if(objetos[11] == True):
          objetos[11] = False
     if(objetos[11] == False):
          return objetos[11]
def enable_object_12():
     if(objetos[12] == True):
          objetos[12] = False
     if(objetos[12] == False):
          return objetos[12]
def enable_object_13():
     if(objetos[13] == True):
          objetos[13] = False
     if(objetos[13] == False):
          return objetos[13]
def enable_object_14():
     if(objetos[14] == True):
          objetos[14] = False
     if(objetos[14] == False):
          return objetos[14]


font_size_win= 37
textX_win = 120
textY_win = 430
black_text_win=(0,0,0)
font_win = pygame.font.Font("fonts/SuperMario256.ttf", font_size_win)
def show_win_msg(x,y):
     win_msg = font_win.render("Has encontrado los 15 Objetos, Felicitaciones! ", True, black_text_win)
     screen.blit(win_msg, (x,y))

     
def you_win(value):
     if(int(value) == 15):
          show_win_msg(textX_win,textY_win)

          
situar_imagen_X=[40,160,259,367,457,532,608,690,710,820,900,980,980,1076,1158]
situar_imagen_Y=[770,770,770,770,770,770,770,740,790,770,770,720,810,770,780]
def situar_imagen(x,y):
     imagen_situada = pygame.image.load('images/marcador_objetos.png')     
     screen.blit(imagen_situada, (x,y))

     
     
imagenes_X= [1031, 1234, 389, 472, 429,480,674,777,550,596,747,804,727,757,10,66,149,243,751,844,590,653,996,1045,410,471,1080,1148,789,823]
imagenes_Y= [558, 735, 133,223, 226,308, 476,521,430,451,136,198,285,330,612,637,663,707,566,638,126,223,421,466,427,456,302,349,18,47]
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
          if (event.type == pygame.MOUSEBUTTONDOWN and whereImI[1] >= imagenes_Y[18] and whereImI[1] <= imagenes_Y[19] and whereImI[0] >= imagenes_X[18] and whereImI[0] <= imagenes_X[19]):         
               if(objetos[9] == True):
                    enable_object_9()    
                    score()
                    you_win(score_actual)
          if (event.type == pygame.MOUSEBUTTONDOWN and whereImI[1] >= imagenes_Y[20] and whereImI[1] <= imagenes_Y[21] and whereImI[0] >= imagenes_X[20] and whereImI[0] <= imagenes_X[21]):         
               if(objetos[10] == True):
                    enable_object_10()    
                    score()
                    you_win(score_actual)
          if (event.type == pygame.MOUSEBUTTONDOWN and whereImI[1] >= imagenes_Y[22] and whereImI[1] <= imagenes_Y[23] and whereImI[0] >= imagenes_X[22] and whereImI[0] <= imagenes_X[23]):         
               if(objetos[11] == True):
                    enable_object_11()    
                    score()
                    you_win(score_actual)
          if (event.type == pygame.MOUSEBUTTONDOWN and whereImI[1] >= imagenes_Y[24] and whereImI[1] <= imagenes_Y[25] and whereImI[0] >= imagenes_X[24] and whereImI[0] <= imagenes_X[25]):         
               if(objetos[12] == True):
                    enable_object_12()    
                    score()
                    you_win(score_actual)
          if (event.type == pygame.MOUSEBUTTONDOWN and whereImI[1] >= imagenes_Y[26] and whereImI[1] <= imagenes_Y[27] and whereImI[0] >= imagenes_X[26] and whereImI[0] <= imagenes_X[27]):         
               if(objetos[13] == True):
                    enable_object_13()    
                    score()
                    you_win(score_actual)
          if (event.type == pygame.MOUSEBUTTONDOWN and whereImI[1] >= imagenes_Y[28] and whereImI[1] <= imagenes_Y[29] and whereImI[0] >= imagenes_X[28] and whereImI[0] <= imagenes_X[29]):         
               if(objetos[14] == True):
                    enable_object_14()    
                    score()
                    you_win(score_actual)          
          else:
               if event.type == pygame.QUIT:
                 game_on = False #game_off
                 pygame.quit()
                 sys.exit()

     if(int(score_actual) == 15):
          show_win_msg(textX_win,textY_win)
          mixer.music.fadeout(5000)
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
     if(objetos[9] == False):
          situar_imagen(situar_imagen_X[9],situar_imagen_Y[9])
     if(objetos[10] == False):
          situar_imagen(situar_imagen_X[10],situar_imagen_Y[10])
     if(objetos[11] == False):
          situar_imagen(situar_imagen_X[11],situar_imagen_Y[11])
     if(objetos[12] == False):
          situar_imagen(situar_imagen_X[12],situar_imagen_Y[12])
     if(objetos[13] == False):
          situar_imagen(situar_imagen_X[13],situar_imagen_Y[13])
     if(objetos[14] == False):
          situar_imagen(situar_imagen_X[14],situar_imagen_Y[14])
     
               

while game_on:
    dibujo_el_fondo()
    score_up()
    pygame.display.flip()
    

            
