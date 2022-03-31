
#3coding=utf-8
'''
Proyecto creado el 16 de enero de 2020
Por Johans Gonzalez
Encuentre las diferencias
'''


# importa la librería Pygame

import pygame

def main():
    # inicializa Pygame
    pygame.init()

    screen = pygame.display.set_mode((640, 480))#Creacion de pantalla
    pygame.display.set_caption('Encuentre las diferencias')

    #Preparamos la imagen de la diferencia
    difference = pygame.image.load('banana.jpg')
    difference = pygame.transform.scale(difference, (640, 480))#Escalamos imagen

    #Musica primera imagen
    sonido = pygame.mixer.Sound('tunes.wav')

    sonido.play()

    #Blitting mostrar imagen en patalla
    screen.blit(difference, (0,0))#Copia imagen en pantalla
    pygame.display.update()#Refrescamos pantalla

    # bucle infinito
    while True:
        pygame.init()
        # obtiene un solo evento de la cola de eventos
        event = pygame.event.wait()

        # si se presiona el botón 'cerrar' de la ventana
        if event.type == pygame.QUIT:
            # detiene la aplicación
            pygame.quit()

        # si algún botón del mouse es presionado
        if event.type == pygame.MOUSEBUTTONDOWN:
            #Preparamos Imagen zoobie
            sonido.stop()#Detenemos reproduccion
            zombie = pygame.image.load('terror.jpg')
            zombie = pygame.transform.scale (zombie, (640, 480))#Escalamos imagen
    
            #Reproduce sonido
            scream = pygame.mixer.Sound('scream.wav')
            scream.play()
    
            #Montar imagen Zombie en pantalla y actualizar
            screen.blit(zombie, (0,0))
            pygame.display.update()
    
if __name__ == '__main__':
    main()