import unittest
 
import ingresso
import sessao
class TestIngresso(unittest.TestCase):
  def setUp(self):
        ingresso.excluir_todos_ingressos()

if __name__ == '__main__':
    unittest.main(exit=False)
