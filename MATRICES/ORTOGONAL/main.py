from Matriz import Matriz_O

fila = 5
columna = 6
Matrix = Matriz_O()

for i in range(1,fila+1):
    for j in range(1,columna+1):
        Matrix.ingresardatos(str(i+j),i,j)
        print(str(i)+" ",str(j)+" ",str(i+j))

print("------------------------------------------------------------")
print(Matrix.mostrarMatriz())