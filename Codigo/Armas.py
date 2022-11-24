import pygame
from Jugador import *

class Arma(pygame.sprite.Sprite):
    
    def __init__(self,jugador,grupos):
        super().__init__(grupos)

        self.image = pygame.Surface((40,40))

        if jugador.estado == "derecha":
            self.rect = self.image.get_rect(midleft = jugador.rect.midright)
            self.image = pygame.image.load("./Grafico/test/rock.png").convert_alpha()
        if jugador.estado == "derecha_idel":
            self.rect = self.image.get_rect(midleft = jugador.rect.midright)
            self.image = pygame.image.load("./Grafico/test/rock.png").convert_alpha()
        if jugador.estado == "izquierda":
            self.rect = self.image.get_rect(midright = jugador.rect.midleft)    
            self.image = pygame.image.load("./Grafico/test/rock.png").convert_alpha()
        if jugador.estado == "izquierda_idel":
            self.rect = self.image.get_rect(midright = jugador.rect.midleft)
            self.image = pygame.image.load("./Grafico/test/rock.png").convert_alpha() 
        if jugador.estado == "abajo":
            self.rect = self.image.get_rect(midtop = jugador.rect.midbottom)
            self.image = pygame.image.load("./Grafico/test/rock.png").convert_alpha()
        if jugador.estado == "abajo_idel":
            self.rect = self.image.get_rect(midtop = jugador.rect.midbottom)
            self.image = pygame.image.load("./Grafico/test/rock.png").convert_alpha()
        if jugador.estado == "arriba":
            self.rect = self.image.get_rect(midbottom = jugador.rect.midtop)
            self.image = pygame.image.load("./Grafico/test/rock.png").convert_alpha()
        if jugador.estado == "arriba_idel":
            self.rect = self.image.get_rect(midbottom = jugador.rect.midtop)
            self.image = pygame.image.load("./Grafico/test/rock.png").convert_alpha()
        print(jugador.estado)        
    #     self.rect = self.image.get_rect(center = jugador.rect.center)