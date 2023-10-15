class Creneau:
    def __init__(self,heured,heuref):
        self.heure_debut = heured
        self.heure_fin = heuref

    def get_heure_debut(self):
        return self.heure_debut    

    def get_heur_fin(self):
        return self.heure_fin     

    def duree(self):
        heure = (self.heure_fin[0] - self.heure_debut[0])*60
        minute = self.heure_fin[1] - self.heure_debut[1]
        return minute+heure

    def conflitavec(self,cren):
        if cren.get_heure_debut() < self.heure_debut < cren.get_heur_fin():
            return True

        elif self.heure_debut < cren.get_heure_debut() < self.heure_fin:
            return True

        elif cren.get_heure_debut() > self.heure_fin > cren.get_heur_fin():
            return True

        elif self.heure_debut > cren.get_heure_debut() > self.heure_fin:
            return True

        else:
            return False

creneau1 = Creneau((8,00),(9,30))
creneau2 = Creneau((9,30),(10,20))
creneau3 = Creneau((9,00),(10,00))

class Planning:
    def __init__(self):
        self.planing = []

    def ajoutercreneau(self,cren):
        if self.planing == []:
            self.planing.append(cren)
            return "C bon"
        else:    
            for k in self.planing:
                if k.conflitavec(cren) != True:
                    self.planing.append(cren)  
                    return "C bon"

                else:
                    return "pas bon"
                
    def dureeTotal(self):
        total = 0
        for x in self.planing:
            total = total + x.duree()
        return total

    def dureeTotalHM(self):
        total = 0
        for y in self.planing:
            total = total + y.duree()
        heure = total//60
        minute = total%60
        return (heure,minute)

eleve1 = Planning()
print(eleve1.ajoutercreneau(creneau1))
print(eleve1.ajoutercreneau(creneau2))
print(eleve1.ajoutercreneau(creneau3))
print("Durée total du planning:",eleve1.dureeTotal(),"minutes")
dureeHM = eleve1.dureeTotalHM()
print("Durée total du planning:",dureeHM[0],"Heure(s)",dureeHM[1],"minute(s)")