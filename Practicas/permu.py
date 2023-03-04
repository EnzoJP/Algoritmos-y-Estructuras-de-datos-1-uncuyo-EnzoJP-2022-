from linkedlist import *

#una forma__________________________________________

def isPermutation(L1,L2):
	current=L1.head
	cond=True
	current2=L2.head
	cond=permutaR(L1,L2,cond,current2,current)
	return cond
def permutaR(L1,L2,cond,current2,current):
	cond2=False
	valor=current2.value
	if cond is not False:
		current=L1.head
		while current!=None:
			if current.value == valor:
				cond2=True
			current=current.nextNode
	if cond2 is not True:
		cond=False
		return cond
	if current2.nextNode is not None:
		cond=permutaR(L1,L2,cond,current2.nextNode,current)
	return cond

#______________________________________________
def isPermutation3(L1,L2):
	suma1=0
	suma2=0
	if length(L1)!=length(L2):
		return	False
	for i in range (0,length(L1)):
		suma1=suma1+access(L1,i)
	for j in range (0,length(L2)):
		suma2=suma2+access(L2,j)
	print("a",suma1)
	print("a",suma2)
	if suma1==suma2:
		return True
	else:
		return False

def ordenarLista(L):
  #Funcion O(n) de ordenar una lista
  check=False
  for i in range(0,length(L)-1):
    if access(L,i)<access(L,i+1):
      check=True
  for i in range(0,length(L)-1):
    if access(L,i)>access(L,i+1):
      move2(L,i,i+1)
      check=False
  #printList(L)
  if check==False:
    ordenarLista(L)
  else:
    return

def isPermutation2(L,S):
  if length(S)!=length(L):
    return False
  elif L.head==None or S.head==None:
    return print("Al menos una lista ingresada está vacía")
  ordenarLista(L)
  ordenarLista(S)
  #printList(L)
  #printList(S)
  check=True
  for i in range(0,length(L)):
    if access(L,i)!=access(S,i):
      check=False
  return check

def move2(L,posInicio,posFinal):
  #Mover un nodo de un lugar(posInicio) a otro(posFinal)
  element=access(L,posInicio)
  size=length(L)
  if posInicio>=size or posFinal>=size:
    return print("Posiciones no válidas")
  if posInicio>posFinal:
    initialPosition=posInicio
    finalPosition=posFinal
  elif posInicio<posFinal:
    initialPosition=posInicio-1
    finalPosition=posFinal+1
  else:
    return
  insert(L,element,finalPosition)
  current=L.head
  if posInicio==0:
    L.head=current.nextNode
  else:
    for i in range (0,initialPosition):
      current=current.nextNode
    current.nextNode=current.nextNode.nextNode

L1=LinkedList()
L2=LinkedList()
add(L1,23);add(L1,3);add(L1,2);add(L1,4);add(L1,6)
add(L2,2);add(L2,3);add(L2,23);add(L2,4);add(L2,6)
printList(L1)
printList(L2)
L=LinkedList()
insert(L,4,length(L));insert(L,200,length(L));insert(L,0,length(L))
insert(L,87,length(L));insert(L,94,length(L));insert(L,14,length(L))
insert(L,8,length(L));insert(L,25,length(L));insert(L,148,length(L))
printList(L)

S=LinkedList()
insert(S,8,length(S));insert(S,94,length(S));insert(S,200,length(S))
insert(S,14,length(S));insert(S,148,length(S));insert(S,0,length(S))
insert(S,4,length(S));insert(S,87,length(S));insert(S,255,length(S))
printList(S)
# sino tambien la sumatoria deberia dar igual 

print(isPermutation2(L,S))

