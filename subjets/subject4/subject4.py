#!/usr/bin/env python3

class Heure():
    def __init__(self, heure = 0, minute = 0):
        self.heure = heure
        self.minute = minute
    
    def toString(self):
        heures = self.heure
        minutes = self.minute
        return(f"{heures}:{minutes}")
    
    def compareTo(self, autreHeure):
        if not isinstance(autreHeure, Heure):
            return("Can not compare, it is not an hour")
        else:
            minutesComparees = self.minute
            minutesComparantes = autreHeure.minute
            heuresComparees = self.heure
            heuresComparantes = autreHeure.heure
            if heuresComparees >= heuresComparantes:
                if minutesComparees > minutesComparantes:
                    return(1)
                if minutesComparees == minutesComparantes:
                    return(0)
            else:
                return(-1)

class Creneau():
    def __init__(self, heureDebut = None, heureFin = None, minuteDebut = None, minuteFin = None):
        self.heureDebut = heureDebut
        self.heureFin = heureFin
        self.minuteDebut = minuteDebut
        self.minuteFin = minuteFin

    def conflictWith(self, inputCreneau):

        heureDebutCreneauComparee = self.heureDebut
        heureFinCreneauComparee = self.heureFin
        minuteDebutCreneauComparee = self.minuteDebut
        minuteFinCreneauComparee = self.minuteFin

        heureDebutCreneauComparant = inputCreneau.heureDebut
        heureFinCreneauComparant = inputCreneau.heureFin
        minuteDebutCreneauComparant = inputCreneau.minuteDebut
        minuteFinCreneauComparant = inputCreneau.minuteFin

        # fallait utiliser la méthode créée sur les heures
        # if heureDebutCreneauComparee.compareTo(inputCreneau.heureDebut) == -1 and 
        # toujours réfléchir un peu plus loin que l'exercice, ou avec un peu plus de recul

        if heureDebutCreneauComparant > heureDebutCreneauComparee and heureDebutCreneauComparant < heureFinCreneauComparee:
            return(True)

        if heureFinCreneauComparant > heureDebutCreneauComparee and heureFinCreneauComparant < heureFinCreneauComparee:
            return(True)

        return(False)
    
    def duree(self):
        minutes = str(self.minuteFin - self.minuteDebut)
        heures = str(self.heureFin - self.heureDebut)
        return(f"{heures}:{minutes}")
    
class Planning:
    def __init__(self, tableauCreneaux = None):
        self.tableauCreneaux = tableauCreneaux
        # tableau qui contiendra des instances d'objects creneaux
    
    def ajouterCreneau(self, inputCreneau):
        self.tableauCreneaux.append(inputCreneau)
    
    def dureeTotal(self):
        minutesTotales
        heuresTotales
        for creneaux in self.tableauCreneaux:
            heuresTotales += creneaux.duree()
    
class CreneauCours(Creneau):
    def __init__(self, heureDebut, heureFin, minuteDebut, minuteFin):
        super().__init__(heureDebut, heureFin, minuteDebut, minuteFin)

    def etd(self):
        return(self.duree())

class CreneauTD(Creneau):
    def __init__(self, heureDebut, heureFin, minuteDebut, minuteFin):
        super().__init__(heureDebut, heureFin, minuteDebut, minuteFin)

    def etd(self):
        return(self.duree()*0.5)

class CreneauTP(Creneau):
    def __init__(self, heureDebut, heureFin, minuteDebut, minuteFin):
        super().__init__(heureDebut, heureFin, minuteDebut, minuteFin)

    def etd(self):
        return(self.duree()*0.33)
    




            
        


# initialisation des valeurs

test = Heure()
test.heure = 1
test.minute = 2

test2 = Heure()
test2.heure = 4
test2.minute = 40

test3 = Heure()
test3.heure = 4
test3.minute = 40

creaneau1 = Creneau()
creaneau2 = Creneau()

creaneau1

# initialisation des tests

# WORKING
print(test.toString())  # fonctionne aussi sans print

# WORKING
print(test.compareTo(test2))
print(test2.compareTo(test3))
print(test2.compareTo(test))

