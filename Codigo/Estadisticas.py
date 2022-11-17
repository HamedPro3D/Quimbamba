import pygame
from Ajustes import *

class Stats:
    def __init__(self):
        self.mostrars = pygame.display.get_surface()
        self.font = pygame.font.Font(ubicacion,tamañofuente)

        self.tamañobarravida = pygame.Rect(1010,10,anchovida,alturavida)
        self.tamañobarraenergia = pygame.Rect(1100,40,anchobarraenergia,alturavida)

         
    
    def mostrarbarra(self,actual,maximo,cuadrotrasero,color):
        pygame.draw.rect(self.mostrars,"black",cuadrotrasero)

        ratestadisticas = actual/maximo
        tamañoactual = cuadrotrasero.width * ratestadisticas
        rectanguloactcual= cuadrotrasero.copy()
        rectanguloactcual.width= tamañoactual

        pygame.draw.rect(self.mostrars,color,rectanguloactcual)

    def mostrarexperiencia(self,xp):
        texto = self.font.render(str(int(xp)),False,"black")
        x = self.mostrars.get_size()[0] - 20
        y = self.mostrars.get_size()[1] - 20
        textorect = texto.get_rect(bottomright = (x,y))

        self.mostrars.blit(texto,textorect)

    def display(self,jugador):
        self.mostrarbarra(jugador.vida,jugador.estadisticas["vida"],self.tamañobarravida,"red")
        self.mostrarbarra(jugador.energia,jugador.estadisticas["energia"],self.tamañobarraenergia,"blue")

        self.mostrarexperiencia(jugador.xp)