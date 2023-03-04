from linkedlist import *

def sub(Lsub,current):
	#insert(Lsub,"[]",length(Lsub))
	laux=LinkedList()
	while current is not None:
		insert(laux,f"[{current.value}]",length(laux))
		current=current.nextNode
	printList(laux)
	current=Lsub.head
	subR(Lsub,current,laux)
def subR(Lsub,current,laux):
	if current is not None:
		for i in range (1,length(Lsub)):
			insert(laux,f"[{current.value},{access(Lsub,i)}]",length(laux))
		printList(laux)

		subR(Lsub,current.nextNode,laux)
"""
def potencia(Lsub,r):

    if length(Lsub) == 0:
        return [[]]
    r = potencia(access(Lsub,0),r)
    printList(r)
    return r + [s + [acces(Lsub,0)] for s in r]
"""

def subset(L):
  subL = LinkedList()
  subSetR(L.head, subL.head, subL) 
  add(subL, "{}")
  #revert (subL)
  return subL
def subSetR(current, subLnode, subL):
  if current == None:
    return
  if subLnode == None: # paso por todo subLnode
    add(subL, f"{current.value}") 
    return subSetR (current.nextNode, subL.head, subL)
  # le quedan subLnodes por pasar 
  add(subL, f"{subLnode.value}, {current.value}")
  return subSetR (current, subLnode.nextNode, subL)


Lsub=LinkedList()
add(Lsub,3)
add(Lsub,2)
add(Lsub,1)

current=Lsub.head
sub(Lsub,current)
Lsub=subset(Lsub)
printList(Lsub)




