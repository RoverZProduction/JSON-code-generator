#!/usr/bin/env python
#-*- coding:Utf-8 -*-

#Programme permettant la transformation d'un texte normal en un texte en JSON.

from Genfns import *

withoutColor = text(text = raw_input('Entrez le texte sans couleur :'))

putColor = raw_input('Voulez-vous ajouter de la couleur à un autre texte ? (O/n) :')
if putColor == 'O':
    withColor = color(text = raw_input('Entrez le texte à mettre en couleur :'),color = raw_input('Entrez la couleur souhaitée :'))
    print withoutColor, withColor
else:
    print withoutColor + '}'
