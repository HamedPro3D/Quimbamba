import pygame
from Ajustes import *
from Entidad import entidades
from Soporte import *

class enemigo(entidades):
    def __init__(self,nombremoustro,pos,grupos,obstaculos):
        super().__init__(grupos)
        self.sprite_type = "enemy"

        self.importargraficos(nombremoustro)
        self.estado = "idle"
        self.image = self.animaciones[self.estado][self.framesi]

        self.rect = self.image.get_rect(topleft= pos)
        self.hitbox = self.rect.inflate(0,-10)
        self.obstaculos = obstaculos

        self.nombremoustro = nombremoustro
        moustroinfo = informacionmosutros[self.nombremoustro]
        self.vida = moustroinfo["vida"]
        self.xp = moustroinfo["xp"]
        self.velocidad = moustroinfo["velocidad"]
        self.daño = moustroinfo["daño"]
        self.resistencia = moustroinfo["resistencia"]
        self.radioataque = moustroinfo["radioataque"]
        self.deteccion = moustroinfo["deteccion"]
        self.tipo = moustroinfo["tipoataque"]

        self.puedeatacar = True
        self.tiempoataque = None
        self.esperaataque = 400
    
    def importargraficos(self,name):
        self.animaciones = {"idle":[],"move":[],"attack":[]}
        main_path = f"./Grafico/monsters/{name}/"
        for animacion in self.animaciones.keys():
            self.animaciones[animacion] = import_folder(main_path + animacion)

    def get_player_distance_direction(self,player):
                enemy_vec = pygame.math.Vector2(self.rect.center)
                player_vec = pygame.math.Vector2(player.rect.center)
                distance = (player_vec - enemy_vec).magnitude()
                if distance > 0:
                            direction = (player_vec - enemy_vec).normalize()
                else:
                    direction = pygame.math.Vector2()


                return (distance,direction)
		

    def tomarestado(self,jugador):
        distancia = self.get_player_distance_direction(jugador)[0]

        if distancia <= self.radioataque and self.puedeatacar == True:
            if self.estado != "attack":
                self.framesi = 0
            self.estado = "attack"
        elif distancia <= self.deteccion:
            self.estado = "move"
        else: 
            self.estado = "idle"

    def acciones(self,jugador):
        if self.estado == "attack":
            self.tiempoataque = pygame.time.get_ticks()
            print("atacando")
        elif self.estado == "move":
            self.direccion =self.get_player_distance_direction(jugador)[1]
        else:
            self.direccion = pygame.math.Vector2()

    def animacion(self):
        animacione = self.animaciones[self.estado]

        self.framesi += self.animacionv
        if self.framesi >= len(animacione):
            if self.estado == "attack":
                self.puedeatacar = False
            self.framesi = 0

        self.image = animacione[int(self.framesi)]
        self.rect = self.image.get_rect(center = self.hitbox.center)
            
    def esperaataques(self):
        if not self.puedeatacar:
            tiempoactual = pygame.time.get_ticks()
            if tiempoactual - self.tiempoataque >= self.esperaataque:
                self.puedeatacar = True

# def dañarse(jugador,atacado,self):
    #     if atacado:
    #         self.healt -= jugador.dañodelarma()
    #   else:
    #       pass
        
    
    def update(self):
        self.move(self.velocidad)
        self.animacion()
        self.esperaataques()
    
    def actualizacionenemigos(self,jugador):
        self.tomarestado(jugador)
        self.acciones(jugador)