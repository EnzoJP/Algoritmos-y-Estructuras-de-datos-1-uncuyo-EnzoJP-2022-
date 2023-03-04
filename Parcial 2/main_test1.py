# vim: set tabstop=4 shiftwidth=4 expandtab   
import sys
sys.path.append('ejercicio1')
from linkedlist import length,LinkedList,add,update,insert,access

# Se define una nueva estructura BinaryTree
class BinaryTreeT:
    root=None

# Se define una nueva estructura BinaryTreeNode
class BinaryTreeNodeT:
        parent = None 
        leftnode=None
        rightnode=None
        key = None
        value=None
 
# Agregar un elemento al arbol dado una clave y un valor
# - se construye el nodo y se llama a InsertNode la funcion recursiva que realiza la insercion

def insertT(btree,value,key):
    node=BinaryTreeNodeT()
    node.key=key
    node.value=value
    # chequeo si es el nodo root
    if btree.root==None:
        btree.root=node
    else:
        # verifico si ya existe
        res=accessT(btree,key)
        if res!=None:
            return None
        else:
            insertNodeT(btree.root,node)
    return node

def insertNodeT(root,node):
    currentNode=root
    if node.key < currentNode.key :
        if currentNode.leftnode!=None:
            insertNodeT(currentNode.leftnode,node)
        else:
            node.parent=currentNode
            currentNode.leftnode=node
    else:
        if currentNode.rightnode!=None:
            insertNodeT(currentNode.rightnode,node)
        else:
            node.parent=currentNode
            currentNode.rightnode=node
    
# buscar el nodo que contiene la key
def accessNodeT(root,key):
    currentNode=root
    
    if not currentNode:
        return None
    elif currentNode.key == key:
        return currentNode
    elif key < currentNode.key:
        return accessNodeT(currentNode.leftnode,key)
    else:
        return accessNodeT(currentNode.rightnode,key)

# Devolver el valor del nodo que contiene la key y None en caso contrario.
def accessT(btree,key):
    if btree.root==None:
        return None
    else:
        node=accessNodeT(btree.root,key)
        if node != None:
            return(node)
        else:
            return None

# atravezamos el arbol en  Orden
def traverseinOrderT(B):
    L=LinkedList()
    traverseinOrderRT(L,B.root)
    return L

def traverseinOrderRT(L,root):
    if root !=None:
        currentNode=root
        traverseinOrderRT(L,currentNode.rightnode)
        insert(L,currentNode.key,length(L))
        #print("[",currentNode.key, ",",currentNode.value,"]",end=',')
        traverseinOrderRT(L,currentNode.leftnode)
    
from ejercicio1 import findCommonAncestor
import unittest

class TestExamen4(unittest.TestCase):
    def setUp(self):
        pass

    def test_ancestor_parent(self):
        """ -- caso de padre comun
        """
        B=BinaryTreeT()
        a=[10,5,20,2,8,15,25]
        for i in a:
          insertT(B,i,i)
        #L=traverseinOrderT(B)

       # for i in range(0,length(L)):
       #     print(access(L,i),end=" ")

        nodoA=accessT(B,2)
        nodoB=accessT(B,8)

        self.assertEqual(findCommonAncestor(B,nodoA,nodoB),5)


    def test_ancestor_grandparent(self):
        """ -- caso de abuelo comun
        """
        B=BinaryTreeT()
        a=[10,5,20,2,8,15,25]
        for i in a:
          insertT(B,i,i)
        #L=traverseinOrderT(B)

        #for i in range(0,length(L)):
        #    print(access(L,i),end=" ")

        nodoA=accessT(B,2)
        nodoB=accessT(B,25)

        self.assertEqual(findCommonAncestor(B,nodoA,nodoB),10)

    def test_ancestor_root(self):
        """ -- caso de raiz como parametro 
        """
        B=BinaryTreeT()
        a=[10,5,20,2,8,15,25]
        for i in a:
          insertT(B,i,i)
        #L=traverseinOrderT(B)

        nodoA=accessT(B,B.root.value)
        nodoB=accessT(B,25)

        self.assertEqual(findCommonAncestor(B,nodoA,nodoB),None)
    
    def test_ancestor_not_found(self):
        """ -- caso no existe ancestro
        """
        B=BinaryTreeT()
        a=[10,5,20,2,8,15,25]
        for i in a:
          insertT(B,i,i)
        #L=traverseinOrderT(B)
        nodoA=BinaryTreeNodeT()
        nodoA.value=200
        nodoA.key=200
        nodoB=accessT(B,25)
        self.assertEqual(findCommonAncestor(B,nodoA,nodoB),None)





if __name__=="__main__":
    unittest.main(verbosity=3)
