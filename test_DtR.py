import unittest 
from decimal_to_roman import decimal_to_roman
class TestDecimalToRoman(unittest.TestCase):

    def test_1(self): 
        #pre condicón no hay 
        #proceso1
        resultado = decimal_to_roman(1)
        #verificación
        self.assertEqual(resultado, 'I')#Assert verifica 


    def test_2(self):
        resultado = decimal_to_roman(2)
        self.assertEqual(resultado, 'II')

    def test_3(self):
        resultado = decimal_to_roman(3)
        self.assertEqual(resultado, 'III')

    def test_4(self):
        resultado = decimal_to_roman(4)
        self.assertEqual(resultado, 'IV')

    def test_5(self):
        resultado = decimal_to_roman(5)
        self.assertEqual(resultado, 'V')

    def test_6(self):
        resultado = decimal_to_roman(6)
        self.assertEqual(resultado, 'VI')   

    def test_7(self):
        resultado = decimal_to_roman(7)
        self.assertEqual(resultado, 'VII')


    def test_8(self):
        resultado = decimal_to_roman(8)
        self.assertEqual(resultado, 'VIII')

    def test_9(self):
        resultado = decimal_to_roman(9)
        self.assertEqual(resultado, 'IX')

    def test_10(self):
        resultado = decimal_to_roman(10)
        self.assertEqual(resultado, 'X')

    def test_11(self):
        resultado = decimal_to_roman(11)
        self.assertEqual(resultado, 'XI')

    def test_22(self):
        resultado = decimal_to_roman(22)
        self.assertEqual(resultado, 'XXII')

    def test_95(self):
        resultado = decimal_to_roman(95)
        self.assertEqual(resultado, 'XCV')

if __name__ == '__main__':
    unittest.main()