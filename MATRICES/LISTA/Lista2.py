import os

class Nodo2:
    def __init__(self, dato):
        self.dato = dato
        self.lista = None
        self.siguiente = None

class ListaCircular2:
    def __init__(self):
        self.cabeza = None

    def vacio(self):
        return self.cabeza==None

    ## ----------------------- Metodo para Ingresar Nodos ------------------------------------------
    def ingresar(self, dato):
        Nuevo = Nodo2(dato)
        if self.vacio():
            self.cabeza = Nuevo
        else:
            Nuevo.siguiente = self.cabeza
            self.cabeza = Nuevo

    #------------------------- Metodo para Recorrer la Lista --------------------------------------------
    def Recorrer(self):
        aux = self.cabeza
        if(self.vacio()):
            print("La lista se encuentra vacia")
        else:
            while (aux!=None):
                print(aux.dato)
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