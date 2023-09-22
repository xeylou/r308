#!/usr/bin/env python

class noeud():
    def __init__(self, valeur = None):
        self.valeur = valeur
        self.enfantGauche = None
        self.enfantDroit = None
    
    def inserer(self, valeur):
        valeurAInserer = valeur
        # pas de valeur initiallement
        if self.valeur == None:
            self.valeur = valeurAInserer
            return('inséré')
        # pas besoin d'ajouter quelque part
        elif self.valeur == valeurAInserer:
            return('inséré')
        # essaye de mettre à gauche si existant (récursif), sinon création
        elif valeurAInserer < self.valeur:
            if self.enfantGauche is not None:
                self.enfantGauche.inserer(valeurAInserer)
                return
            self.enfantGauche = noeud(valeurAInserer)
            return
        # pareil pour droite
        elif self.enfantDroit:
            self.enfantDroit.inserer(valeurAInserer)
            return
        self.enfantDroit = noeud(valeurAInserer)

    def minimum(self):
        # jusqu'à ce qu'il n'y ait plus rien à gauche
        if self.enfantGauche is not None:
            self.enfantGauche.minimum()
        # il est à gauche, sinon premier noeud
        else:
            print(self.valeur)

    def maximum(self):
        # jusqu'à ce qu'il n'y ait plus rien à droite
        if self.enfantDroit is not None:
            self.enfantDroit.maximum()
        # plus grand noeud ou le seul
        else:
            print(self.valeur)
    
    def estDansArbre(self, valeurCherchee):
        # finalement le noeud a la valeur recherchée (condition finale)
        if self.valeur == valeurCherchee:
            return(True)
        # plus à gauche?
        if valeurCherchee < self.valeur:
            # pas trouvé à gauche
            if self.enfantGauche == None:
                return(False)
            # on va toujours plus à gauche si pas trouvé
            return(self.enfantGauche.estDansArbre(valeurCherchee))
        # pas de noeud plus à droite, pas valeur dans arbre
        if self.enfantDroit == None:
            return(False)
        # essaye à droite
        return(self.enfantDroit.estDansArbre(valeurCherchee))

    def parcoursPrefix(self, valeurs = []):
        # les valeurs quand on passe à gauche d'un noeud
        tableauPasse = valeurs
        # le noeud racine de l'arbre
        if self.valeur is not None:
            tableauPasse.append(self.valeur)
        # on continue le suivi sur la gauche jusqu'à ce qu'il n'y ait plus de noeud
        if self.enfantGauche is not None:
            self.enfantGauche.parcoursPrefix(tableauPasse)
        # il n'y a plus de noeud à gauche, on passe par le bas pour aller vers la droite puis remonter
        if self.enfantDroit is not None:
            self.enfantDroit.parcoursPrefix(tableauPasse)
        return(tableauPasse)
    
    def parcoursInfix(self, valeurs = []):
        tableauPasse = valeurs
        if self.enfantGauche is not None:
            self.enfantGauche.parcoursInfix(tableauPasse)
        if self.valeur is not None:
            tableauPasse.append(self.valeur)
        if self.enfantDroit is not None:
            self.enfantDroit.parcoursInfix(tableauPasse)
        return(tableauPasse)

    def parcoursPostfix(self, valeurs = []):
        tableauPasse = valeurs
        if self.enfantGauche is not None:
            self.enfantGauche.parcoursPostfix(tableauPasse)
        if self.enfantDroit is not None:
            self.enfantDroit.parcoursPostfix(tableauPasse)
        if self.valeur is not None:
            tableauPasse.append(self.valeur)
        return(tableauPasse)


class arbre():
    def __init__(self, racine):
        self.racine = racine


###########
# TESTS
###########

arbre1 = noeud()
arbre1.inserer(3)
arbre1.inserer(2)
arbre1.inserer(9)
arbre1.inserer(1)
arbre1.inserer(5)

# https://asciiflow.com
# print(f"\narbre:\n\n         3\n         │\n         │\n    2 ◄──┴──► 9\n    │         │\n    │         │\n1◄──┘     5◄──┘\n")
print(f"\ngraphique de l'arbre:\n\n          3\n\n          │\n          │\n     2 ◄──┴──► 9\n\n     │         │\n     │         │\n1 ◄──┘    5 ◄──┘\n")

print("\nle chiffre 9 est présent:")
print(arbre1.estDansArbre(9)) # print car doit retourner des trucs

print("\nle chiffre 10 est présent:")
print(arbre1.estDansArbre(10)) # print car doit retourner des trucs

print(f"\nminimum:")
arbre1.minimum()
print("\nmaximum:")
arbre1.maximum()

# ! /!\ DIFFERENCE ELIF & IF
# ! SI CONDITION PAS LES AUTRES

print(f"\nparcours préfix:")
print(arbre1.parcoursPrefix())
print(f"\nparcours infixe:")
print(arbre1.parcoursInfix())
print(f"\nparcours postfix/suffix:")
print(arbre1.parcoursPostfix())