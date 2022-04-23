from re import A
from ABB import ArbolABB

Nuevo = ArbolABB()

Nuevo.agregar(3)
Nuevo.agregar(2)
Nuevo.agregar(4)
Nuevo.agregar(1)
Nuevo.agregar(5)
Nuevo.PreOrden(Nuevo.raiz)
print("-------------------------------------------")
Nuevo.PostOrden(Nuevo.raiz)
print("-------------------------------------")
Nuevo.InOrden(Nuevo.raiz)
Nuevo.graficar(Nuevo.raiz)