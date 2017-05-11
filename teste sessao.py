import unittest
import sessao

class TestSala(unittest.TestCase):

    def setUp(self):
        sessao.remover_todas_as_sessoes()

    def test_criar_sessao(self):
        sessao.criar_sessao(36,65,11,9,23)
        sessoes = sessao.listar_sessao()
        self.assertEqual(1,len(sessoes))
        s=sessoes[0]
        self.assertEqual(36,s[0])
        self.assertEqual(65,s[1])
        self.assertEqual(11,s[2])
        self.assertEqual(9,s[3])
        self.assertEqual(23,s[4])
        
    def test_buscar_sessao(self):
        sessao.criar_sessao(36,65,11,9,23)
        sessao.criar_sessao(3,5,1,2,65)

        s=sessao.buscar_sessao(3)

        self.assertEqual(3,s[0])
        self.assertEqual(5,s[1])
        self.assertEqual(1,s[2])
        self.assertEqual(2,s[3])
        self.assertEqual(65,s[4])
       
    def test_excluir_sessao(self):
        sessao.criar_sessao(36,65,11,9,23)
        sessao.criar_sessao(3,5,1,2,65)
        sessao.excluir_sessao(36)
        s = sessao.buscar_sessao(36)
        self.assertIsNone(s)

    def test_alterar_sessao(self):
        sessao.criar_sessao(36,65,11,9,23)
        sessao.criar_sessao(3,69,11,12,65)

        s=sessao.buscar_sessao(3)
        s[1] = 69
        s[2] = 11
        s[3] = 12
        s[4] = 65
        self.assertEqual(3,s[0])
        self.assertEqual(69,s[1])
        self.assertEqual(11,s[2])
        self.assertEqual(12,s[3])
        self.assertEqual(65,s[4])

    def test_verificar_disponibilidade(self):
        sessao.criar_sessao(36,65,11,9,23)
        sessao.criar_sessao(3,5,1,2,65)
        s = sessao.verificar_disponibilidade(36)
        self.assertEqual(23,s[4])

if __name__ =='__main__':
    unittest.main(exit=False)
