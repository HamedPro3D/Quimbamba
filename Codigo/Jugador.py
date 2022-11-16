from lib2to3 import pygram
from pickle import FALSE
from tkinter import CENTER
import pygame
from Ajustes import *
from Soporte import import_folder


class Jugador(pygame.sprite.Sprite):
    def __init__(self,pos,grupos,obstaculos):
        super().__init__(grupos)
        self.image = pygame.image.load("./player/0.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-26)

        self.animaciones()
        self.estado = "abajo"
        self.animaciondent = 0
        self.velocidadanimacion = 0.30
        self.direccion = pygame.math.Vector2()
        self.velocidad = 10
        self.ataque = False
        self.ataqueesp = 400
        self.ataquetiempo = None
        self.sw = 0

        self.obstaculos = obstaculos

    def animaciones(self):
        ubicacionp = "./player/"
        self.animacionp = {"arriba": [], "abajo": [], "izquierda": [], "derecha": [], "arriba_idel": [],
            "abajo_idel": [],"izquierda_idel":[],"derecha_idel":[] }
        
        for animacion in self.animacionp.keys():
            todopath = ubicacionp + animacion
            self.animacionp[animacion] = import_folder(todopath)
        print(self.animacionp)

        
    def input(self):
        teclas = pygame.key.get_pressed()

        #Teclas de movimiento:

        if teclas[pygame.K_UP]:
            self.direccion.y = -1
            self.estado = "arriba"
        elif teclas[pygame.K_DOWN]:
            self.direccion.y = 1
            self.estado = "abajo"
        else:
            self.direccion.y = 0
        if teclas[pygame.K_RIGHT]:
            self.direccion.x = 1
            self.estado = "derecha"
            self.sw = self.sw + 1
            print(self.sw)
            if(self.sw <= 10):
                self.image = pygame.image.load("./player/derecha/1.png").convert_alpha()
                print("fem")
                self.sw=self.sw + 1
            if self.sw >= 8 :
                self.image = pygame.image.load("./player/derecha/2.png").convert_alpha()
            if self.sw >= 10:
                self.image = pygame.image.load("./player/derecha/3.png").convert_alpha()
                self.sw=0
        elif teclas[pygame.K_LEFT]:
            self.direccion.x = -1
            self.estado = "izquierda"
            self.sw = self.sw + 1
            print(self.sw)
            if(self.sw <= 10):
                self.image = pygame.image.load("./player/izquierda/1.png").convert_alpha()
                print("fem")
                self.sw=self.sw + 1
            if self.sw >= 8 :
                self.image = pygame.image.load("./player/izquierda/2.png").convert_alpha()
            if self.sw >= 10:
                self.image = pygame.image.load("./player/izquierda/3.png").convert_alpha()
                self.sw=0
        else:
            self.direccion.x = 0

        #Teclas de ataque
        if teclas[pygame.K_SPACE] and not self.ataque:
            self.ataque = True
            self.tiempoataque = pygame.time.get_ticks()
            print("Ataque")
            

        if teclas[pygame.K_f] and not self.ataque:
            self.ataque = True
            self.tiempoataque = pygame.time.get_ticks()
            print("Cuchillo")


        #Animacion Idel

        #Transformaciones
        if teclas[pygame.K_k]:
            print("transformacion")
            self.image = pygame.image.load("./test/rock.png").convert_alpha()

        if teclas[pygame.K_j]:
            self.image = pygame.image.load("./test/player.png").convert_alpha()

    def estados(self):
        #Idel
        if self.direccion.x == 0 and self.direccion.y == 0:
            if not "idel" in self.estado and not "ataque" in self.estado:
                self.estado = self.estado + "_idel"
        if self.ataque:
            self.direccion.x = 0
            self.direccion.y = 0
            if not "ataque" in self.estado:
                self.estado = self.estado + "_ataque"

    def move(self,velocidad):
        if self.direccion.magnitude() != 0:
            self.direccion = self.direccion.normalize()

        self.hitbox.x += self.direccion.x * velocidad
        self.colision("horizontal")
        self.hitbox.y += self.direccion.y * velocidad
        self.colision("vertical")
        self.rect.center = self.hitbox.center

    def espera(self):
        tiempoactual = pygame.time.get_ticks()

        if self.ataque:
            if tiempoactual - self.tiempoataque >= self.ataqueesp:
                self.ataque = False

    def secuencia(self):
        animacion = self.animaciones[self.estado]
        
        self.animaciondent += self.velocidadanimacion
        if self.animaciondent >= len(animacion):
            self.animaciondent = 0

        self.image = animacion[int(self.animaciondent)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

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
        self.espera()
        self.estados()
        self.move(self.velocidad)
