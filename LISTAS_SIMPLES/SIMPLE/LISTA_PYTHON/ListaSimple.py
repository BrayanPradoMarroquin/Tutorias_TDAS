from NodoSimple import Nodo
import os

class Lista:
    def __init__(self):
        self.cabeza = None

    def vacio(self):
        return self.cabeza == None

    def agregar(self, id, nombre):
        Nuevo = Nodo(id, nombre)
        if self.vacio():
            self.cabeza = Nuevo
        else:
            Nuevo.siguiente = self.cabeza
            self.cabeza = Nuevo 

    def recorrer(self):
        Nuevo = self.cabeza
        while(Nuevo != None):
            print(str(Nuevo.getid()) + " -> " + Nuevo.getnombre())
            Nuevo = Nuevo.siguiente

    def graficar(self):
        Nuevo = self.cabeza
        cont = 0
        cadena = ""
        file = open('grafica.dot', 'w')
        cadena = cadena + 'digraph G { \n'
        while(Nuevo!=None):
            cadena = cadena + 'Node'+str(cont)+'[label=\"'+str(Nuevo.getid())+" -> "+Nuevo.getnombre()+'\"];\n'
            if(Nuevo!=self.cabeza):
                cadena = cadena + 'Node'+str(cont-1)+' -> '+'Node'+str(cont)+';\n'
            Nuevo = Nuevo.siguiente
            cont+=1
        cadena = cadena + '}'
        file.write(cadena)
        file.close()
        os.system('dot -Tpng grafica.dot -o grafica.png')
        os.startfile("grafica.png")


Nuevo = Lista()
Nuevo.agregar(1, "hola")
Nuevo.agregar(1, "otro")
Nuevo.agregar(3, "cinco")
Nuevo.recorrer()
Nuevo.graficar()