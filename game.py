
import pygame
import pytmx
import pyscroll
from player import Player
from monstre import monstre
from arme import Balle
import time
import schedule
from pnj import PNJ,PNJ_Car,Objet
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Monster Hunter")
        self.clock = pygame.time.Clock()
        #charger le niveau
        tmx_data = pytmx.util_pygame.load_pygame("Level/city3.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data,self.screen.get_size())
        self.tmx_data1 = pytmx.util_pygame.load_pygame("Level/city3.tmx")
        # toutes les couches de la cartes
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer,default_layer=5)
        map_layer.zoom = 3
        # Joueur
        player_position = tmx_data.get_object_by_name("player")
        self.player = Player(player_position.x,player_position.y,self)
        self.group.add(self.player)
        # Collision + Events
        hopital = tmx_data.get_object_by_name("hosto")
        self.hopital = pygame.Rect(hopital.x,hopital.y,hopital.width,hopital.height)
        
        Atm = tmx_data.get_object_by_name("atm")
        self.atm = pygame.Rect(Atm.x,Atm.y,Atm.width,Atm.height)
        #Monstre
        monstre_position = [self.player.position[0]+250,self.player.position[1]]
        self.gr_monstre = pygame.sprite.Group()
        # ------------------------------ Verifcation
        self.monstre1 = ""
        self.ATM_v = False
        self.vef = False
        self.bll = False
        self.bll1 = False
        self.bll2 = False
        self.bll3 = False
        self.bll4 = False
        self.boss_cd = 0
        #------------Fonction
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
        # PNJ
        # ---------------- Paul ----------------------
        way_paul = []
        self.gr_pnj = pygame.sprite.Group()
        count1 = 1
        for x in range(1,5):
            obj_name = tmx_data.get_object_by_name("paul"+ str(count1))
            way_paul.append(pygame.Rect( obj_name.x,  obj_name.y,  obj_name.width,  obj_name.height))
            count1 += 1
        paul = PNJ(way_paul[0][0],way_paul[0][1],self.player,"paul")
        self.group.add(paul)
        self.gr_pnj.add(paul)
        # ---------------- Robert ----------------------
        way_robert = []
        count1 = 1
        for x in range(1,5):
            obj_name = tmx_data.get_object_by_name("robert"+ str(count1))
            way_robert.append(pygame.Rect( obj_name.x,  obj_name.y,  obj_name.width,  obj_name.height))
            count1 += 1
        robert = PNJ(way_robert[0][0],way_robert[0][1],self.player,"robert")
        self.group.add(robert)
        self.gr_pnj.add(robert)
        # ---------------- Voiture Bleu ----------------------
        way_bleu = []
        count1 = 1
        for x in range(1,5):
            obj_name = tmx_data.get_object_by_name("bleu"+ str(count1))
            way_bleu .append(pygame.Rect( obj_name.x,  obj_name.y,  obj_name.width,  obj_name.height))
            count1 += 1
        bleu = PNJ_Car(way_bleu [0][0],way_bleu [0][1],self.player,"bleu")
        self.group.add(bleu)
        self.gr_pnj.add(bleu)
        print(self.gr_pnj)
        # --------------------------- Lampe pour l'amélioration--------------------
        lamp_pos = []
        count1 = 1
        for x in range(1,4):
            obj_name = tmx_data.get_object_by_name("lamp"+ str(count1))
            lamp_pos.append(pygame.Rect( obj_name.x,  obj_name.y,obj_name.width,  obj_name.height))
            count1 += 1
        self.lamp1 = Objet(lamp_pos[0][0],lamp_pos[0][1],self.player,"lamp")
        self.lamp2 = Objet(lamp_pos[1][0],lamp_pos[1][1],self.player,"lamp")
        self.lamp3 = Objet(lamp_pos[2][0],lamp_pos[2][1],self.player,"lamp")
        
        self.group.add(self.lamp1)
        self.group.add(self.lamp2)
        self.group.add(self.lamp3)
        
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
        elif touche[pygame.K_g]:
            self.player.Hack_atm()
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
        # Collision Hopital
        if self.bll is False:
            if self.player.box.colliderect(self.hopital):
                self.player.hosto()
                self.bll = True
        if not self.player.box.colliderect(self.hopital):
            self.bll = False
        # Collision ATM  
        if self.ATM_v is False:
            if self.player.box.colliderect(self.atm):
                self.player.Hack_atm()
                self.ATM_v = True
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
            #Monstre et pnj mouvement
            for pnj in self.gr_pnj:
                pnj.avancer()
            for balle in self.gr_balle:
                balle.avancer()
            for monstre in self.gr_monstre:
                    monstre.avancer()
            # Player Update
            if self.player.xp >=100:
                self.player.xp = 0
                self.player.niveau += 1
            if self.player.pv <= 0:
                print("Vous êtes mort")
                self.player.remove(self.group)
                running = False
            #Lamp collision
            if self.bll1 is False:
                if self.lamp1.box.colliderect(self.player):
                    self.lamp1.remove(self.group)
                    print("Vous avez trouvé une des lampes pour améliorer votre arme")
                    self.boss_cd += 1
                    self.bll1 = True
                
            if self.bll2 is False and self.bll3 is True:
                if self.lamp2.box.colliderect(self.player):
                    self.lamp2.remove(self.group)
                    print("Vous avez trouvé une des lampes pour améliorer votre arme")
                    self.boss_cd += 1
                    self.bll2 = True
            
            if self.bll3 is False and self.bll1 is True:
                if self.lamp3.box.colliderect(self.player):
                    self.lamp3.remove(self.group)
                    print("Vous avez trouvé une des lampes pour améliorer votre arme")
                    self.boss_cd += 1
                    self.bll3 = True
            # Condition pour faire améliorer les balles
            if self.boss_cd == 3 and self.bll4 is False:
                self.player.attack = 20
                self.bll4 = True
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.display.quit()
                    pygame.quit()
            self.clock.tick(60)
        pygame.quit()