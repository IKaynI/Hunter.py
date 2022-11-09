import pygame
import animation
import pytmx
from arme import Balle,Balle1
from tkinter import *
class Player(animation.Animation_player_rundroite):
    def __init__(self,x,y,game):
        super().__init__("run")
        self.game = game
        self.sprite_sheet = pygame.image.load("Assets/Gunner_Blue_Idle.png")
        self.image = self.get_image(0,0)
        self.image.set_colorkey(0,0)
        self.rect = self.image.get_rect()
        self.balle = ""
        self.position = [x,y]
        self.x = self.position[0]
        self.y = self.position[1]
        self.box = pygame.Rect(0,0, self.rect.width * 0.5,5)
        self.old_position = self.position.copy()
        self.verif = None
        #Stats
        self.vitesse = 2.5
        self.pv_max = 100
        self.pv = 150
        self.argent = 10
        self.niveau = 0
        self.attack = 10
        self.xp = 0
    def tir(self):
        if self.verif is True:
            self.balle = Balle(self.position[0] +35,self.position[1]+15,self)
            self.game.gr_balle.add(self.balle)
            self.game.group.add(self.balle)
    def tir1(self):
        if self.verif is False:
            self.balle = Balle1(self.position[0] -15,self.position[1]+15,self)
            self.game.gr_balle.add(self.balle)
            self.game.group.add(self.balle)
    # Collision    
    def sauvegarder_localisation(self):
        self.old_position = self.position.copy()
    def retour_arriere(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.box.midbottom = self.rect.midbottom
    # Mouvement du Joueur
    def droite(self):
        self.verif = True
        self.active_animation()
        self.animate()
        self.position[0] += 2.5
    def gauche(self):
        self.verif = False
        self.active_animation()
        self.animate1()
        self.position[0] -= 2.5
    def saut(self):
        self.active_animation()
        self.animate()
        self.position[1] -= 2.5
    def bas(self):
        self.active_animation()
        self.animate()
        self.position[1] += 2.5
    #position update
    def update(self):
        self.rect.topleft = self.position
        self.box.midbottom = self.rect.midbottom
    def get_image(self,x,y):
        image = pygame.Surface([48,48])
        image.blit(self.sprite_sheet, (0,0),(x,y, 48, 48))
        return image
    # Fenetre de stats
    def stats(self):
        window = Tk()
        window_width = 504
        window_height = 243
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        window.geometry("543x260")
        window.configure(bg = "#ffffff")
        canvas = Canvas(
            window,
            bg = "#ffffff",
            height = 260,
            width = 543,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        background_img = PhotoImage(file = f"Ui/background.png")
        background = canvas.create_image(
            277.5, 134.0,
            image=background_img)

        canvas.create_text(
            336.0, 80.5,
            text = round(self.pv),
            fill = "#ffffff",
            font = ("", int(15.0)))

        canvas.create_text(
            336.0, 125.5,
            text = self.attack,
            fill = "#ffffff",
            font = ("", int(15.0)))

        canvas.create_text(
            336.0, 171.5,
            text = self.niveau,
            fill = "#ffffff",
            font = ("", int(15.0)))

        canvas.create_text(
            500.0, 80.5,
            text = self.argent,
            fill = "#ffffff",
            font = ("", int(15.0)))

        canvas.create_text(
            500.0, 125.5,
            text = self.vitesse,
            fill = "#ffffff",
            font = ("", int(15.0)))

        window.resizable(False, False)
        window.mainloop()