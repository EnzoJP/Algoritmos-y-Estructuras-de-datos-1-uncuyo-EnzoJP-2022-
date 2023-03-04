from ALGO1 import *
from linkedlist import *

# 1) -------------------------------------------------
def deleteRepeat(L):
  #borra los repetidos en una lista
  current=L.head
  while current!=None:
    current2=L.head
    while current2!=None:
      if (current.value==current2.value) and (current!=current2):
        element=current.value
        delete(L,element)
      current2=current2.nextNode
    current=current.nextNode

def intercalaLista (A,B,C):
  #intercala los elementos de dos listas y lo guarda en otra lista
  longR=length(A)+length(B)
  #crea lista vacia
  C.head=Node()
  currentR=C.head
  for i in range(0,longR-1):
    currentR.nextNode=Node()
    currentR=currentR.nextNode
    
  currentR=C.head
  current1=B.head
  current2=A.head
  for i in range(0,length(A)):
    currentR.value=current2.value
    currentR=currentR.nextNode
    currentR.value=current1.value
    currentR=currentR.nextNode
    current1=current1.nextNode
    current2=current2.nextNode
    
def buscaparesList(A,C):
  #borra los pares de una lista en la otra
  element=0
  current=C.head
  for i in range(0,length(C)):
    current2=A.head
    for j in range(0,length(A)):
      if current2.value==current.value and current.value%2==0:
        element=current.value
        delete(C,element)
      current2=current2.nextNode
    current=current.nextNode

def listaimpar(C):
  #crea otra lista y la imprime con los impares de otra
  D=LinkedList()
  current=C.head
  element=0
  while current != None:
    if current.value%2!=0:
      add(D,current.value)
    current=current.nextNode
  printList(D)

def agregaelemtos(A,B):
  #agrega los de otra lista que esten en un rango
  current=B.head
  while current != None:
    if current.value>50 and current.value<100:
      element=current.value
      long=length(A)
      insert(A,element,long)
    current=current.nextNode
# 3) -------------------------------------------------
def printemp(emp):
  #imprime la lista empleados
  current=emp.head
  while current != None:
    print(current.value.nombre,end="-->")
    print(current.value.edad,end=";")
    print(current.value.nroLegajo,end="")
    print("")
    current=current.nextNode

# 4) -------------------------------------------------
def invertList(A):
  #invierte la lista
  current=A.head 
  long=length(A)
  for i in range(0,length(A)):
    element=current.value
    insert(A,element,long)
    current=current.nextNode
    delete(A,element)
    long=long-1

print("1)--------------------------")
A=LinkedList()  
add(A,678)
add(A,3)
add(A,22)
add(A,54)
add(A,345)
add(A,89)
add(A,67)
add(A,3)
add(A,45)
add(A,24)

B=LinkedList()
add(B,33)
add(B,12)
add(B,567)
add(B,234)
add(B,15)
add(B,12)
add(B,59)
add(B,64)
add(B,34)
add(B,46)

C=LinkedList()
print("A")
printList(A)
print("B")
printList(B)
print("intercalada:")
intercalaLista(A,B,C)
printList(C)
print("borra los pares de la lista a")
buscaparesList(A,C)
printList(C)
print("Nueva con impares")
listaimpar(C)
print("sin repetidos lista a")
deleteRepeat (A)
printList(A)
print("agregados los elementos entre 50-100")
agregaelemtos(A,B)
printList(A)
print("2---------------------------")
class LinkedListEmp:
  head=None

class Empleado:
  nombre=None
  edad=None
  nroLegajo=None

class NodeEmp:
  value=Empleado
  nextNode=None
  
emp=LinkedListEmp()

aux=Empleado()
aux.nombre="Eduardo Ángel"
aux.edad=34
aux.nroLegajo=2
insert(emp,aux,length(emp))

aux=Empleado()
aux.nombre="Juan Carlos"
aux.edad=23
aux.nroLegajo=5
insert(emp,aux,length(emp))

aux=Empleado()
aux.nombre="Luis Esteban"
aux.edad=32
aux.nroLegajo=7
insert(emp,aux,length(emp))

aux=Empleado()
aux.nombre="Juan Carlos"
aux.edad=23
aux.nroLegajo=5
insert(emp,aux,length(emp))

aux=Empleado()
aux.nombre="Pedro Agusto"
aux.edad=40
aux.nroLegajo=9
insert(emp,aux,length(emp))

aux=Empleado()
aux.nombre="Luis Esteban"
aux.edad=32
aux.nroLegajo=7
insert(emp,aux,length(emp))

aux=Empleado()
aux.nombre="Pedro Cesar"
aux.edad=45
aux.nroLegajo=8
insert(emp,aux,length(emp))

aux=Empleado()
aux.nombre="Eduardo Ángel"
aux.edad=34
aux.nroLegajo=2
insert(emp,aux,length(emp))

aux=Empleado()
aux.nombre="Luis Esteban"
aux.edad=32
aux.nroLegajo=7
insert(emp,aux,length(emp))

print("Lista de empleados original")
printemp(emp)
print("3---------------------------")
#borra los legajos repetidos
current=emp.head
while current!=None:
    current2=emp.head
    while current2!=None:
      #primero ve el valor y despues el nodo
      if (current.value.nroLegajo==current2.value.nroLegajo) and (current!=current2):
        delete(emp,current.value)
      current2=current2.nextNode
    current=current.nextNode
print("sin duplicados")
printemp(emp)
#agrega el legajo 6
aux=Empleado()
aux.nombre="Ernesto Andrés"
aux.edad=55
aux.nroLegajo=6
insert(emp,aux,length(emp)-1)
print("Lista con el nuevo amigo")
printemp(emp)
#Mover el legajo 9 luego del legajo 8
current=emp.head
while current.nextNode!=None:
  if current.nextNode.value.nroLegajo==8:
    aux=current.value
    posc=search(emp,current.nextNode.nextNode.value)
    insert(emp,aux,posc)
    delete(emp,current.value)
  current=current.nextNode
print("el legajo 9 luego del legajo 8")
printemp(emp)

print("4---------------------------")
print("lista A invertida")
invertList(A)
printList(A)



