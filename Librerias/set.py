from ALGO1 import *

def Create_set(array):
  #Crea un TAD de tipo Set
  cont=0
  for i in range(0,len(array)):
    for j in range(0,len(array)):
      if i != j:
        if array[j]==array[i] and array[j] != None :
          array[j]=None
  for k in range(0,len(array)):
    if array[k]==None:
      cont += 1
  vectorSet=Array((len(array)-cont),0)
  j=-1 #para que empieze de cero
  for i in range(0,len(array)):
    if array[i] != None:
      j+=1
      vectorSet[j]=array[i]

  return vectorSet

def check_duplicates(array):
  #verifique si hay o no duplicados en los Array
  duplic=0
  for i in range(0,len(array)):
    for j in range(0,len(array)):
      if i != j:
        if array[i] == array[j]:
          duplic+=1
  if duplic>=1:
    print("hay duplicados")
    return True
  else:
    return False
def Union(arrayS,arrayT):
  #Aplica la operación UNIÓN sobre los conjuntos
  vectorU=Array(len(arrayS)+len(arrayT),0)
  for i in range(0,len(arrayS)):
    vectorU[i]=arrayS[i]
  for j in range(0,len(arrayT)):
    vectorU[j+len(arrayS)]=arrayT[j]
  return Create_set(vectorU)
def Intersection(arrayS,arrayT):
  #Aplica la operación INTERSECCIÓN sobre los conjuntos
  iguales=0
  k=0
  for i in range(0,len(arrayS)):
    for j in range(0,len(arrayT)):
      if arrayS[i]==arrayT[j]:
        iguales+=1
  vectorI=Array(iguales,0)
  for i in range(0,len(arrayS)):
    for j in range(0,len(arrayT)):
      if arrayS[i]==arrayT[j]:
        vectorI[k]=arrayT[j]#coloco cualquiera ya es el mismo valor
        k+=1
  return vectorI
def Difference(arrayS,arrayT):
  #Aplica la operación DIFERENCIA en los conjuntos (A-B)
  vectorD=Array(len(arrayS)+len(arrayT),0)
  vectorD=arrayS
  for i in range(0,len(arrayS)):
    for j in range(0,len(arrayT)):
      if arrayS[i]==arrayT[j]:
        vectorD[i]=None
  return Create_set(vectorD)