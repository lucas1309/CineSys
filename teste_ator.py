import unittest

import ator

class TestAtor(unittest.TestCase):
  def setUp(self):
        ator.remover_todos_atores()
  def test_sem_ators(self):
        atores = ator.listar_atores()
        self.assertEqual(0, len(atores))
  def test_adicionar_um_ator(self):
        ator.adicionar_ator(1, "Chris Hemsworth", "Australiano", 33)

        atores = ator.listar_atores()
        self.assertEqual(1, len(atores))

        a = atores[0]

        self.assertEqual(1, a[0])
        self.assertEqual("Chris Hemsworth", a[1])
        self.assertEqual("Australiano", a[2])
        self.assertEqual(33, a[3])
  def test_adicionar_dois_atores(self):
        ator.adicionar_ator(2, "Jason Statham", "Ingles", 49)
        ator.adicionar_ator(1, "Chris Hemsworth", "Australiano", 33)

        atores = ator.listar_atores()
        self.assertEqual(2, len(atores))
  def test_buscar_atores(self):
        ator.adicionar_ator(2, "Jason Statham", "Ingles", 49)
        ator.adicionar_ator(1, "Chris Hemsworth", "Australiano", 33)

        a = ator.obter_ator(1)
        self.assertEqual(1, a[0])
        self.assertEqual("Chris Hemsworth", a[1])
        self.assertEqual("Australiano", a[2])
        self.assertEqual(33, a[3])
  def test_excluir_ator(self):
       ator.adicionar_ator(2, "Jason Statham", "Ingles", 49)
       ator.adicionar_ator(1, "Chris Hemsworth", "Australiano", 33)

       ator.excluir_ator(1)

       a = ator.obter_ator(1)
       self.assertIsNone(a)
      
  def test_remover_todos_atores(self):
        ator.adicionar_ator(2, "Jason Statham", "Ingles", 49)
        ator.adicionar_ator(1, "Chris Hemsworth", "Australiano", 33)

        ator.remover_todos_atores()

        a = ator.obter_ator(1)
        self.assertIsNone(a)
        
  def test_iniciar_atores(self):
        ator.iniciar_atores()
        atores = ator.listar_atores()
        self.assertEqual(3, len(atores))
        
        
            
if __name__ == '__main__':
    unittest.main(exit=False)
