
import pygame
import pytmx
import pyscroll
from player import Player
from monstre import monstre
from arme import Balle
import time
import schedule
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Monster Hunter")
        self.clock = pygame.time.Clock()
        #charger le niveau
        tmx_data = pytmx.util_pygame.load_pygame("Level/city3.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data,self.screen.get_size())
        # toutes les couches de la cartes
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer,default_layer=5)
        map_layer.zoom = 3
        # Joueur
        player_position = tmx_data.get_object_by_name("player")
        self.player = Player(player_position.x,player_position.y,self)
        self.group.add(self.player)
        #Monstre
        monstre_position = [self.player.position[0]+250,self.player.position[1]]
        self.gr_monstre = pygame.sprite.Group()
        self.monstre1 = ""
        self.vef = False
        def monstre_sp():
            print("un monstre est apparue")
            x = self.player.position[0]+250
            y = self.player.position[1]
            self.monstre1 =(monstre(x,y,self.player))
            self.gr_monstre.add(self.monstre1)
            self.group.add(self.monstre1)
        self.monstre2 =(monstre(15,30,self.player))
        self.monstre2.pv = 0
        self.monstre3 = (monstre(15,30,self.player))
        def monstre_sp1():
            if self.vef is False and self.monstre2.pv > 0:
                self.vef = True
            if self.vef is True:
                print("ez")
                self.monstre3 = None
                self.monstre3 = self.monstre2
                self.monstre2 = None
                self.gr_monstre.add(self.monstre3)
                self.group.add(self.monstre3)
            print("un monstre est apparue")
            x = self.player.position[0]+250
            y = self.player.position[1]
            self.monstre2 =(monstre(x,y,self.player))
            self.gr_monstre.add(self.monstre2)
            self.group.add(self.monstre2)
            self.vef = False
        #balle
        self.gr_balle = pygame.sprite.Group()
        self.balle1 = Balle(self.player.position[0] +35,self.player.position[1]+15,self.player)
        self.gr_balle.add(self.balle1)
        self.group.add(self.balle1)
        
        
        # Rectangle de Collision
        self.walls = []
        count = 0
        for x in range(102):
            obj_name = tmx_data.get_object_by_name("collision"+ str(count))
            self.walls.append(pygame.Rect( obj_name.x,  obj_name.y,  obj_name.width,  obj_name.height))
            count += 1
        # début Fonction 
        monstre_sp()
        schedule.every(35).seconds.do(monstre_sp1)
        schedule.every(60).seconds.do(monstre_sp)
        
        

    # Captation des touches de claviers
    def entre_clavier(self):
        touche = pygame.key.get_pressed()
        if touche[pygame.K_z]:
            self.player.saut()
        elif touche[pygame.K_q]:
            self.player.gauche()
        elif touche[pygame.K_d]:
            self.player.droite()
        elif touche[pygame.K_s]:
            self.player.bas()
        elif touche[pygame.K_f]:
            self.player.stats()
        elif touche[pygame.K_m]:
            self.playerbts
    def entre_clavier1(self):
        for event in pygame. event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.player.tir1()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 3:
                        self.player.tir()
    # On actualise les données
    def update(self):
        self.group.update()
        for sprite in self.group.sprites():
            if sprite.box.collidelist(self.walls) > -1:
                sprite.retour_arriere()  
             
    def run(self):
        
        running = True
        while running:
            schedule.run_pending()
            self.player.sauvegarder_localisation()
            self.entre_clavier()
            self.entre_clavier1()
            self.update()
            self.group.center(self.player.rect.center)
            self.group.draw(self.screen)
            
            for balle in self.gr_balle:
                balle.avancer()
            for monstre in self.gr_monstre:
                    monstre.avancer()
            if self.player.xp >=100:
                self.player.xp = 0
                self.player.niveau += 1
            if self.player.pv < 0:
                print("Vous êtes mort")
                self.player.remove(self.group)
                running = False   
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.display.quit()
                    pygame.quit()
            self.clock.tick(60)
        pygame.quit()