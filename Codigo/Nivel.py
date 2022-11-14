import pygame
from Ajustes import *
from suelo import piso
from Jugador import Jugador
from Debug import debug
from Soporte import *
from random import *

class Nivel:
    def __init__(self):

        self.mostrars = pygame.display.get_surface()
        self.spritesv = YCamaraGrupo()
        self.obstaculos = pygame.sprite.Group()

        self.crearmapa()

    def crearmapa(self):
        layouts = {
            'boundary': import_csv_layout("./Mapa/map_FloorBlocks.csv"),
            "grass": import_csv_layout("./Mapa/map_Grass.csv"),
            "objetos": import_csv_layout("./Mapa/map_Objects.csv")
        }
        graphics = {
            "grass" : import_folder("./Grafico/grass"),
            "objeto": import_folder("./Grafico/objects")
        }
        
        

        for style,layout in layouts.items():
            for row_index,row in enumerate(layout):
                for col_index, col in enumerate(row):
                  if col != '-1':
                   x  = col_index * TILESIZE
                   y = row_index * TILESIZE
                   if style == 'boundary':
                        piso((x,y),[self.obstaculos],'invisible')
                   if style == "grass":
                        random_grass_i = choice(graphics["grass"])
                        piso((x,y),[self.spritesv,self.obstaculos],"grass",random_grass_i)
                   if style == "objetos":
                        superficie = graphics["objeto"][int(col)]
                        piso((x,y),[self.spritesv,self.obstaculos],"objeto",superficie)
            #    if col == "x":
            #        piso((x,y),[self.spritesv,self.obstaculos])
             #   if col == "p":
        self.jugador = Jugador((900,985),[self.spritesv],self.obstaculos)

    


    def run(self):
        self.spritesv.custom_draw(self.jugador)
        self.spritesv.update()
        debug(self.jugador.estado)

class YCamaraGrupo(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.mostrars = pygame.display.get_surface()
        self.mitadancho = self.mostrars.get_size()[0]//2
        self.mitadlargo = self.mostrars.get_size()[1]//2
        self.offset = pygame.math.Vector2()


        self.suelo_superficie = pygame.image.load("./Grafico/tilemap/ground.png")
        self.suelo_rect = self.suelo_superficie.get_rect(topleft = (0,0))

    def custom_draw(self,jugador):

        self.offset.x =  jugador.rect.centerx - self.mitadancho
        self.offset.y = jugador.rect.centery - self.mitadlargo

        suelooffset_pos = self.suelo_rect.topleft - self.offset
        self.mostrars.blit(self.suelo_superficie,suelooffset_pos)

       # for sprite in self.sprites():
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offsetpos = sprite.rect.topleft - self.offset
            self.mostrars.blit(sprite.image,offsetpos)