import pygame

class entidades(pygame.sprite.Sprite):
    def __init__(self, grupos):
        super().__init__(grupos)
        self.framesi = 0
        self.animacionv = 0.15
        self.direccion = pygame.math.Vector2()

    def move(self,velocidad):
        if self.direccion.magnitude() != 0:
            self.direccion = self.direccion.normalize()

        self.hitbox.x += self.direccion.x * velocidad
        self.colision('horizontal')
        self.hitbox.y += self.direccion.y * velocidad
        self.colision('vertical')
        self.rect.center = self.hitbox.center


    def colision(self,direccion):
        if direccion == 'horizontal':
            for sprite in self.obstaculos:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direccion.x > 0:
                        self.hitbox.right = sprite.hitbox.left
                    if self.direccion.x < 0:
                        self.hitbox.left = sprite.hitbox.right

        if direccion == 'vertical':
            for sprite in self.obstaculos:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direccion.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direccion.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom