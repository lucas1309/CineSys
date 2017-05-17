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
