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
        self.assertEqual(i[1][0],20)
        
   def  test_vender_ingresso(self):
        sessao.criar_sessao(20,20,20,20,20)
        ingresso.adicionar_ingresso(20,20)
        ingresso.vender_ingresso(20,2)
        i = ingresso.obter_ingresso(20)
        self.assertEqual(i[2],18)
     
    def test_verificar_ingresso(self):
        sessao.criar_sessao(20,20,20,20,20)
        ingresso.adicionar_ingresso(20,20)
        i = ingresso.verificar_ingresso(20)
        self.assertEqual(i[1],20)
     
if __name__ == '__main__':
    unittest.main(exit=False)
