
import os
from Nodo import Nodo

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
            self.cabeza = self.cola = Nuevo
            self.cola.siguiente = self.cabeza
        else:
            Nuevo.siguiente = self.cabeza
            self.cabeza.anterior = Nuevo
            self.cabeza = Nuevo
        self.unirnodos()

    def unirnodos(self):
        self.cabeza.anterior = self.cola
        self.cola.siguiente = self.cabeza

    #------------------------- Metodo para Recorrer la Lista --------------------------------------------
    def Recorrer(self):
        aux = self.cabeza
        while (aux):
            print(aux.dato)
            aux = aux.siguiente
            if aux== self.cabeza:
                break

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
                cadena = cadena + 'Node'+str(cont)+' -> '+'Node'+str(cont-1)+';\n'
            cont+=1
            aux = aux.siguiente
        cadena = cadena + 'Node'+str(cont)+'[label=\"'+aux.dato+'\"];\n'
        cadena = cadena + 'Node'+str(cont-1)+' -> '+'Node'+str(cont)+';\n'
        cadena = cadena + 'Node'+str(cont)+' -> '+'Node'+str(cont-1)+';\n'
        cadena = cadena + 'Node'+str(cont)+' -> '+'Node'+str(0)+';\n'
        cadena = cadena + 'Node'+str(0)+' -> '+'Node'+str(cont)+';\n'
        cadena = cadena + '}'
        file.write(cadena)
        file.close()
        os.system('dot -Tpng grafica.dot -o grafica.png')
        os.startfile("grafica.png")