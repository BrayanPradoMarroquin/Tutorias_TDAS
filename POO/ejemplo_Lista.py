class Nodo:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.siguiente = None

class Lista:
    def __init__(self):
        self.inicio = None
        self.final = None

    def vacio(self):
        return self.inicio == None
    
    def insertar(self, id, nombre):
        nuevo = Nodo(id, nombre)
        if self.vacio():
            self.inicio = nuevo
            self.final = self.inicio
            self.inicio.siguiente = self.inicio
            self.inicio.siguiente = self.final
        else:
            self.final.siguiente = nuevo
            nuevo.siguiente = self.inicio
            self.final = self.inicio

    def buscar(self, id):
        actual = self.inicio
        puntero = False
        while(puntero==False):
            if(actual.id==id):
                return actual
            elif (actual.siguiente==self.inicio):
                print("No existe el dato en la Lista")
                puntero=True
            else:
                actual = actual.siguiente
