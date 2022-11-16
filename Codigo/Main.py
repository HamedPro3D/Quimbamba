import pygame,sys
from Ajustes import *
from Debug import debug
from Nivel import Nivel

class Game:
    def __init__(self):
        

        pygame.init()
        self.pantalla = pygame.display.set_mode((Ancho,Largo))
        pygame.display.set_caption("wegito")
        self.frames = pygame.time.Clock()

        self.nivel = Nivel()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.pantalla.fill('blue')
            self.nivel.run()
        # debug(pygame.mouse.get_pos())
        # debug(pygame.mouse.get_pressed(),40,0)
        # debug("Mouse track",pygame.mouse.get_pos()[1],pygame.mouse.get_pos()[0])
            pygame.display.update()
            self.frames.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()
