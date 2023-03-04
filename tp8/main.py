from ALGO1 import *
from linkedlist import *
from mystack import *

def sumaEnterosRecursiv(valor):
  #suma enteros hasta ese numero
  if valor < 0:
    print("Error no es positivo")
    return None
  elif valor==0:
    return valor
  else:
    return valor+sumaEnterosRecursiv(valor-1)
  
def fibonacci(valor):
  #calcula el termino n-esimo de Fibonacci
  if valor <=1: 
    return valor
  else:
    return fibonacci(valor-1)+fibonacci(valor-2)
    
def sumaPares(valor):
  #suma los pares hasta 2
  if valor%2!=0 or valor==0:
    print("Error numero incorrecto")
    return None
  if valor==2:
    return valor
  if valor%2==0:
    return valor+sumaPares(valor-2)

def ordenaLista(L,position_orig,position_dest):
  #caso base
  if position_dest==length(L):
    return 
  #ordena de menor a mayor una lista
  current=L.head
  for i in range(0,position_dest):
    current=current.nextNode
  menor=current.value
  while current!=None:
    if current.value<=menor:
      menor=current.value
    current=current.nextNode
  cont=0
  current=L.head
  while current!=None:
    if current.value==menor:
      position_orig=cont
    cont+=1
    current=current.nextNode
  #bloque de mover
  if position_orig==0:
    insert(L,menor,position_dest)
  else:
    if position_orig != None:
      current=L.head
      for i in range(0,length(L)-1):
        if i==position_orig-1:
           current.nextNode=current.nextNode.nextNode
        current=current.nextNode
    else:
      return None  
    insert(L,menor,position_dest)
  return ordenaLista(L,position_orig,position_dest+1)

def PCfibonacci(valor):
  L=LinkedList
  push(L,0)
  push(L,1)
  suma=0
  for i in range (1,valor):
    current=pop(L)
    previous=pop(L)
    suma=current+previous
    push(L,current)
    push(L,suma)
  result=pop(L)
  return result

valor=input_int("Dame un numero entero :)")
a=sumaEnterosRecursiv(valor)
print("La suma de los enteros es: ",a)
res=sumaPares(valor)
print("la suma de los pares es: ",res)
f=fibonacci(valor)
print("El resultado del num de fibonacci es: ",f)

A=LinkedList()  
add(A,1)
add(A,2)
add(A,3)
add(A,4)
add(A,5)
add(A,6)
add(A,6)
add(A,213)
add(A,6)
add(A,7)
print("lista orginal")
printList(A)
print("lista de menor a mayor ")
ordenaLista(A,0,0)
printList(A)
fpc=PCfibonacci(valor)
print("Fibonacci con pilas ",fpc) 