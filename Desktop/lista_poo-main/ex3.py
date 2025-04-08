import datetime

class Funcionario:
    def __init__(self, id_num, nome, sobrenome, data_nascimento, data_admissao, salario):
        self.id_num = id_num
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento
        self.data_admissao = data_admissao  
        self.salario = salario
    
    def idade(self):
        ano_atual = datetime.datetime.now().year
        return ano_atual - self.data_nascimento[2]
    
    def tempo_de_casa(self):
        ano_atual = datetime.datetime.now().year
        return ano_atual - self.data_admissao[2]
    
    def aumento_de_salario(self):
        anos = self.tempo_de_casa()
        if anos < 5:
            self.salario *= 1.02  
        elif anos < 10:
            self.salario *= 1.05  
        else:
            self.salario *= 1.10  
    
    def mostrar_funcionario(self):
        
        print(f"Número pessoal: {self.id_num}")
        print(f"Nome: {self.nome}")
        print(f"Sobrenome: {self.sobrenome}")
        print(f"Idade: {self.idade()}")
        print(f"Tempo de casa: {self.tempo_de_casa()} anos")
        print(f"Salário em €: {self.salario:.2f}")


agente = Funcionario('4', 'Julia', 'Scandoleiro', (4, 4, 2007), (7, 7, 2014), 10000)
agente.aumento_de_salario()
agente.mostrar_funcionario()
