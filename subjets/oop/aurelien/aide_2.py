class Etudiant():
    def __init__(self,nom,prenom,age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.note = []

    def modif_nom(self,nom):
        self.nom = nom
        
    def modif_prenom(self,prenom):
        self.surname = prenom

    def modif_age(self,age):
        self.age = age

    def savenote(self,note):
        self.note.append(note)

    def nombre_note(self):
        return len(self.note)

    def moyen_eleve(self):
        total_note = 0
        nombre_note = len(self.note)
        for note in self.note:
            total_note += note

        moyenne = total_note/nombre_note    
        return moyenne


class Promotion():
    def __init__(self):
        self.etud = []

    def addetud(self,etudiant):
        self.etud.append(etudiant)

    def nbetud(self):
        return len(self.etud)

    def calculermoyenne(self):
        note = 0
        nombre_note = len(self.etud)
        for ele in self.etud:
            if ele.moyen_eleve() != 0:
                note += ele.moyen_eleve()
        moyenne = note/nombre_note
        return moyenne
        
        
eleve1 = Etudiant("p1","n1",28)
eleve1.savenote(18)        
eleve1.savenote(13)
eleve1.savenote(8)
eleve1.savenote(14)
eleve2 = Etudiant("p2","n2",18)
eleve2.savenote(12)        
eleve2.savenote(5)
eleve2.savenote(7)
eleve2.savenote(10)
eleve3 = Etudiant("p3","n3",18)
eleve3.savenote(20)        
eleve3.savenote(18)
eleve3.savenote(19)
eleve3.savenote(16)
Pormo = Promotion()
Pormo.addetud(eleve1)
Pormo.addetud(eleve2)
Pormo.addetud(eleve3)

print("Nombre d'étudiant dans la promo:",Pormo.nbetud())
print("Moyenne de la promo:",Pormo.calculermoyenne())