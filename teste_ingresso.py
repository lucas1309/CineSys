import unittest
 
import ingresso
import sessao
class TestIngresso(unittest.TestCase):
  def setUp(self):
        ingresso.excluir_todos_ingressos()
    
  def test_sem_ingressos(self):
        ingressos = ingresso.listar_ingressos()
        self.assertEqual(0, len(ingressos))
     
if __name__ == '__main__':
    unittest.main(exit=False)
