from csv import reader
from os import walk
import py_compile

import pygame

def import_csv_layout(path):
    terreno_mapa = []
    with open(path) as nivel_mapa:
        layout = reader(nivel_mapa,delimiter= ',')
        for row in layout:
            terreno_mapa.append(list(row))
        return terreno_mapa


def import_folder(path):
    superficie_lista = []
    for _,__,archivoimagen in walk(path):
        for image in archivoimagen:
            todopath = path + "/" + image
            image_surf = pygame.image.load(todopath).convert_alpha()
            superficie_lista.append(image_surf)
    return superficie_lista




#print(import_csv_layout("./Mapa/map_FloorBlocks.csv"))