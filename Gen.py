#!/usr/bin/env python
#-*- coding:Utf-8 -*-

#Programme permettant la transformation d'un texte normal en un texte en JSON. test

from GenFns import *
from time import *

withoutColor = text(text = raw_input('Entrez le texte sans couleur :'))

withColor = ""

while 1:
    putColor = raw_input('Voulez-vous ajouter de la couleur à un autre texte ? (si texte sans couleur rentrez "white" au moment de la question de la couleur) (O/n) :')
    if not(putColor == "O"):
        if withColor == "":
            print withoutColor + '}'
            sleep(50)
            break
        else:
            print withoutColor + ',extra:[', withColor + ']}'
            sleep(50)
            break
    elif withColor == "":
        if not(putColor == ''):
            withColor = color(text = raw_input('Entrez le texte à mettre en couleur :'),color = raw_input('Entrez la couleur souhaitée :'))
    elif putColor == 'O':
        withColor = withColor + ',' + color(text = raw_input('Entrez le texte à mettre en couleur :'),color = raw_input('Entrez la couleur souhaitée :'))
sleep(120)       