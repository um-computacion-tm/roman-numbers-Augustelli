import unittest
from roman_to_decimals import roman_to_decimals
from parameterized import parameterized


class TestRomanToDecimal(unittest.TestCase):
    
    def test_I(self):
        resultado = roman_to_decimals('I')
        self.assertEqual(resultado, 1)

    def test_II(self):
        resultado = roman_to_decimals('II')
        self.assertEqual(resultado, 2)
    
    def test_III(self):
        resultado = roman_to_decimals('III')
        self.assertEqual(resultado,3)

    def test_IV(self):
        resultado = roman_to_decimals('IV')
        self.assertEqual(resultado,4)

    def test_V(self):
        resultado = roman_to_decimals('V')
        self.assertEqual(resultado,5)

    def test_VI(self):
        resultado = roman_to_decimals('VI')
        self.assertEqual(resultado,6)

    def test_VII(self):
        resultado = roman_to_decimals('VII')
        self.assertEqual(resultado,7)


    def test_VIII(self):
        resultado = roman_to_decimals('VIII')
        self.assertEqual(resultado,8)

    def test_IX(self):
        resultado = roman_to_decimals('IX')
        self.assertEqual(resultado,9)
    
    def test_X(self):
        resultado = roman_to_decimals('X')
        self.assertEqual(resultado,10)

    def test_XI(self):
        resultado = roman_to_decimals('XI')
        self.assertEqual(resultado,11)


    def test_XV(self):
        resultado = roman_to_decimals('XV')
        self.assertEqual(resultado,15)

    def test_XX(self):
        resultado = roman_to_decimals('XX')
        self.assertEqual(resultado,20)


    def test_XXX(self):
        resultado = roman_to_decimals('XXX')
        self.assertEqual(resultado,30)


    def test_XL(self):
        resultado = roman_to_decimals('XL')
        self.assertEqual(resultado,40)


    def test_L(self):
        resultado = roman_to_decimals('L')
        self.assertEqual(resultado,50)


    def test_LX(self):
        resultado = roman_to_decimals('LX')
        self.assertEqual(resultado,60)


    def test_LXX(self):
        resultado = roman_to_decimals('LXX')
        self.assertEqual(resultado,70)



    def test_LXXX(self):
        resultado = roman_to_decimals('LXXX')
        self.assertEqual(resultado,80)


    def test_XC(self):
        resultado = roman_to_decimals('XC')
        self.assertEqual(resultado,90)


    def test_C(self):
        resultado = roman_to_decimals('C')
        self.assertEqual(resultado,100)

if __name__ == "__main__":
    unittest.main()
