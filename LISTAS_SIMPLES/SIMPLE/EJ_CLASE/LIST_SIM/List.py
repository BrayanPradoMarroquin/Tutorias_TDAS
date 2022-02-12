import os
from Nodo import Nodo

class Lista:
    def __init__(self):
        self.inicio = None

    
    def vacio(self):
        return self.inicio == None


    def Insertar(self, id, nombre):
        nuevo = Nodo(id, nombre)
        if self.vacio():
            self.inicio = nuevo
        else:
            nuevo.siguiente = self.inicio
            self.inicio = nuevo
    
    def recorrer(self):
        actual = self.inicio
        while(actual!=None):
            print(str(actual.getid())+" --- "+actual.getnombre())
            actual = actual.siguiente
    
    def eliminar(self, id):
        actual = self.inicio
        anterior = None
        while(actual!=None):
            if(actual.getid()==id):
                anterior.siguiente = actual.siguiente
                break
            else:
                anterior = actual
                actual = actual.siguiente

    def graficar(self):
        Nuevo = self.inicio
        cont = 0
        cadena = ""
        file = open('grafica.dot', 'w')
        cadena = cadena + 'graph G { \n'
        while(Nuevo!=None):
            cadena = cadena + 'Node'+str(cont)+'[label=\"'+str(Nuevo.getid())+" -> "+Nuevo.getnombre()+'\"];\n'
            if(Nuevo!=self.inicio):
                cadena = cadena + 'Node'+str(cont-1)+' -- '+'Node'+str(cont)+';\n'
            Nuevo = Nuevo.siguiente
            cont+=1
        cadena = cadena + '}'
        file.write(cadena)
        file.close()
        os.system('dot -Tpng grafica.dot -o grafica.png')
        os.startfile("grafica.png")