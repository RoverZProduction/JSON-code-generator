#!/usr/bin/env python
#-*- coding:Utf-8 -*-

#Programme qui définit les fonctions utilisés par le script Gen.py

def text(text):
    JSON = ''
    inter = ['{','text:','"',text,'"']              #Fonction qui transforme une simple phrase en format JSON
    for fin in inter:
        JSON = JSON + fin
    return JSON
    
def color(text,color):
    JSON = ''
    inter = [',','extra:[{','text:"',text,'",','color:"',color,'"}]}']
    for fin in inter:                               #Fonction qui permet l'ajout de couleur
        JSON = JSON + fin
    return JSON
