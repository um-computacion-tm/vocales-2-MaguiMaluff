import unittest
from vocales import contador_vocales

class TestContarVocales(unittest.TestCase):
    def test_sin(self):
        palabra = "try"
        resultado = contador_vocales(palabra)
        self.assertEqual(resultado, {})

    def test_sin_vocales(self):
        palabra = "tryhgf"
        resultado = contador_vocales(palabra)
        self.assertEqual(resultado, {})

    def test_con_vocal_o(self):
        palabra = "sOl"
        resultado = contador_vocales(palabra)
        self.assertEqual(resultado, {"o": 1})

    def test_con_vocal_doble_o(self):
        palabra = "solo"
        resultado = contador_vocales(palabra)
        self.assertEqual(resultado, {"o": 2})

    def test_con_dos_vocales(self):
        palabra = "solA"
        resultado = contador_vocales(palabra)
        self.assertEqual(resultado, {"o": 1,
                                     "a": 1})

    def test_con_todas_las_vocales(self):
        palabra = "solamente quiero que gane Boca"
        resultado = contador_vocales(palabra)
        self.assertEqual(
            resultado,
            {"a": 3,
             "e": 5,
             "i": 1,
             "o": 3,
             "u": 2},
        )

    def test_con_vocales_en_mayuscula(self):
        palabra = "SOlAmente quIerO"
        resultado = contador_vocales(palabra)
        self.assertEqual(resultado, {"a": 1,
                                     "e": 3,
                                     "i": 1,
                                     "o": 2,
                                     "u": 1},)   
    
    def test_con_2_o(self):
        palabra = "solo"
        resultado = contador_vocales(palabra)
        self.assertEqual(resultado, {"o": 2})

    def test_con_a_o(self):
        palabra = "ArrOz"
        resultado = contador_vocales(palabra)
        self.assertEqual(resultado, {"a": 1,
                                     "o": 1})
    
    def test_con_mayonesa(self):
        palabra = "mayOneSa"
        resultado = contador_vocales(palabra)
        self.assertEqual(resultado, {"a": 2,
                                     "o": 1,
                                     "e": 1})
    def test_murcielago(self):
        palabra = "murcielago"
        resultado = contador_vocales(palabra)
        self.assertEqual(resultado, {"a": 1,
                                     "e": 1,
                                     "i": 1,
                                     "o": 1,
                                     "u": 1})
    def test_con_vocal_a(self):
        palabra = "sal"
        resultado = contador_vocales(palabra)
        self.assertEqual(resultado, {"a": 1})
    
    def test_con_vocal_e(self):
        palabra = "les"
        resultado = contador_vocales(palabra)
        self.assertEqual(resultado, {"e": 1})

    def test_con_vocal_i(self):
        palabra = "si"
        resultado = contador_vocales(palabra)
        self.assertEqual(resultado, {"i": 1})

    def test_con_vocal_u(self):
        palabra = "su"
        resultado = contador_vocales(palabra)
        self.assertEqual(resultado, {"u": 1})

unittest.main()