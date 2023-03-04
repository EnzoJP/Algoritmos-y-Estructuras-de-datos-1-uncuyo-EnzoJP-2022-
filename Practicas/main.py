from binarytree import *
import linkedlist 

#Ancestro__________________________________________

def findCommonAncestor(B,NodoB,NodoA):
	current=B.root
	estan=False
	prim=False
	seg=False
	prim=buscaNodo(B,NodoA,current,prim)
	seg=buscaNodo(B,NodoB,current,seg)
	if prim==True and seg==True:
		estan=True
	if estan==False:
		return None
	else:
		current=B.root
		ListaAux=linkedlist.LinkedList()
		List1=findCommonAncestorR(B,NodoA,current,ListaAux)
		current=B.root
		List2=findCommonAncestorR(B,NodoB,current,ListaAux)
		Ancestro=None
		Ancestro=comparoYvenzo(List1,List2,B)
		return Ancestro

def buscaNodo(B,nodo,current,esta):
	if current is not None:
		if current.value==nodo.key:
			esta=True
		esta=buscaNodo(B,nodo,current.leftnode,esta)
		esta=buscaNodo(B,nodo,current.rightnode,esta)
	return esta

def findCommonAncestorR(B,Nodo,current,List):
	if current is not None:
		if current.value==Nodo.key:
			List=ListaParent(B,current,List)
			return List
		List=findCommonAncestorR(B,Nodo,current.leftnode,List)
		List=findCommonAncestorR(B,Nodo,current.rightnode,List)
	return List

def ListaParent(B,current,List):
	List=linkedlist.LinkedList()
	while current.parent is not B.root:
		current=current.parent
		linkedlist.insert(List,current.key,linkedlist.length(List))
	return List

def comparoYvenzo(List1,List2,B):
	Ancestro=None
	for i in range(0,length(List1)):
		for j in range(0,length(List2)):
			if linkedlist.access(List1,i)==linkedlist.access(List2,j):
				Ancestro=linkedlist.access(List1,i)
				Ancestro=access(B,Ancestro)
				return Ancestro
	return Ancestro

#_________________________________________






B=BinaryTree()
insert(B,8,8);insert(B,3,3);insert(B,10,10);insert(B,1,1);insert(B,6,6)
insert(B,14,14);insert(B,4,4);insert(B,7,7);insert(B,13,13)
a=traverseBreadFirst(B)
printList(a)

NodoA=BinaryTreeNode()
NodoB=BinaryTreeNode()
NodoA.key=2;NodoA.value=9
NodoB.key=6;NodoA.value=12
