class Nodo:
    def __init__(self, id, nombre):
        self.__id = id
        self.__nombre = nombre
        self.siguiente = None

    def getid(self):
        return self.__id

    def getnombre(self):
        return self.__nombre

    def setid(self, id):
        self.__id = id

    def setnombre(self, id):
        self.__nombre = id
