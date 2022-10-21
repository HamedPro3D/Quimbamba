import pygame
from Ajustes import *

class Jugador(pygame.sprite.Sprite):
    def __init__(self,pos,grupos,obstaculos):
        super().__init__(grupos)
        self.image = pygame.image.load("./Grafico/test/player.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-26)

        self.direccion = pygame.math.Vector2()
        self.velocidad = 10

        self.obstaculos = obstaculos

    def input(self):
        teclas = pygame.key.get_pressed()

        #Input de movimiento:

        if teclas[pygame.K_UP]:
            self.direccion.y = -1
        elif teclas[pygame.K_DOWN]:
            self.direccion.y = 1
        else:
            self.direccion.y = 0

        if teclas[pygame.K_RIGHT]:
            self.direccion.x = 1
        elif teclas[pygame.K_LEFT]:
            self.direccion.x = -1
        else:
            self.direccion.x = 0

        #Input de ataque
        if teclas[pygame.K_SPACE]:
            print("Ataque")


        #Input Idel



    def move(self,velocidad):
        if self.direccion.magnitude() != 0:
            self.direccion = self.direccion.normalize()

        self.hitbox.x += self.direccion.x * velocidad
        self.colision("horizontal")
        self.hitbox.y += self.direccion.y * velocidad
        self.colision("vertical")
        self.rect.center = self.hitbox.center

    def colision(self,direccion):
        if direccion == "horizontal":
            for sprite in self.obstaculos:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direccion.x > 0:
                        self.hitbox.right = sprite.hitbox.left
                    if self.direccion.x < 0:
                        self.hitbox.left = sprite.hitbox.right

        if direccion == "vertical":
            for sprite in self.obstaculos:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direccion.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direccion.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom

    def update(self):
        self.input()
        self.move(self.velocidad)
