from lib2to3 import pygram
from pickle import FALSE
from tkinter import CENTER
import pygame
from Ajustes import *
from Entidad import entidades

class Jugador(entidades):
    def __init__(self,pos,grupos,obstaculos,atacar,magia):
        super().__init__(grupos)
        self.image = pygame.image.load("./Grafico/player/0.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-26)


        self.estado = "abajo"
        self.animaciondent = 0
        self.velocidadanimacion = 0.30
        self.direccion = pygame.math.Vector2()
        self.ataque = False
        self.ataqueesp = 400
        self.ataquetiempo = None
        self.sw = 0
        self.atacar = atacar
        self.magia = magia

        self.estadisticas = {"vida": 100,"energia": 60, "ataque": 30,"magia":60,"velocidad":10}
        self.vida = self.estadisticas["vida"] * 0.5
        self.energia = self.estadisticas["energia"] * 0.4
        self.xp = 400
        self.velocidad = self.estadisticas["velocidad"]

        self.obstaculos = obstaculos

    def input(self):
        teclas = pygame.key.get_pressed()
        if self.ataque == False:
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
                if(self.sw <= 15):
                    self.image = pygame.image.load("./Grafico/player/derecha/1.png").convert_alpha()
                if self.sw >= 5 :
                    self.image = pygame.image.load("./Grafico/player/derecha/2.png").convert_alpha()
                if self.sw >= 10:
                    self.image = pygame.image.load("./Grafico/player/derecha/3.png").convert_alpha()
                if self.sw >= 15:
                    self.image = pygame.image.load("./Grafico/player/derecha/4.png").convert_alpha()
                    self.sw=0
            elif teclas[pygame.K_LEFT]:
                self.direccion.x = -1
                self.estado = "izquierda"
                self.sw = self.sw + 1
                if(self.sw <= 15):
                    self.image = pygame.image.load("./Grafico/player/izquierda/1.png").convert_alpha()
                if self.sw >= 5 :
                    self.image = pygame.image.load("./Grafico/player/izquierda/2.png").convert_alpha()
                if self.sw >= 10:
                    self.image = pygame.image.load("./Grafico/player/izquierda/3.png").convert_alpha()
                if self.sw >= 15:
                    self.image = pygame.image.load("./Grafico/player/izquierda/4.png").convert_alpha()
                    self.sw=0
            else:
                self.direccion.x = 0

            #Teclas de ataque
            if teclas[pygame.K_SPACE] and not self.ataque:
                self.ataque = True
                self.tiempoataque = pygame.time.get_ticks()
                if self.estado == "derecha":
                    self.image = pygame.image.load("./Grafico/player/ataque/1.png").convert_alpha()
                if self.estado == "derecha_idel":
                    self.image = pygame.image.load("./Grafico/player/ataque/1.png").convert_alpha()
                if self.estado == "izquierda":
                    self.image = pygame.image.load("./Grafico/player/ataque/1.png").convert_alpha()
                if self.estado == "izquierda_idel":
                    self.image = pygame.image.load("./Grafico/player/ataque/1.png").convert_alpha()
                if self.estado == "arriba":
                    self.image = pygame.image.load("./Grafico/player/ataque/1.png").convert_alpha()
                if self.estado == "arriba_idel":
                    self.image = pygame.image.load("./Grafico/player/ataque/1.png").convert_alpha()
                if self.estado == "abajo":
                    self.image = pygame.image.load("./Grafico/player/ataque/1.png").convert_alpha()
                if self.estado == "abajo_idel":
                    self.image = pygame.image.load("./Grafico/player/ataque/1.png").convert_alpha()
                self.atacar()
                

            if teclas[pygame.K_f] and not self.ataque:
                self.ataque = True
                self.tiempoataque = pygame.time.get_ticks()
                print("Magia")
                self.magia()


            #Animacion Idel

            #Transformaciones
            if teclas[pygame.K_k]:
                print("transformacion")
                self.image = pygame.image.load("./Grafico/test/rock.png").convert_alpha()

            if teclas[pygame.K_j]:
                self.image = pygame.image.load("./Grafico/test/player.png").convert_alpha()
            
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


    def update(self):
        self.input()
        self.espera()
        self.estados()
        self.move(self.velocidad)
