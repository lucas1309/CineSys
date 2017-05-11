import unittest
import sala


class TestSala(unittest.TestCase):

    def setUp(self):
        sala.remover_todas_as_salas()
    
    def test_criar_sala(self):
        sala.criar_sala(11,30)
        salas = sala.listar_salas()
        self.assertEqual(1,len(salas))
        s=salas[0]
        self.assertEqual(11,s[0])
        self.assertEqual(30,s[1])

    def test_obter_sala(self):
        sala.criar_sala(11,30)
        sala.criar_sala(3,58)
        
        s =sala.obter_sala(11)
        
        self.assertEqual(11,s[0])
        
    def test_excluir_sala(self):
        sala.criar_sala(11,30)
        sala.criar_sala(3,58)
        sala.excluir_sala(3)
        s = sala.obter_sala(3)
        self.assertIsNone(s)
        
    def teste_alterar_sala(self):
        sala.criar_sala(11,30)
        sala.criar_sala(3,58)
        s = sala.obter_sala(11)
        salas = sala.listar_salas()
        s[1] = 60
        self.assertEqual(11,s[0])
        self.assertEqual(60,s[1])

if __name__ =='__main__':
    unittest.main(exit=False)
