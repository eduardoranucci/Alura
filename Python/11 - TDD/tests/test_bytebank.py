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
        
    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        
        entrada_salario = 100000
        entrada_nome = 'Paulo Bragança'
        esperado = 90000
        
        diretor = Funcionario(entrada_nome, '02/02/2000', entrada_salario)
        diretor.decrescimo_salario()
        resultado = diretor.salario
        
        assert resultado == esperado