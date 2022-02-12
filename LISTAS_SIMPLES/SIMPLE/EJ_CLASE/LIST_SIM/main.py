import imp
from List import Lista

ListNew = Lista()
ListNew.Insertar(1, "Juan")
ListNew.Insertar(2, "Pedro")
ListNew.Insertar(3, "Pedro")
ListNew.recorrer()
ListNew.graficar()
ListNew.eliminar(2)
ListNew.recorrer()