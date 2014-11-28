#!/usr/bin/env python
#-*- coding:Utf-8 -*-

#Programme qui définit les fonctions utilisés par le script Gen.py

def text(text = raw_input('Entrez le texte sans couleur :')):
    JSON = ''
    inter = ['{','text:','"',text,'"']              #Fonction qui transforme une simple phrase en format JSON
    for fin in inter:
        JSON = JSON + fin
    print JSON
    
def color(text = raw_input('Entrez le texte à mettre en couleur :'),color = raw_input('Entrez la couleur souhaitée :')):
    JSON = ''
    inter = [',','extra:[{','text:',text,',','color:',color,'}]']
    for fin in inter:
        JSON = JSON + fin
    print JSON
