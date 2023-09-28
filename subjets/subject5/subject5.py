class Expression:
    def evaluer(self):
        pass

    def expression(self):
        pass

class Constante(Expression):
    def __init__(self, valeur):
        self.valeur = valeur

    def evaluer(self):
        return(self.valeur)

    def expression(self):
        return(self.valeur)

class Operateurbinaire(Expression):
    def __init__(self, gauche, droit):
        self.gauche = gauche
        self.droit = droit

class Plus(Operateurbinaire):
    def evaluer(self):
        return(self.gauche.evaluer() + self.droit.evaluer())
    
    def expression(self):
        # return(f"({self.gauche.evaluer()} + {self.droit.evaluer()})
        # return(f"({self.gauche.evaluer()} + {self.droit.evaluer()} + {self.droit.expression()} + {self.gauche.expression()})")
        return(f"({self.gauche.expression()} + {self.droit.expression()})")
        

class Moins(Operateurbinaire):
    def evaluer(self):
        return(self.gauche.evaluer() - self.droit.evaluer())
    
    def expression(self):
        # return(f"({self.gauche.evaluer()} - {self.droit.evaluer()})
        # return(f"({self.gauche.evaluer()} - {self.droit.evaluer()} + {self.droit.expression()} + {self.gauche.expression()})")
        return(f"({self.gauche.expression()} - {self.droit.expression()})")

class Multiplier(Operateurbinaire):
    def evaluer(self):
        return(self.gauche.evaluer() * self.droit.evaluer())
    
    def expression(self):
        # return(f"({self.gauche.evaluer()} * {self.droit.evaluer()})
        # return(f"({self.gauche.evaluer()} * {self.droit.evaluer()} + {self.droit.expression()} + {self.gauche.expression()})")
        return(f"({self.gauche.expression()} * {self.droit.expression()})")

class Diviser(Operateurbinaire):
    def evaluer(self):
        if self.droit.evaluer() == 0:
            raise ValueError("divison par zero")
        return(self.gauche.evaluer() / self.droit.evaluer())
        
    def expression(self):
        # return(f"({self.gauche.evaluer()} / {self.droit.evaluer()})
        # return(f"({self.gauche.evaluer()} / {self.droit.evaluer()} + {self.droit.expression()} + {self.gauche.expression()})")
        return(f"({self.gauche.expression()} / {self.droit.expression()})")

expr = Multiplier(Constante(3), Plus(Constante(2), Multiplier(Constante(3), Constante(5))))
print(f"{expr.expression()} = {expr.evaluer()}")