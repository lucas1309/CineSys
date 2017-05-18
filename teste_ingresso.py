import unittest
 
import ingresso
import sessao
class TestIngresso(unittest.TestCase):
  def setUp(self):
        ingresso.excluir_todos_ingressos()
    
  def test_sem_ingressos(self):
        ingressos = ingresso.listar_ingressos()
        self.assertEqual(0, len(ingressos))
     
  def test_adicionar_um_ingresso(self):
        sessao.criar_sessao(20,20,20,20,20)
        ingresso.adicionar_ingresso(20,20)
         
        ingressos = ingresso.listar_ingressos()
        self.assertEqual(1, len(ingressos))
        sessoes = sessao.listar_sessao()
        self.assertEqual(1, len(sessoes))
        
   def test_obter_ingresso(self):
        sessao.criar_sessao(20,20,20,20,20)
        ingresso.adicionar_ingresso(20,20)
        i = ingresso.obter_ingresso(20)
        self.assertEqual(i[0],20)
        self.assertEqual(i[1],20)
     
if __name__ == '__main__':
    unittest.main(exit=False)
