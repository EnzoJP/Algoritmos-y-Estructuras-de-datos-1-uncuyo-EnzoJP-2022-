#Palau Enzo
#enzoopalau@gmail.com
#13686

from binarytree import *
import linkedlist 


def findCommonAncestor(Tree,NodoA,NodoB):
	#Devulevo None si no tiene y el value si tiene ancestro comun
	current=Tree.root
	estan=False
	prim=False
	seg=False
	prim=buscaNodo(Tree,NodoA,current,prim)
	seg=buscaNodo(Tree,NodoB,current,seg)
	if prim==True and seg==True:
		estan=True
	if estan==False:
		return None
	else:
		current=Tree.root
		ListaAux=linkedlist.LinkedList()
		List1=findCommonAncestorR(Tree,NodoA,current,ListaAux)
		current=Tree.root
		List2=findCommonAncestorR(Tree,NodoB,current,ListaAux)
		Ancestro=None
		Ancestro=comparoYvenzo(List1,List2,Tree)
		return Ancestro

def buscaNodo(Tree,nodo,current,esta):
	if current is not None:
		if current.key==nodo.key:
			esta=True
		esta=buscaNodo(Tree,nodo,current.leftnode,esta)
		esta=buscaNodo(Tree,nodo,current.rightnode,esta)
	return esta

def findCommonAncestorR(Tree,Nodo,current,List):
	if current is not None:
		if current.key==Nodo.key:
			List=ListaParent(Tree,current,List)
			return List
		List=findCommonAncestorR(Tree,Nodo,current.leftnode,List)
		List=findCommonAncestorR(Tree,Nodo,current.rightnode,List)
	return List

def ListaParent(Tree,current,List):
	List=linkedlist.LinkedList()
	while current is not Tree.root:
		current=current.parent
		linkedlist.insert(List,current.key,linkedlist.length(List))
	return List

def comparoYvenzo(List1,List2,Tree):
	Ancestro=None
	for i in range(0,length(List1)):
		for j in range(0,length(List2)):
			if linkedlist.access(List1,i)==linkedlist.access(List2,j):
				Ancestro=linkedlist.access(List1,i)
				Ancestro=access(Tree,Ancestro)
				return Ancestro
	return Ancestro