from linkedlist import *

class PriorityQueue:
  head=None
class PriorityNode:
  value=None
  nextNode=None
  priority=None


def enqueue_priority(Q,element,priority):
  #Agrega un elemento a Q con la prioridad
  add(Q,element)
  Q.head.priority=priority
  posc=0
  return posc
def dequeue_priority(Q):
#extrae el primer elemento de la cola Q con la mayor prioridad
  Long=length(Q)
  posc=0
  if Long==0:
    return None
  else:
    element=Q.head.value
    mayor=Q.head.priority
    current=Q.head
    for i in range(0,Long):
      if current.priority>=mayor:
        mayor=current.priority
        posc=i
        element=current.value
      current=current.nextNode 
    if posc==0:
      delete(Q,element)
    else:
      current=Q.head
      for i in range (0,posc-1):
        current=current.nextNode
      current.nextNode=current.nextNode.nextNode
    return element

      
      