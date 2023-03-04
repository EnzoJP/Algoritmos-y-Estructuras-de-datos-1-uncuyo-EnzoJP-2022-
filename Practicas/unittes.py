# vim: set tabstop=4 shiftwidth=4 expandtab   
import sys
sys.path.append('ejercicio1')
sys.path.append('ejercicio2')
import unittest
from linkedlist import length,LinkedList,add,update,insert,printList
#from ejercicio2 import Calculate_expression
from permu import isPermutation3
from ejoper import Calculate_expression

class TestExamen4(unittest.TestCase):
    def setUp(self):
        pass

    def test_1_permutation_equal(self):
        """ -- Verifica que una lista del mismo tamaño sea permutacion de la otra
        """
        L=LinkedList()
        S=LinkedList()
        for a in range(97,97+10):
            add(S,a)
        for a in range(97+9,96,-1):
            add(L,a)
        printList(L)
        printList(S)

        self.assertEqual(isPermutation3(L,S),True)

    def test_1_permutation_diff(self):
        """ -- Verifica que una lista del mismo tamaño no sea permutacion de la otra
        """
        L=LinkedList()
        S=LinkedList()
        for a in range(97,97+10):
            add(S,a)
        for a in range(97+9,96,-1):
            add(L,a)
        update(S,109,5)
        update(L,50,5)
        self.assertEqual(isPermutation3(L,S),False)

    def test_1_permutation_length(self):
        """ +-------+  Verifica que una lista de distinto tamaño no sea permutacion de la otra
        """
        L=LinkedList()
        S=LinkedList()
        for a in range(97,97+11):
            add(S,a)
        for a in range(97+10,97,-1):
            add(L,a)
        self.assertEqual(isPermutation3(L,S),False)

    def test_2_calculate_expression_sum_and_product(self):
        """ -- Verifica suma y multiplicacion
        """
        L=LinkedList()
        insert(L,"3",length(L))
        insert(L,"+",length(L))
        insert(L,"3",length(L))
        insert(L,"*",length(L))
        insert(L,"2",length(L))
        self.assertEqual(Calculate_expression(L),9)


    def test_2_calculate_expression_product_and_quocient(self):
        """ +-------+  Verifica operaciones con productos y cocientes
        """
        L=LinkedList()
        insert(L,"2",length(L))
        insert(L,"*",length(L))
        insert(L,"3",length(L))
        insert(L,"/",length(L))
        insert(L,"2",length(L))
        self.assertEqual(Calculate_expression(L),3)

    def test_2_calculate_expression_product_and_quotient_floatl(self):
        """ -- Verifica que el conciente se trunque cuando el resultado es real
        """
        L=LinkedList()
        insert(L,"3",length(L))
        insert(L,"*",length(L))
        insert(L,"3",length(L))
        insert(L,"/",length(L))
        insert(L,"2",length(L))
        self.assertEqual(Calculate_expression(L),4)


    def test_3_calculate_expression_sum_and_product_v2(self):
        """ -- Verifica suma y multiplicacion VERSION 2
        """
        L=LinkedList()
        insert(L,3,length(L))
        insert(L,"+",length(L))
        insert(L,3,length(L))
        insert(L,"*",length(L))
        insert(L,2,length(L))
        self.assertEqual(Calculate_expression(L),9)


    def test_3_calculate_expression_product_and_quocient_v2(self):
        """ +-------+ Verifica operaciones con productos y cocientes VERSION 2
        """
        L=LinkedList()
        insert(L,2,length(L))
        insert(L,"*",length(L))
        insert(L,3,length(L))
        insert(L,"/",length(L))
        insert(L,2,length(L))
        self.assertEqual(Calculate_expression(L),3)

    def test_3_calculate_expression_product_and_quotient_floatl_v2(self):
        """ -- Verifica que el conciente se trunque cuando el resultado es real VERSION 2
        """
        L=LinkedList()
        insert(L,3,length(L))
        insert(L,"*",length(L))
        insert(L,3,length(L))
        insert(L,"/",length(L))
        insert(L,2,length(L))
        self.assertEqual(Calculate_expression(L),4)




if __name__=="__main__":
    unittest.main(verbosity=0)
