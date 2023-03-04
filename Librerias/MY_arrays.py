from ALGO1 import *
def leevector(vector,dim):
  #llena el vector
    for i in range(0,dim):
      vector[i]=input_int(f"ingrese el valor {i+1}: ")
    return vector
def Check (dim1,dim2):
    #controlar dimensiones
  checkdim=0
  while checkdim==0:
    dim1 = input_int("Ingrese el tamaño del vector1  ")
    dim2 = input_int("Ingrese el tamaño del vector2  ")
  if dim1<=0 and dim2<=0:
    print("invalido")
  elif dim1 != dim2:
    print("No coinciden")
  else:
    checkdim=1 
    

def leematriz(matriz,dimf,dimc):
  #llena la matriz
  for i in range(0,dimf):
    for j in range(0,dimc):
      matriz[i][j]=input_int(f"ingrese el valor({i+1},{j+1})")
  return matriz
def mostrarvect (vecresult):
  #muestra el vector
  print(vecresult)
def iniciarvec(vecresult,dimc):
  #inicializo el vector con 0
  for k in range (0,dimc):
    vecresult[k]=0
def muestramat(matrizresult):
  #imprime la matriz
  for i in range(0,dimf):
    for j in range(0,dimc):
      print(matrizresult[i][j],end=" ")
    print()

def transpuesta(matriz):
  #devuelve una matriz transpuesta
  Matransp=Array(len(matriz),Array(len(matriz[0]),0))
  for i in range(len(matriz[0])):
        for j in range(len(matriz)):
            Matransp[i][j] = matriz[j][i]
  return Matransp

def Multmatrices(matriz1,matriz2):
  matresult=Array(len(matriz1),Array(len(matriz2[0]),0))
  if len(matriz1[0])==len(matriz2):
    for i in range(0,len(matriz1)):
      for j in range(0,len(matriz2[0])):
        for k in range(0,len(matriz2)):
          matresult[i][j] += matriz1[i][k]*matriz2[k][j]
  return matresult    
