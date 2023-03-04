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
def QuickSort(L):
	OrdList=LinkedList()
	OrdList=QuickSortR(L,OrdList)
	return OrdList
def QuickSortR(L,OrdList):
	if L.head is not None:
		List1=LinkedList()
		List2=LinkedList()
		Pivote=0
		Pivote=PivoteF(L,Pivote)
		current=L.head
		#divide la lista
		while current is not None:
			if current.value<Pivote:
				insert(List1,current.value,length(List1))
			if current.value>=Pivote:
				insert(List2,current.value,length(List2))
			current=current.nextNode
		#si es de un elemento los uno sino sigo
		if length(List1)>1:
			QuickSortR(List1,OrdList)
		elif length(List1)==1:
			insert(OrdList,List1.head.value,length(OrdList))
		if length(List2)>1:
			QuickSortR(List2,OrdList)
		elif length(List2)==1:
			insert(OrdList,List2.head.value,length(OrdList))
	return OrdList
	
def PivoteF(L,Pivote):
	#saca el pivote de una lista
	PivotePos=random.randint(0,length(L)-1)
	Pivote=access(L,PivotePos)
	return Pivote 
