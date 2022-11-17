import pygame
from Ajustes import *
from suelo import piso
from Jugador import Jugador
from Debug import debug
from Soporte import *
from random import *
from Armas import Arma
from Magia import Magia
from Estadisticas import Stats
from Enemigos import enemigo

class Nivel:
    def __init__(self):

        self.mostrars = pygame.display.get_surface()
        self.spritesv = YCamaraGrupo()
        self.obstaculos = pygame.sprite.Group()
        self.ataqueactual = None
        self.spritesataque = pygame.sprite.Group()
        self.spritesataqueenemigos = pygame.sprite.Group()

        

        self.crearmapa()

        self.stats = Stats()

    def crearmapa(self):
        layouts = {
            'boundary': import_csv_layout("./Mapa/map_FloorBlocks.csv"),
            "grass": import_csv_layout("./Mapa/map_Grass.csv"),
            "objetos": import_csv_layout("./Mapa/map_Objects.csv"),
            "entities": import_csv_layout("./Mapa/map_Entities.csv")
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
                        piso((x,y),[self.spritesv,self.obstaculos,self.spritesataqueenemigos],"grass",random_grass_i)
                   if style == "objetos":
                        superficie = graphics["objeto"][int(col)]
                        piso((x,y),[self.spritesv,self.obstaculos],"objeto",superficie)
                   if style == "entities":
                       if col == "394":
                           self.jugador = Jugador((900,985),[self.spritesv],self.obstaculos,self.atacar,self.magia)
                       else:
                           if col == "390":
                                nombrevariablemoustro = "bamboo"
                           if col == "391":
                                nombrevariablemoustro = "spirit"
                           elif col == "392":
                                nombrevariablemoustro = "raccoon"
                           elif col == "393":
                                nombrevariablemoustro = "squid"
                           enemigo(nombrevariablemoustro,(x,y),[self.spritesv,self.spritesataqueenemigos],self.obstaculos)
            #    if col == "x":
            #        piso((x,y),[self.spritesv,self.obstaculos])
             #   if col == "p":
        

    
    def atacar(self):
        self.ataqueactual = Arma(self.jugador,["",self.spritesataque])
    
    def magia(self):
        self.ataqueactual = Magia(self.jugador,[self.spritesv,self.spritesataque])

    def logicaataquesp(self):
        if self.spritesataque:
            for spriteataque in self.spritesataque:
                colisionsprites = pygame.sprite.spritecollide(spriteataque,self.spritesataqueenemigos,False)
                if colisionsprites:
                    for objetivo in colisionsprites:
                        #objetivo.kill()
                        if objetivo.sprite_type == "grass":
                            objetivo.kill()
                        else:
                            objetivo.kill()

    def run(self):
        self.spritesv.custom_draw(self.jugador)
        self.spritesv.update()
        self.spritesv.actualizacionenemigo(self.jugador)
        self.stats.display(self.jugador)
        self.logicaataquesp()
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

    def actualizacionenemigo(self,jugador):
        spritesenemigos = [sprite for sprite in self.sprites() if hasattr(sprite,"sprite_type") and sprite.sprite_type == "enemy"]
        for enemigo in spritesenemigos:
            enemigo.actualizacionenemigos(jugador)