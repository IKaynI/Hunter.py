import pygame
import animation
import pytmx
from arme import Balle,Balle1
from tkinter import *
import random
import itertools
import time
import tkinter as tk
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
        self.box = pygame.Rect(0,0,self.rect.width * 0.5,5)
        self.old_position = self.position.copy()
        self.verif = None
        #Stats
        self.vitesse = 4.5
        self.pv_max = 150
        self.pv = 150
        self.argent = 10
        self.niveau = 0
        self.attack = 10
        self.xp = 0
        #Verif Boutique
        self.hack_outil = True
        self.combinaison = itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9],4)
        self.rd_num = random.randint(0,5040)
        count = 0
        for combi in self.combinaison:
            count += 1
            result = str("".join(str(i) for i in combi ))
            if count == self.rd_num:
                self.b = result
        self.verifhack = True
    # ------------------------- Fonction ---------------------------------------------------------
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
        self.position[0] += self.vitesse
    def gauche(self):
        self.verif = False
        self.active_animation()
        self.animate1()
        self.position[0] -= self.vitesse
    def saut(self):
        self.active_animation()
        self.animate()
        self.position[1] -= self.vitesse
    def bas(self):
        self.active_animation()
        self.animate()
        self.position[1] += self.vitesse
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
        
    # Hopital message box
    def heal(self):
        if self.argent >=50:
            self.argent -= 50
            self.pv = self.pv_max
    def hosto(self):
        window = Tk()
        window.geometry("195x115")
        window_width = 195
        window_height = 115
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        window.configure(bg = "#4c4e52")
        canvas = Canvas(
        window,
        bg = "#4c4e52",
        height = 115,
        width = 182,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
        canvas.place(x = 0, y = 0)

        canvas.create_text(
        103.5, 31.0,
        text = "Se soigner pour 50$ ?\n",
        fill = "#ffffff",
        font = ("None", int(15.0)))

        img0 = PhotoImage(file = f"Ui/img0.png")
        b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = self.heal,
        relief = "flat")

        b0.place(
        x = 47, y = 67,
        width = 86,
        height = 20)

        window.resizable(False, False)
        window.mainloop()
        
        # Hack ATM
    
    def verif_outil(self):
        if self.hack_outil is False:
            print("Vous n'avez pas l'outil de piratage")
        if self.hack_outil is True: 
            print("Vous avez l'outil")
            self.hack()
    def hack(self):
        print("Début du piratage")
        combinaison = itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9],4)
        for combi in combinaison:
            result = str("".join(str(i) for i in combi ))
            if result == self.b:
                c = result
                self.entry0.delete(0, END)
                self.entry0.insert("end",c)
    def valid(self):
        self.combi = self.combi4.get()
        print(self.b, self.combi)
        if self.b == self.combi and self.verifhack is True:
            print("Vous avez réussi le piratage")
            self.argent += 100
            self.verifhack = False
        else:
            print("Le code n'est pas bon")
    def Hack_atm(self):
        window = Tk()
        window.geometry("618x529")
        window.configure(bg = "#ffffff")
        window_width = 618
        window_height = 529
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.combi4 = tk.StringVar()
        canvas = Canvas(
            window,
            bg = "#ffffff",
            height = 529,
            width = 618,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        background_img = PhotoImage(file = f"Ui/background1.png")
        background = canvas.create_image(
            309.5, 264.5,
            image=background_img)

        img0 = PhotoImage(file = f"Ui/img01.png")
        b0 = Button(
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.valid,
            relief = "flat")

        b0.place(
            x = 249, y = 296,
            width = 116,
            height = 40)

        entry0_img = PhotoImage(file = f"Ui/img_textBox0.png")
        self.entry0_bg = canvas.create_image(
            307.0, 225.5,
            image = entry0_img)

        self.entry0 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            highlightthickness = 0,
            width=30,
            fg="Black",
            font= ("Helvetica", 15),
            textvariable= self.combi4)

        self.entry0.place(
            x = 209, y = 213,
            width = 196,
            height = 23)

        img1 = PhotoImage(file = f"Ui/img02.png")
        b1 = Button(
            image = img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.verif_outil,
            relief = "flat")

        b1.place(
            x = 505, y = 415,
            width = 56,
            height = 22)

        window.resizable(False, False)
        window.mainloop()