#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
que fait : fichier classe des regles du jeu
qui : FOËX Vick / nael Axel
quand : 17/12/2020
que reste a faire : tout
lien git : https://github.com/armagoonGit/TP_space_invader
"""

from time import sleep

from alien import Alien
from moduGraphique import fenetre

class gameRule:
    def __init__(self):
        self.affichage = fenetre(self)
        
        self.alien = [Alien()]
        self.idAlien = []
        
        self.ship = "a pas"
    
    def start(self):
        self.affichage.go()

            
    def initialisationObj(self):
        for alien in self.alien:
            self.idAlien.append( self.affichage.can.create_oval(alien.x, alien.y, alien.x + 20, alien.y + 20,width=1,outline='red',fill='blue') )
        self.turn()

    def turn(self):
        sleep(200)

        for el in zip(self.alien, self.idAlien) :
            el[0].mouvement()
            self.affichage.can.coords(el[1] ,el[0].x + 1000, el[0].y, el[0].x + 20, el[0].y + 20 )
        
        
a = gameRule()
print(a.affichage.can.cget('height') )
a.start()

