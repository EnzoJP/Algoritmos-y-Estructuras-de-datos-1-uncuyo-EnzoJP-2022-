from linkedlist import *
import random

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

def MergeSort(L):
	OrdList=LinkedList()
	OrdList=MergeSortR(L,OrdList)
	return OrdList
def MergeSortR(L,OrdList):
	if L.head is not None:
		List1=LinkedList()
		List2=LinkedList()
		Pivote=0
		Pivote=PivoteF(L,Pivote)
		current=L.head
		#divide la lista
		while current.value is not Pivote:
			insert(List1,current.value,length(List1))
			current=current.nextNode
		while current is not None:
			insert(List2,current.value,length(List2))
			current=current.nextNode
		#si no es de un elemento sigo
		if length(List1)>1:
			MergeSortR(List1,OrdList)
		if length(List2)>1:
			MergeSortR(List2,OrdList)
		return Merge(List1,List2,OrdList)
def Merge(L,R,newList):
	currentL = L.head
	currentR = R.head
	newList=LinkedList()
	while currentL != None and currentR != None:
		if currentL.value < currentR.value:
			insert(newList,currentL.value,length(newList))
			currentL = currentL.nextNode
		else:
			insert(newList,currentR.value,length(newList))
			currentR = currentR.nextNode
	if currentL == None:
		while currentR != None:
			insert(newList,currentR.value,length(newList))
			currentR = currentR.nextNode
	else:
		while currentL != None:
			insert(newList,currentL.value,length(newList))
			currentL = currentL.nextNode
	return(newList)

