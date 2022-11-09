import pygame
"""
class balle(pygame.sprite.Sprite):
    def __init__(self,player):
        super().__init__()
        self.velocite = 6
        self.player = player
        self.image = pygame.image.load("Assets/balle.png")
        self.image = pygame.transform.scale(self.image,(20,20))
        self.rect = self.image.get_rect()
        self.box = pygame.Rect(0,0, self.rect.width * 0.5,5)
        self.rect.x = 455
        self.rect.y = 380
        
    def mouvement(self):
        self.rect.x += self.velocite
        if self.rect.x > 800:
            self.player.ballegr.remove(self)
        if self.player.game.monstre1.box.colliderect(self):
            self.player.ballegr.remove(self)
class balle1(pygame.sprite.Sprite):
    def __init__(self,player):
        super().__init__()
        self.velocite = 6
        self.player = player
        self.image = pygame.image.load("Assets/balle1.png")
        self.image = pygame.transform.scale(self.image,(20,20))
        self.rect = self.image.get_rect()
        self.rect.x = 755
        self.rect.y = 375
        
    def mouvement(self):
        self.rect.x -= self.velocite
        if self.player.check_colli(self.player):
            self.remove()
        if self.rect.x > 800:
            self.player.ballegr.remove(self)
"""
"""
class Balle(pygame.sprite.Sprite):
    def __init__(self,player,x,y):
        super().__init__()
        self.velocite = 2
        self.player = player
        self.image = pygame.image.load("Assets/balle.png")
        self.image = pygame.transform.scale(self.image,(10,10))
        self.image.set_colorkey(0,0)
        self.rect = self.image.get_rect()
        self.position = [x,y]
        self.x = self.position[0]
        self.y = self.position[1]
        self.box = pygame.Rect(0,0, self.rect.width * 0.5,5)
        self.old_position = self.position.copy()
        print(self.x,self.y)
    def sauvegarder_localisation(self):
        self.old_position = self.position.copy()
    def retour_arriere(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.box.midbottom = self.rect.midbottom    
    def mouvement(self):
        self.x += 1
    def update(self):
        self.position = self.position
        
"""       
class Balle(pygame.sprite.Sprite):         
    def __init__(self,x,y,player):
        super().__init__()
        self.player = player
        self.image = pygame.image.load("Assets/balle.png")
        self.image = pygame.transform.scale(self.image,(10,10))
        self.image.set_colorkey(0,0)
        self.rect = self.image.get_rect()
        self.position = [x,y]
        self.box = pygame.Rect(0,0, self.rect.width * 0.5,5)
        self.old_position = self.position.copy()
        self.diff_x = x
        self.diff = self.diff_x - self.position[0]
        self.player_x = self.player.position[0] + 800
        self.vitesse = 3
    def avancer(self):
        self.position[0] += self.vitesse
        if self.position[0]> self.player_x:
            self.remove(self.player.game.gr_balle)
            self.remove(self.player.game.group)
        if self.box.colliderect(self.player.game.monstre1 or self.player.game.monstre2):
            print("toucher1")
            self.remove(self.player.game.gr_balle)
            self.remove(self.player.game.group)
            self.player.game.monstre1.pv -= 10
            if self.player.game.monstre1.pv == 0:
                self.player.game.monstre1.kill()
                self.player.xp += 50
                self.player.argent += 20
        if self.box.colliderect(self.player.game.monstre2):
            print("toucher2")
            self.remove(self.player.game.gr_balle)
            self.remove(self.player.game.group)
            self.player.game.monstre2.pv -= 10
            if self.player.game.monstre2.pv == 0:
                self.player.game.monstre2.kill()
                self.player.xp += 50
                self.player.argent += 20
        if self.box.colliderect(self.player.game.monstre3):           
            print("toucher3")
            self.remove(self.player.game.gr_balle)
            self.remove(self.player.game.group)
            self.player.game.monstre3.pv -= 10
            if self.player.game.monstre3.pv == 0:
                self.player.game.monstre3.kill()
                self.player.xp += 50
                self.player.argent += 20       
        
    def update(self):
        self.rect.topleft = self.position
        self.box.midbottom = self.rect.midbottom
    def retour_arriere(self):
        pass
    
class Balle1(pygame.sprite.Sprite):         
    def __init__(self,x,y,player):
        super().__init__()
        self.player = player
        self.image = pygame.image.load("Assets/balle1.png")
        self.image = pygame.transform.scale(self.image,(10,10))
        self.image.set_colorkey(0,0)
        self.rect = self.image.get_rect()
        self.position = [x,y]
        self.box = pygame.Rect(0,0, self.rect.width * 0.5,5)
        self.old_position = self.position.copy()
        self.diff_x = x
        self.diff = self.diff_x - self.position[0]
        self.player_x = self.player.position[0] + 800
        self.player_xx = self.player.position[0] - 800
        self.vitesse = 3
    def avancer(self):
        self.position[0] -= self.vitesse
        if self.position[0]< self.player_xx:
            print("supp")
            self.remove(self.player.game.gr_balle)
            self.remove(self.player.game.group)
        if self.box.colliderect(self.player.game.monstre1):
            print("toucher1")
            self.remove(self.player.game.gr_balle)
            self.remove(self.player.game.group)
            self.player.game.monstre1.pv -= 10
            if self.player.game.monstre1.pv == 0:
                self.player.game.monstre1.remove(self.player.game.gr_monstre)
                self.player.game.monstre1.remove(self.player.game.group)
                self.player.xp += 50
                self.player.argent += 20 
        if self.box.colliderect(self.player.game.monstre2):
            print("toucher2")
            self.remove(self.player.game.gr_balle)
            self.remove(self.player.game.group)
            self.player.game.monstre2.pv -= 10
            if self.player.game.monstre2.pv == 0:
                self.player.game.monstre2.kill()
                self.player.xp += 50
                self.player.argent += 20
        if self.box.colliderect(self.player.game.monstre3):           
            print("toucher3")
            self.remove(self.player.game.gr_balle)
            self.remove(self.player.game.group)
            self.player.game.monstre3.pv -= 10
            if self.player.game.monstre3.pv == 0:
                self.player.game.monstre3.kill()
                self.player.xp += 50
                self.player.argent += 20
    def update(self):
        self.rect.topleft = self.position
        self.box.midbottom = self.rect.midbottom
    def retour_arriere(self):
        pass