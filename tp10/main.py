from binarytree import *
import linkedlist
#--------------------------------------------
def TreeBalance(B):
	#verifica si un árbol binario está balanceado.
	"""retorna False si no es Balanceado/True si lo es.
 """
	balance=True
	current=B.root
	balance=balanceR(B,current,balance)
	return balance
def balanceR(B,current,balance):
	#ve la altura para todos los nodos de su Arbderecho e Arbizq
	#si un nodo no esta balanceado return false
	nivelder=0
	nivelizq=0
	if current!=None:
		nivelizq=maxalt(current.leftnode)
		nivelder=maxalt(current.rightnode)
		if (nivelizq-nivelder==0) or (nivelizq-nivelder==-1) or (nivelizq-nivelder==1):
			#subA balanciado
			pass
		else:
			balance=False	
			return balance
		balance=balanceR(B,current.leftnode,balance)
		balance=balanceR(B,current.rightnode,balance)
	return balance
def maxalt(current):
	#ve la altura de cada sub arbol
    if current == None:
        return 0
    else:
        lalt = maxalt(current.leftnode)
        ralt = maxalt(current.rightnode)
        if (lalt > ralt):
            return lalt+1
        else:
            return ralt+1
	
#--------------------------------------------
def searchSubtree(BT2,BT1):
	#determine si BT2 es un subárbol de BT1.
	"""retorna False si no es SubArb/True si lo es.
 """
	#chequeo de tamaño:
	L1=traverseInPostOrder(BT1)
	L2=traverseInPostOrder(BT2)
	if linkedlist.length(L2)>=linkedlist.length(L1):
		return None
	else:
		current1=BT1.root
		current2=BT2.root
		sub=False
		sub=searchSubtreeR(current1,current2,sub)
	return sub
def searchSubtreeR(current1,current2,sub):
	if (current1 is not None) and (current2 is not None):
		if current1.key==current2.key:
			sub=True
			sub=searchSubtreeR2(current1,current2,sub)
			return sub
		sub=searchSubtreeR(current1.leftnode,current2,sub)
		sub=searchSubtreeR(current1.rightnode,current2,sub)
	return sub

def searchSubtreeR2(current1,current2,sub):
	if (current1 is not None) and (current2 is not None):
		if current1.key!=current2.key:
			sub=False
			return sub
		if current2.leftnode!=None:
			if current1.leftnode!=None:
				sub=searchSubtreeR2(current1.leftnode,current2.leftnode,sub)
			else:
				#mas hijos
				sub=False
				return sub
		if current2.rightnode!=None:
			if current1.rightnode!=None:
				sub=searchSubtreeR2(current1.rightnode,current2.rightnode,sub)
			else:
				#mas hijos
				sub=False
				return sub
	return sub



#--------------------------------------------
def checkBST(B):
	#verifica que un árbol binario es un Árbol Binario de Búsqueda.
	"""retorna False si no es Binario/True si es Binario.
 """
	esBin=True
	current=B.root
	esBin=checkBinaryR(B,current,esBin)
	return esBin
def checkBinaryR(B,current,esBin):
	if current!=None:
		if current.leftnode!=None:
			if current.leftnode.key>=current.key:
				esBin=False
		if current.rightnode!=None:
			if current.rightnode.key<=current.key:
				esBin=False
		esBin=checkBinaryR(B,current.leftnode,esBin)
		esBin=checkBinaryR(B,current.rightnode,esBin)
	return esBin
#--------------------------------------------
B5=BinaryTree()
insert(B5,5,5);insert(B5,3,3);insert(B5,2,2);insert(B5,1,1)
insert(B5,7,7);insert(B5,6,6);insert(B5,4,4);insert(B5,9,9);insert(B5,0,0);insert(B5,-1,-1)

a=TreeBalance(B5)
print(a)