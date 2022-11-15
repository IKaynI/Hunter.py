import pygame    
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
            self.player.game.monstre1.pv -= self.player.attack
            if self.player.game.monstre1.pv == 0:
                self.player.game.monstre1.kill()
                self.player.xp += 50
                self.player.argent += 20
        if self.box.colliderect(self.player.game.monstre2):
            print("toucher2")
            self.remove(self.player.game.gr_balle)
            self.remove(self.player.game.group)
            self.player.game.monstre2.pv -= self.player.attack
            if self.player.game.monstre2.pv == 0:
                self.player.game.monstre2.kill()
                self.player.xp += 50
                self.player.argent += 20
        if self.box.colliderect(self.player.game.monstre3):           
            print("toucher3")
            self.remove(self.player.game.gr_balle)
            self.remove(self.player.game.group)
            self.player.game.monstre3.pv -= self.player.attack
            if self.player.game.monstre3.pv == 0:
                self.player.game.monstre3.kill()
                self.player.xp += 50
                self.player.argent += 20       
        
    def update(self):
        if self.player.game.bll4 is True:
            self.image = pygame.image.load("Assets/balle2.png")
            self.image = pygame.transform.scale(self.image,(10,10))
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
            self.player.game.monstre1.pv -= self.player.attack
            if self.player.game.monstre1.pv == 0:
                self.player.game.monstre1.remove(self.player.game.gr_monstre)
                self.player.game.monstre1.remove(self.player.game.group)
                self.player.xp += 50
                self.player.argent += 20 
        if self.box.colliderect(self.player.game.monstre2):
            print("toucher2")
            self.remove(self.player.game.gr_balle)
            self.remove(self.player.game.group)
            self.player.game.monstre2.pv -= self.player.attack
            if self.player.game.monstre2.pv == 0:
                self.player.game.monstre2.kill()
                self.player.xp += 50
                self.player.argent += 20
        if self.box.colliderect(self.player.game.monstre3):           
            print("toucher3")
            self.remove(self.player.game.gr_balle)
            self.remove(self.player.game.group)
            self.player.game.monstre3.pv -= self.player.attack
            if self.player.game.monstre3.pv == 0:
                self.player.game.monstre3.kill()
                self.player.xp += 50
                self.player.argent += 20
    def update(self):
        if self.player.game.bll4 is True:
            self.image = pygame.image.load("Assets/balle3.png")
            self.image = pygame.transform.scale(self.image,(10,10))
        self.rect.topleft = self.position
        self.box.midbottom = self.rect.midbottom
    def retour_arriere(self):
        pass