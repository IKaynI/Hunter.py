import pygame
class PNJ(pygame.sprite.Sprite):
    def __init__(self,x,y,player,target):
        super().__init__("")
        self.player = player
        #image de base
        self.sprite_sheet = pygame.image.load(f"Assets/{target}/{target}0.png")
        self.image = self.get_image(0,0)
        self.image.set_colorkey(0,0)
        #Saugarde de la premiere image
        self.old_image = self.image.copy()
        # Bas en haut
        self.image2 = pygame.image.load(f"Assets/{target}/{target}1.png")
        self.image2.set_colorkey(0,0)
        # Droite Gauche
        self.image3 = pygame.image.load(f"Assets/{target}/{target}2.png")
        self.image3.set_colorkey(0,0)
        #Haut bas
        self.image4 = pygame.image.load(f"Assets/{target}/{target}3.png")
        self.image4.set_colorkey(0,0)
        # Positon, Collision et verif
        self.rect = self.image.get_rect()
        self.position = [x,y]
        self.box = pygame.Rect(0,0, self.rect.width * 0.5,5)
        self.old_position = self.position.copy()
        self.pv_max = 100
        self.pv = 100
        self.vitesse = 1.75
        self.target = target
        self.verif= False
        self.verif2= False
        self.verif3 = False
        self.vitesse = 1
    def avancer(self):
        way = []
        count1 = 1
        for x in range(1,5):
            obj_name = self.player.game.tmx_data1.get_object_by_name( self.target+ str(count1))
            way.append(pygame.Rect( obj_name.x,  obj_name.y,  obj_name.width,  obj_name.height))
            count1 += 1
        # Gauche à droite
        if self.position[0] < way[1][0] and self.verif is False:
            self.image = self.old_image
            self.position[0] += self.vitesse
            if self.position[0] == way[1][0] and self.position[1] == way[1][1]:
                self.verif = True
        # Bas en Haut
        if self.position[1] > way[2][1] and self.verif is True and self.verif2 is False:
                self.image = self.image2
                self.position[1] -= self.vitesse
                if self.position[1] == way[2][1]:
                    self.verif2 = True
        # Droite à gauche
        if self.position[0] > way[3][0] and self.verif2 is  True:
            self.image = self.image3
            self.position[0] -= self.vitesse
            self.verif3 = True
        # Haut en bas
        if self.position[0] == way[3][0] and self.verif is True:
            self.image = self.image4
            self.position[1] += self.vitesse
            if self.position[1] == way[0][1]:
                self.verif = False
                self.verif2 = False
        if self.box.colliderect(self.player):
                self.vitesse = 0
        if not self.box.colliderect(self.player):
                self.vitesse = 1          
                   
    def get_image(self,x,y):
        image = pygame.Surface([16,32])
        image.blit(self.sprite_sheet, (0,0),(x,y, 16, 32))
        return image
    def update(self):
        self.rect.topleft = self.position
        self.box.midbottom = self.rect.midbottom
    def retour_arriere(self):
        pass
    
# -------------------------------- Voiture -------------------------------------------------------------------------------------  
class PNJ_Car(pygame.sprite.Sprite):
    def __init__(self,x,y,player,target):
        super().__init__("")
        self.player = player
        #image de base
        self.sprite_sheet = pygame.image.load(f"Assets/{target}/{target}0.png")
        self.image = self.sprite_sheet
        self.image.set_colorkey(0,0)
        #Saugarde de la premiere image
        self.old_image = self.image.copy()
        # Bas en haut
        self.image2 = pygame.image.load(f"Assets/{target}/{target}1.png")
        self.image2.set_colorkey(0,0)
        # Droite Gauche
        self.image3 = pygame.image.load(f"Assets/{target}/{target}2.png")
        self.image3.set_colorkey(0,0)
        #Haut bas
        self.image4 = pygame.image.load(f"Assets/{target}/{target}3.png")
        self.image4.set_colorkey(0,0)
        # Positon, Collision et verif
        self.rect = self.image.get_rect()
        self.position = [x,y]
        self.box = pygame.Rect((0,0),(5,5))
        self.old_position = self.position.copy()
        self.pv_max = 100
        self.pv = 100
        self.target = target
        self.verif= False
        self.verif2= False
        self.verif3 = False
        self.vitesse = 3.5
    def avancer(self):
        way = []
        count1 = 1
        for x in range(1,5):
            obj_name = self.player.game.tmx_data1.get_object_by_name( self.target+ str(count1))
            way.append(pygame.Rect( obj_name.x,  obj_name.y,  obj_name.width,  obj_name.height))
            count1 += 1
        # Gauche à droite
        if self.position[0] < way[1][0] and self.verif is False:
            self.image = self.old_image
            self.position[0] += self.vitesse
            if self.position[0] == way[1][0] and self.position[1] == way[1][1]:
                self.verif = True
        # Bas en Haut
        if self.position[1] > way[2][1] and self.verif is True and self.verif2 is False:
                self.image = self.image2
                self.position[1] -= self.vitesse
                if self.position[1] == way[2][1]-1:
                    self.verif2 = True
        # Droite à gauche
        if self.position[0] > way[3][0] and self.verif2 is  True:
            self.image = self.image3
            self.position[0] -= self.vitesse
            self.verif3 = True
        # Haut en bas
        if self.position[0] == way[3][0] and self.verif is True:
            self.image = self.image4
            self.position[1] += self.vitesse
            if self.position[1] == way[0][1]:
                self.verif = False
                self.verif2 = False
        if self.box.colliderect(self.player):
                self.player.pv = 0           
    def get_image(self,x,y):
        image = pygame.Surface([16,32])
        image.blit(self.sprite_sheet, (0,0),(x,y, 16, 32))
        return image
    def update(self):
        self.rect.topleft = self.position
        self.box.midbottom = self.rect.midbottom
    def retour_arriere(self):
        pass
    
    

# ---------------------------------------------------------------Objet ------------------------------------------------------------
class Objet(pygame.sprite.Sprite):
    def __init__(self,x,y,player,target):
        super().__init__("")
        self.player = player
        #image de base
        self.sprite_sheet = pygame.image.load(f"Assets/{target}/{target}0.png")
        self.image = self.get_image(0,0)
        self.image.set_colorkey(0,0)
        #Saugarde de la premiere image
        self.old_image = self.image.copy()
        # Positon, Collision et verif
        self.rect = self.image.get_rect()
        self.position = [x,y]
        self.box = pygame.Rect(0,0, self.rect.width * 0.5,5)
        self.target = target
    def get_image(self,x,y):
        image = pygame.Surface([16,32])
        image.blit(self.sprite_sheet, (0,0),(x,y, 16, 32))
        return image
    def update(self):
        self.rect.topleft = self.position
        self.box.midbottom = self.rect.midbottom
    def retour_arriere(self):
        pass