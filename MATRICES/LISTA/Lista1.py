from ast import If
import os
from Lista2 import ListaCircular2

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.lista = ListaCircular2()
        self.siguiente = None

class ListaCircular:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def vacio(self):
        return self.cabeza==None

    ## ----------------------- Metodo para Ingresar Nodos ------------------------------------------
    def ingresar(self, dato):
        Nuevo = Nodo(dato)
        if self.vacio():
            self.cabeza = Nuevo
        else:
            Nuevo.siguiente = self.cabeza
            self.cabeza = Nuevo
            
    #------------------------- Metodo para Recorrer la Lista --------------------------------------------
    def Recorrer(self):
        aux = self.cabeza
        while (aux!=None):
            print(aux.dato)
            aux = aux.siguiente

    #------------------------- Metodo de llenado de Segunda Lista ---------------------------------------
    def llenar(self, id, data):
        aux = self.cabeza
        while(aux!=None):
            if(aux.dato!=id):
                aux = aux.siguiente
            else:
                aux.lista.ingresar(data)
                break 

    #------------------------- Metodo de recorrido de Segunda Lista y Lista primaria --------------------

    def recorrer2(self):
        aux = self.cabeza
        if (self.vacio()):
            print("La lista esta vacia")
        else:
            while(aux!=None):
                print("-------", aux.dato)
                print(aux.lista.Recorrer())
                aux = aux.siguiente

    #------------------------- Metodo para Graficar Lista --------------------------------------------------
    def graficar(self):
        aux = self.cabeza
        cont = 0
        cadena = ""
        file = open('grafica.dot', 'w')
        cadena = cadena + 'digraph G { \n'
        while(aux.siguiente != self.cabeza):
            cadena = cadena + 'Node'+str(cont)+'[label=\"'+aux.dato+'\"];\n'
            if(aux != self.cabeza):
                cadena = cadena + 'Node'+str(cont-1)+' -> '+'Node'+str(cont)+';\n'
            cont+=1
            aux = aux.siguiente
        cadena = cadena + 'Node'+str(cont)+'[label=\"'+aux.dato+'\"];\n'
        cadena = cadena + 'Node'+str(cont-1)+' -> '+'Node'+str(cont)+';\n'
        cadena = cadena + 'Node'+str(cont)+' -> '+'Node'+str(0)+';\n'
        cadena = cadena + '}'
        file.write(cadena)
        file.close()
        os.system('dot -Tpng grafica.dot -o grafica.png')
        os.startfile("grafica.png")