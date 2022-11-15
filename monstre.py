import pygame
import animation
class monstre(animation.Animation_player_rundroite):
    def __init__(self,x,y,player):
        super().__init__("run-monstre")
        self.player = player
        self.sprite_sheet = pygame.image.load("Assets/monstre/monstre_0.png")
        self.image = self.get_image(0,0)
        self.image.set_colorkey(0,0)
        self.rect = self.image.get_rect()
        self.position = [x,y]
        self.box = pygame.Rect(0,0, self.rect.width * 0.5,5)
        self.old_position = self.position.copy()
        self.pv_max = 100
        self.pv = 100
        self.vitesse = 1.75
    # Le monstre se déplace selon les coordonnées du joueur
    def avancer(self):
        self.active_animation()
        self.animate2()
        if self.player.position[0] < self.position[0] and self.player.position[1] < self.position[1]:
            self.position[0] -= self.vitesse
            self.position[1] -= self.vitesse
            if self.box.colliderect(self.player):
                    self.player.pv -= 0.3
                    monstre.vitesse = 0
        elif self.player.position[0] > self.position[0] and self.player.position[1] > self.position[1]:
             self.position[0] += self.vitesse
             self.position[1] += self.vitesse
             if self.box.colliderect(self.player):
                    self.player.pv -= 0.3
                    monstre.vitesse = 0
        elif self.player.position[0] > self.position[0]:
            self.position[0] += self.vitesse
            if self.box.colliderect(self.player):
                    self.player.pv -= 0.3
                    monstre.vitesse = 0
        elif self.player.position[0] < self.position[0]:
            self.position[0] -= self.vitesse
            if self.box.colliderect(self.player):
                    self.player.pv -= 0.3
                    monstre.vitesse = 0
        elif self.player.position[1] > self.position[1]:
            self.position[1] += self.vitesse
            if self.box.colliderect(self.player):
                    self.player.pv -= 0.3
                    monstre.vitesse = 0
        elif self.player.position[1] < self.position[1]:
            self.position[1] -= self.vitesse
            if self.box.colliderect(self.player):
                    self.player.pv -= 0.3
                    monstre.vitesse = 0
    def get_image(self,x,y):
        image = pygame.Surface([32,32])
        image.blit(self.sprite_sheet, (0,0),(x,y, 32, 32))
        return image
    def update(self):
        self.rect.topleft = self.position
        self.box.midbottom = self.rect.midbottom
    def retour_arriere(self):
        pass
# --------------------------------------------------------------------------- Boss------------------------------------------------------   
