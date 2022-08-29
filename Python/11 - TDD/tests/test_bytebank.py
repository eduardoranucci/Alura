from codigo.bytebank import Funcionario

class TestClass:
    
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        
        entrada = '13/03/2000' # Given - Contexto
        esperado = 22
        
        funcionario_teste = Funcionario('Func Teste', entrada, 1000)
        resultado = funcionario_teste.idade() # When - Ação
        
        assert resultado == esperado # Then - Desfecho
        
    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        
        entrada = '      Lucas Carvalho      '
        esperado = 'Carvalho'
        
        lucas = Funcionario(entrada, '02/02/2000', 1000)
        resultado = lucas.sobrenome()
        
        assert resultado == esperado