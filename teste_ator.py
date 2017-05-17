import unittest

import ator

class TestAtor(unittest.TestCase):
  def setUp(self):
        ator.remover_todos_atores()
  def test_sem_ators(self):
        atores = ator.listar_atores()
        self.assertEqual(0, len(atores))
