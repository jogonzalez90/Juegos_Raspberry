# -*- coding: utf-8 -*-
"""
Juego la serpiente
Elaborado el 14 de Enero de 2020

OJO para instalar la libreria pygame con el prompt de anaconda escribir 
pip install pygame

"""

import pygame, sys, time, random#Modulos pygame
from pygame.locals import *#Carga todas las instrucciones del modulo pygame

pygame.init()#Configura pygame
fpsClock = pygame.time.Clock()#Variable para controlar velocidad del juego

#Superficie de patalla para pygame
playSurface = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Arcade Serpiente')

#Definimos colores del programa
redColour = pygame.Color(255, 0, 0)
blackColour = pygame.Color(0, 0, 0)
whiteColour = pygame.Color(255, 255, 255)
greyColour = pygame.Color(150, 150, 150)

#Inicializacion de variables necesarias
snakePosition = [100,100]#Variable como lista
snakeSegments = [[100,100],[80,100],[60,100]]#Variable como lista para almacenar posicion de la serpiente
raspberryPosition = [300,300]#Variable como lista
raspberrySpawned = 1
direction = 'right'
changeDirection = direction

def gameOver():#Funcion fin del juego
    gameOverFont = pygame.font.Font('freesansbold.ttf', 72)
    gameOverSurf = gameOverFont.render('Game Over', True, greyColour)#Escribe game over en la pantalla
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.midtop = (320, 10)
    playSurface.blit(gameOverSurf, gameOverRect)
    pygame.display.flip()
    time.sleep(1.5)#Pausa de dos segundos
    pygame.quit()#Cerrar ventana
    sys.exit()#Salir de python
    
while True:#Bucle infinito
    for event in pygame.event.get():#For para comprobacion de teclas
        if event.type == QUIT:#Salir del programa al presionar ESC
            pygame.quit()#Cerrar ventana
            sys.exit()#Salir de python
        elif event.type == KEYDOWN:#Verifica eventos presionar teclas
            if event.key == K_RIGHT or event.key == ord('d'):#Flecha del cursor derecho o letra d
                changeDirection = 'right'#Modifica valor de la variable a derecha
            if event.key == K_LEFT or event.key == ord('a'):#Flecha del cursor izquierdo o letra a
                changeDirection = 'left'#Modifica valor de la variable a izquierda
            if event.key == K_UP or event.key == ord('w'):#Flecha del cursor arriba o letra w
                changeDirection = 'up'#Modifica valor de la variable arriba
            if event.key == K_DOWN or event.key == ord('s'):#Flecha del cursor abajo o letra s
                changeDirection = 'down'#Modifica valor de la variable abajo
            if event.key == K_ESCAPE:#con tecal ESC salir de juego
                pygame.event.post(pygame.event.Event(QUIT))
                
    #Comparaciones para evitar muerte de serpiente por ordenes contradictorias
    if changeDirection == 'right' and not direction == 'left':
        direction = changeDirection
    if changeDirection == 'left' and not direction == 'right':
        direction = changeDirection
    if changeDirection == 'up' and not direction == 'down':
        direction = changeDirection
    if changeDirection == 'down' and not direction == 'up':
        direction = changeDirection
        
    #Desplaza serpiente en cualquier direccion  
    if direction == 'right':
        snakePosition[0] += 20
    if direction == 'left':
        snakePosition[0] -= 20
    if direction == 'up':
        snakePosition[1] -= 20
    if direction == 'down':
        snakePosition[1] += 20
    snakeSegments.insert(0,list(snakePosition))#Instruccion para incrementar el cuerpo de la serpiente 
    if snakePosition[0] == raspberryPosition[0] and snakePosition[1] == raspberryPosition[1]:#Examina posicion cabeza y posicion frambuesa
        raspberrySpawned = 0#Establece variable a cero a ser ingerida la frambuesa
    else:
        snakeSegments.pop()#Elimina la cola de la serpiente
        
    #Crea una nueva frambuesa en el lienzo con ubicacion aleatoria al ser ingerida la frambuesa
    if raspberrySpawned == 0:
        x = random.randrange(1,32)
        y = random.randrange(1,24)
        raspberryPosition = [int(x*20),int(y*20)]#Multiplica por el tamaño de cada seccion de la serpiente
    raspberrySpawned = 1#Asegura que tan solo exista una frambuesa en el lienzo
    
    playSurface.fill(blackColour)#Rellena el fondo de la superficie de color negro
    for position in snakeSegments:
        pygame.draw.rect(playSurface,whiteColour,Rect(position[0], position[1], 20, 20))#Cabeza y segmentos de la serpiente color blanco
    pygame.draw.rect(playSurface,redColour,Rect(raspberryPosition[0], raspberryPosition[1], 20, 20))#Frambuesa color rojo
    pygame.display.flip()#Refresca pantalla o actualiza el lienzo
    
    #Escenarios muerte de la serpiente
    if snakePosition[0] > 620 or snakePosition[0] < 0:#Sale de superficie horizontal del juego
        gameOver()#Fin del juego
    if snakePosition[1] > 460 or snakePosition[1] < 0:#Sale de superficie vertical del juego
        gameOver()#Fin del juego
        
    #Muerte por impacto al cuerpo
    for snakeBody in snakeSegments[1:]:
        if snakePosition[0] == snakeBody[0] and snakePosition[1] == snakeBody[1]:
            gameOver()#Fin del juego
            
    fpsClock.tick(12)#Velocidad de la serpiente
