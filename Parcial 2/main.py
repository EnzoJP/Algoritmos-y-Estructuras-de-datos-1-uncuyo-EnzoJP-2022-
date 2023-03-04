# vim: set tabstop=4 shiftwidth=4 expandtab   
import sys
#sys.path.append('ejercicio1')
sys.path.append('ejercicio2')
import unittest
from linkedlist import length,LinkedList,add,update,insert
from ejercicio2 import calculate_expression

class TestExamen4(unittest.TestCase):
    def setUp(self):
        pass

    def test_calculate_expression_1(self):
        """ -- Verifica suma y multiplicacion
        """
        L=LinkedList()
        insert(L,"3",length(L))
        insert(L,"+",length(L))
        insert(L,"3",length(L))
        insert(L,"*",length(L))
        insert(L,"2",length(L))
        self.assertEqual(calculate_expression(L),9)


    def test_calculate_expression_producto_cociente(self):
        """ -- Verifica operaciones con productos y cocientes
        """
        L=LinkedList()
        insert(L,"2",length(L))
        insert(L,"*",length(L))
        insert(L,"3",length(L))
        insert(L,"/",length(L))
        insert(L,"2",length(L))
        self.assertEqual(calculate_expression(L),3)

    def test_calculate_expression_producto_cociente_real(self):
        """ -- Verifica que el conciente se trunque 
        """
        L=LinkedList()
        insert(L,"3",length(L))
        insert(L,"*",length(L))
        insert(L,"3",length(L))
        insert(L,"/",length(L))
        insert(L,"2",length(L))
        self.assertEqual(calculate_expression(L),4)


if __name__=="__main__":
    unittest.main(verbosity=3)
