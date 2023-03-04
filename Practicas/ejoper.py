from linkedlist import *
import math
def Calculate_expression(L):
	if length(L)>1:
		#mult
		current=L.head
		for i in range(0,length(L)):
				if current.nextNode is not None:
					if current.nextNode.value is "*":
						aux=int(current.nextNode.nextNode.value)
						if current.nextNode.nextNode.nextNode is not None:
							current.nextNode=current.nextNode.nextNode.nextNode
						else:
							current.nextNode=None
						current.value=float(current.value)*aux
					else:
						current=current.nextNode
	if length(L)>1:
		#div
		current=L.head
		for i in range(0,length(L)):
				if current.nextNode is not None:
					if current.nextNode.value is "/":
						aux=int(current.nextNode.nextNode.value)
						if current.nextNode.nextNode.nextNode is not None:
							current.nextNode=current.nextNode.nextNode.nextNode
						else:
							current.nextNode=None
						current.value=float(current.value)/aux
					else:
						current=current.nextNode
	printList(L)
	if length(L)>1:
		#rest
		current=L.head
		for i in range(0,length(L)):
				if current.nextNode is not None:
					if current.nextNode.value is "-":
						aux=int(current.nextNode.nextNode.value)
						if current.nextNode.nextNode.nextNode is not None:
							current.nextNode=current.nextNode.nextNode.nextNode
						else:
							current.nextNode=None
						current.value=float(current.value)-aux
					else:
						current=current.nextNode
	printList(L)
	if length(L)>1:
		#sum
		current=L.head
		for i in range(0,length(L)):
				if current.nextNode is not None:
					if current.nextNode.value is "+":
						aux=int(current.nextNode.nextNode.value)
						if current.nextNode.nextNode.nextNode is not None:
							current.nextNode=current.nextNode.nextNode.nextNode
						else:
							current.nextNode=None
						current.value=float(current.value)+aux
					else:
						current=current.nextNode

	valorFinal=float(L.head.value)
	valorFinal=math.trunc(valorFinal)
	return valorFinal


L=LinkedList()
add(L,"4")
printList(L)
Calculate_expression(L)