from linkedlist import *
#ORDENAMIENTOS BASICOS DE VECTORES(LISTAS) DE MENOR A MAYOR

def BubbleSort(L):
	Long=length(L)
	Long2=Long
	for j in range(0,Long2):
		for i in range (0,Long-1):
			if access(L,i)>access(L,i+1):
				move(L,i,i+1)
				#esta funcion mueve los nodos completos
		Long=Long-1
	return L
	
def SelectionSort(L):
	Long=length(L)
	Long2=Long
	for j in range(0,Long2):
		menor=access(L,j)
		posc=None
		for i in range (j,Long):
			if access(L,i)<=menor:
				menor=access(L,i)
				posc=i
		#esta funcion mueve los nodos completos
		move(L,posc,j)
	return L

def InsertionSort(L):
	for i in range (1,length(L)):
		PosMin=None
		printList(L)
		for j in range(i,0,-1):
			if access(L,i)<=access(L,j):
				PosMin=j
		move(L,i,PosMin)
		#esta funcion mueve los nodos completosS
	return L

L=LinkedList()
add(L,1223);add(L,123);add(L,23);add(L,324);add(L,145)
add(L,62);add(L,64213);add(L,1);add(L,1)
printList(L)

print("A")

b=SelectionSort(L)
printList(b)
