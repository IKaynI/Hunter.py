import pygame


class Animation_player_rundroite(pygame.sprite.Sprite):
    def __init__(self,cible):
        super().__init__()
        self.sprite_sheet = pygame.image.load("Assets/player.png")
        self.image = self.get_image(0,0)
        self.images2 = animation.get("runleft")
        self.images3 = animation.get("run-monstre")
        self.current_image = 0
        self.images = animation.get(cible)
        self.animation = False
    def active_animation(self):
        self.animation = True    
    def get_image(self,x,y):
        image = pygame.Surface([48,48])
        image.blit(self.sprite_sheet, (0,0),(x,y, 48, 48))
        return image
    def get_image1(self,x,y,cible):
        image = pygame.Surface([48, 48])
        image.blit(cible, (0,0),(x,y, 48, 48))
        return image
    def get_image2(self,x,y,cible):
        image = pygame.Surface([48, 48])
        image.blit(cible, (0,0),(x,y, 48, 48))
        return image
    # courrir droite
    def animate(self):
        if self.animation is True:
            self.current_image += 0.2
            if self.current_image >= len(self.images):
                self.current_image = 0  
                self.animation = False
            self.image = self.images[int(self.current_image)]
            x = self.get_image1(0,0,self.image)
            self.image = x
            self.image.set_colorkey(0,0)
     # courrir gauche
    def animate1(self):
            if self.animation is True:
                self.current_image += 0.2
                if self.current_image >= len(self.images2):
                    self.current_image = 0  
                    self.animation = False
                self.image = self.images2[int(self.current_image)]
                x = self.get_image1(0,0,self.image)
                self.image = x
                self.image.set_colorkey(0,0)
    def animate2(self):
            if self.animation is True:
                self.current_image += 0.2
                if self.current_image >= len(self.images3):
                    self.current_image = 0  
                    self.animation = False
                self.image = self.images3[int(self.current_image)]
                x = self.get_image1(0,0,self.image)
                self.image = x
                self.image.set_colorkey(0,0)
#chargement des animations courir
def chargement_player_animation(cible):
    images = []
    path = f"Assets/{cible}/{cible}"
    for image in range(0,6):
        image_path = path +"_"+ str(image) + ".png"
        images.append(pygame.image.load(image_path))
        
    return images
def chargement_player_animation1(cible):
    images = []
    path = f"Assets/{cible}/{cible}"
    for image in range(0,8):
        image_path = path +"_"+ str(image) + ".png"
        images.append(pygame.image.load(image_path))
    return images
animation = {
    "run" : chargement_player_animation("run"),
    "runleft": chargement_player_animation("runleft"),
    "run-monstre": chargement_player_animation1("monstre")
}  