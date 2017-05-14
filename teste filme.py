import unittest
import filme

class TestFilme(unittest.TestCase):

    def setUp(self):
        filme.excluir_todos_filmes()

    def test_criar_filme(self):
        filme.criar_filme(1,"Filme","terror",{"Ator":"Beltrano","Diretor" : "Fulano"},120,"18 Anos","UCI")
        filmes = filme.listar_filmes()
        self.assertEqual(1,len(filmes))
        s = filmes[0]
        self.assertEqual(1,s.cod)
        self.assertEqual("Filme",s.nome)
        self.assertEqual("terror",s.genero)
        self.assertEqual({"Ator":"Beltrano","Diretor" : "Fulano"},s.elenco)
        self.assertEqual(120,s.duracao)
        self.assertEqual("18 Anos",s.classificacao)
        self.assertEqual("UCI",s.distribuidora)

    def test_obter_filme(self):
        filme.criar_filme(1,"Filme","terror",{"Ator":"Beltrano","Diretor" : "Fulano"},120,"18 Anos","UCI")
        filme.criar_filme(2,"Filme2","terror2",{"Ator":"Beltrano","Diretor" : "Fulano"},130,"16 Anos","UCA")
        filmeObtido = filme.obter_filme(1)
        self.assertEqual(1,filmeObtido.cod)
        
    def test_excluir_filme(self):
        filme.criar_filme(1,"Filme","terror",{"Ator":"Beltrano","Diretor" : "Fulano"},120,"18 Anos","UCI")
        filme.criar_filme(2,"Filme2","terror2",{"Ator":"Beltrano","Diretor" : "Fulano"},130,"16 Anos","UCA")
        filme.excluir_filme(2)
        f = filme.obter_filme(2)
        self.assertIsNone(f)

    def test_alterar_filme(self):
        elenco = {"Ator":"Beltrano","Diretor" : "Fulano"}
        filme.criar_filme(1,"Filme","terror",elenco,120,"18 Anos","UCI")
        filme.alterar_filme(1,"NovoFilme","aventura",{"Ator":"Ciclano","Diretor" : "Fulano"},100,"10 Anos","CineMark")
        f = filme.obter_filme(1)
        self.assertEqual("NovoFilme",f.nome)
        
if __name__ =='__main__':
    unittest.main(exit=False)
