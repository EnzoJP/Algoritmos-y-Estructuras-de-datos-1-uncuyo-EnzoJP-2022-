from linkedlist import *

def push(S,element):
  #Agrega un elemento al comienzo
  add(S,element)
def pop(S):
  #extrae el primer elemento de la pila
  if S.head!=None:
    current=S.head
    element=S.head.value
    S.head=current.nextNode
    return element
  else:
    return None