import pygame
from sprites import SpriteSheet

###################################
### DEFINI LA PLATEFORME MOBILE ###
###################################

class MovingPlatform(SpriteSheet):

    change_x = 0
    change_y = 0
 
    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0
 
    player = None
    level = None

    def update(self):
 
        # Déplacement horizontal de la plateforme
        self.rect.x += self.change_x
 
        # Gestion de la collision avec le joueur (déplace le joueur)
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            if self.change_x < 0:
                self.player.rect.right = self.rect.left
            else:
                self.player.rect.left = self.rect.right
 
        # Déplacement vertical de la plateforme
        self.rect.y += self.change_y
 
        # Gestion de la collision avec le joueur (déplace le joueur)
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom
 
        # Inverse la direction de la plateforme
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1
 
        cur_pos = self.rect.x - self.level.world_shift_h
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1
