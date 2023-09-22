#!/usr/bin/env python3

class Node():
    def __init__(self, node_value):
        self.node_value = node_value

    def addInTail(self, node_value):
        # node_value est le premier noeud la première fois
        if self.next != None: # un noeud quelconque
            # je vais chercher à faire addintail sur le prochain noeud
            self.next.addInTail(self.next)
        else:
            # création du noeud qui sera le dernier, il pointe vers rien
            new_node = Node(node_value)
            # l'ancien nouveau noeud passé en paramètre pointera vers le nouveau noeud créé
            self.next = new_node

    def afficheNoeud(self):
        try:
            print([self.node_value, self.next])
        except:
            print(self.node_value, None)

class LinkedList(Node):
    def __init__(self):
        self.head = None # premier noeud de la liste

    def addInHead(self, node_value):
        # creation d'un nouveau noeud qui sera le premier
        new_node = Node(node_value)
        # je pointe vers l'ancien premier noeud
        new_node.next = self.head
        # je modifie la liste pour lui indiquer que c'est le nouveau premier noeud
        self.head = new_node

    def addInTail(self, node_value):
        # création d'un nouveau noeud qui sera prochainement le dernier
        new_node = Node(node_value)
        # s'il n'y a pas de noeud dans la liste
        if self.head == None:
            # le noeud créé sera le premier noeud & le dernier car pointe vers rien
            self.head = new_node
        # sinon je le renvoi vers la création d'un nouveau noeud & de son attribution au dernier de la liste
        else:
            # self.head est un noeud, j'applique la méthode addInTail des noeufs, pas de la liste chainée
            self.head.addInTail(node_value)

    def afficherListe(self, noeud_actuel = "test"):
        if noeud_actuel == "test":
            self.head.afficheNoeud()
            print(self.afficherListe(self.head.next))
        else:
            noeud_actuel.afficheNoeud()


# testing

noeud_1 = Node(1)
noeud_2 = Node(2)
noeud_3 = Node(3)
noeud_1.next = noeud_2
noeud_2.next = noeud_3

linked_list = LinkedList()
linked_list.head = noeud_1

# WORKING
# print(noeud_1.next.node_value)

# WORKING
# linked_list.addInHead(noeud_2)

# WORKING
# print(noeud_1.afficheNoeud())

# WORKING
# linked_list.afficherListe()


# linked_list.addInTail(noeud_2)
