import os
from Nodo import Nodo

class ArbolABB:
    def __init__(self):
        self.raiz = None

    def vacio(self):
        return self.raiz == None
    
    def agregar(self, id):
        self.raiz = self.agregarinterno(id, self.raiz)

    def agregarinterno(self, id, raiz):
        if raiz==None:
            return Nodo(id)
        else:
            if id< raiz.id:
               raiz.izquierda = self.agregarinterno(id, raiz.izquierda)
            elif id>raiz.id:
                raiz.derecha = self.agregarinterno(id, raiz.derecha)
        return raiz

    def PreOrden(self, root):
        self.PreOrdenInterno(root)

    def PreOrdenInterno(self, root):
        if root!=None:
            self.PreOrdenInterno(root.izquierda)
            print(root.id, end="\n")
            self.PreOrdenInterno(root.derecha)

    def PostOrden(self, root):
        self.PostOrdenInterno(root)

    def PostOrdenInterno(self, root):
        if root!=None:
            self.PostOrdenInterno(root.derecha)
            print(root.id, end="\n")
            self.PostOrdenInterno(root.izquierda)

    def InOrden(self, root):
        self.InOrdenInterno(root)

    def InOrdenInterno(self, root):
        if root!=None:
            print(root.id, end="\n")
            self.InOrdenInterno(root.derecha)
            self.InOrdenInterno(root.izquierda)

    def graficar(self, raiz):
        file = open("Arbol.dot", 'w')
        file.write("digraph G { \n")
        file.write("rankdir=TB; \n")
        file.write("node [shape = record, color=black , style=filled, fillcolor=gray93];\n")        
        file.write(self.graficadora(raiz))
        file.write("} \n")
        file.close()
        os.system("dot -Tpng Arbol.dot -o Arbol.png")
        os.startfile("Arbol.png")

    def graficadora(self, root):
        cadena =""
        if(root.derecha==None) & (root.izquierda==None):
            cadena = "nodo"+str(root.id)+"[label =\" "+str(root.id) + "\"]; \n"
        else:
            cadena = "nodo"+str(root.id)+"[label =\"<C0>| "+str(root.id) + "|<C1> \"]; \n"

        if(root.izquierda!=None):
            cadena = cadena + self.graficadora(root.izquierda)+"nodo"+str(root.id)+":C0->nodo"+str(root.izquierda.id)+"\n"
        if(root.derecha!=None):
            cadena = cadena + self.graficadora(root.derecha)+"nodo"+str(root.id)+":C1->nodo"+str(root.derecha.id)+"\n"
        
        return cadena