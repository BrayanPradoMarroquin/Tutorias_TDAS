from Matriz import Matriz_O

fila = 3
columna = 3
Matrix = Matriz_O()
dato ="BBW WWB BWW"
##lista = list()
#cont =0
for i in dato:
##lista.append(cont, i)
#cont+=1
    print(i)

lista = list(dato)

##cont=0

for i in range(1,fila+1):
    for j in range(1,columna+1):
        ##Matrix.ingresardatos(lista.pop(cont),i,j)
        ##cont+=1
        Matrix.ingresardatos(lista.pop(0),i,j)
        print(str(i)+" ",str(j)+" ",str(i+j))
print("------------------------------------------------------------")
print(Matrix.mostrarMatriz())