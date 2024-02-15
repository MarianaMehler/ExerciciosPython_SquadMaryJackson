# RESOLUÇÃO DESAFIO POO-DB: GERENCIAMENTO DE BIBLIOTECA

from abc import abstractmethod #import para tornar a classe abstrata 

import sqlite3 # import para usar o dbeaver
conexao = sqlite3.connect('banco-poo-db')  # nome do arquivo criado no Dbeaver
cursor = conexao.cursor()

class Livro:
    lista_genero = [] #lista global para armazenar os generos
    livros_disponiveis = [] # lista global para armazenar os livros disponiveis

    def __init__(self, autor, titulo, editora, genero, emprestado):
        self.autor = autor 
        self.titulo = titulo
        self.editora = editora
        self.genero = genero
        self.emprestado = emprestado
        self.livro() # chama o método livro para imprimir as informações
    
    def livro(self):
        print(f'Livro: {self.titulo}, autor: {self.autor}, editora: {self.editora}, gênero: {self.genero}, emprestado: {self.emprestado}')
        
        Livro.lista_genero.append(self.genero) # adiciona o gênero à lista 'lista_genero'
        
        if self.emprestado == 0 :  # se emprestado == false (significa que o livro está disponivel)
            Livro.livros_disponiveis.append(self)  # armazena na lista 'livros_disponiveis'
        
    @staticmethod  # método estático, para listar os generos
    def generos():
        print('Gêneros cadastrados: ')
        for item in Livro.lista_genero:   # laço de repetição para listar o vetor
            print(f' - {item}')
    
    @staticmethod  # método estático, para listar os livros disponiveis
    def disponiveis():
        print('Livros disponíveis: ') 
        for livro in Livro.livros_disponiveis: # laço de repetição para listar o vetor
            print(f' - Título: {livro.titulo}, autor: {livro.autor}')  # listando os atributos desejáveis do livro
        
    @abstractmethod  #método abstrato dentro de classe abstrata
    def emprestar(self):
        emprestado = emprestado #deve ser instaciado na classe filha 

class Usuario:
    def __init__(self, nome, telefone, nacionalidade):
        self.nome = nome
        self.telefone = telefone
        self.nacionalidade = nacionalidade

class Emprestar(Livro): # herança da classe Livro
    def __init__(self, autor, titulo, editora, genero, emprestado):
        super().__init__(autor, titulo, editora, genero, emprestado)  #método super() para chamar a herança

        self.emprestado(True) # instancia o atributo emprestado como true
        print(f'Livro "{self.titulo}" emprestado.')

'''
############## COMANDOS POO ##############
# Instanciando e listando livros:
print('Livros cadastrados:')
dado = Livro("Itamar Vieira Junior","Torto arado","Arqueiro","Realismo Mágico",False)
dado = Livro("Ana Paula Maia","Enterre seus mortos","Saraiva","Drama",True)
dado = Livro("Margaret Atwood","O conto da aia","Rocco","Distopia",True)
dado = Livro("Stephen King", "It", "Viking Press", "Terror", False)
dado = Livro("George Orwell", "1984", "Penguin Books", "Ficção Científica", False)
dado = Livro("Agatha Christie", "O Assassinato no Expresso Oriente", "Globo Livros", "Mistério", True)
dado = Livro("J.R.R. Tolkien", "O Senhor dos Anéis: A Sociedade do Anel", "Martins Fontes", "Fantasia", False)
dado = Livro("Clarice Lispector", "A Hora da Estrela", "Rocco", "Literatura Brasileira", True)
print('')

# Listando os generos:
dado.generos()
print('')

#listando os livros disponiveis
dado.disponiveis()
'''

############## COMANDOS SQL ##############
## Criando tabelas:
'''
cursor.execute('CREATE TABLE Livros(id_livro INT PRIMARY KEY, titulo VARCHAR(50), autor VARCHAR(50), editora VARCHAR(50), genero VARCHAR(50), emprestado BOOLEAN);') 
cursor.execute('CREATE TABLE Usuarios(id_user INT PRIMARY KEY, nome VARCHAR(50), telefone VARCHAR(50), nacionalidade VARCHAR(50));')
cursor.execute('CREATE TABLE Emprestimos(id_emp INT PRIMARY KEY, data_emprestimo DATE, data_devolucao DATE, usuario VARCHAR(50), titulo VARCHAR(50));')
'''
## Inserindo dados nas tabelas:
'''
# Inserindo dados na tabela Livros:
livros_values = [
    ('1','O conto da aia', 'Margaret Atwood', 'Rocco', 'Distopia', 0),
    ('2','Torto arado', 'Itamar Vieira Junior', 'Arqueiro', 'Realismo Mágico', 1),
    ('3','Enterre seus mortos', 'Ana Paula Maia', 'Saraiva', 'Mistério', 1),
    ('4','O caçador de pipas', 'Kalhed Hoseini', 'Arqueiro', 'Drama', 1),
    ('5','Vermelho, branco e sangue azul', 'Casey McQuiston', 'Rocco', 'Romance', 0)
]
for livro in livros_values:
    cursor.execute('INSERT INTO Livros (id_livro, titulo, autor, editora, genero, emprestado) VALUES (?, ?, ?, ?, ?, ?)', livro)

# Inserindo dados na tabela Usuarios:
user_values = [
    ('1','Maria','499991360963','Brasileira'),
    ('2','Joana','49998762342','Chilena'),
    ('3','Pedro','49999875225','Venezuelana'),
    ('4','Daiane','49991329910', 'Brasileira'),
    ('5','Marli','49998142520','Brasileira')
]
for user in user_values:
    cursor.execute('INSERT INTO Usuarios (id_user, nome, telefone, nacionalidade) VALUES (?, ?, ?, ?)', user)

# Inserindo dados na tabela Emprestimos:
empresta_values = [
    ('1','2024/02/04','26/02/2024','Marli','O conto da aia'),
    ('2','2024/01/15','01/02/2024','Pedro','Torto arado'),
    ('3','2024/02/06','28/02/2024','Joana','Enterre seus mortos')
]
for empresta in empresta_values:
    cursor.execute('INSERT INTO Emprestimos (id_emp, data_emprestimo, data_devolucao, usuario, titulo) VALUES (?, ?, ?, ?, ?)', empresta)
'''

### Consultas SQL:

##listar todos os livros disponíveis
#dados = cursor.execute('SELECT titulo FROM Livros')
#for item in dados:
#    print(item)

##todos os livros emprestados no momento
#dados = cursor.execute('SELECT titulo FROM Livros WHERE emprestado=True')
#for item in dados:
 #   print(item)

##localizar os livros escritos por um autor específico
#dados = cursor.execute('SELECT titulo FROM Livros WHERE autor="Itamar Vieira Junior"')
#for item in dados:
#    print(item)

##verificar o número de cópias disponíveis de um determinado livro
#dados = cursor.execute('SELECT COUNT(*) FROM Livros WHERE titulo="O conto da aia"')
#for item in dados:
#   print(item)

##mostrar os empréstimos em atraso
#dados = cursor.execute('SELECT titulo FROM Emprestimos WHERE data_devolucao<"2024/02/07"')
#for item in dados:
#    print(item)

### Atualizações e exclusões:
## Escreva consultas SQL para atualizar e excluir registros do BD (ex: marcar um livro como devolvido ou remover um autor)
#cursor.execute('DELETE FROM Usuarios where id_user=5')
#cursor.execute('UPDATE Usuarios SET nome="Marli" WHERE nome="Daiane"')
#cursor.execute('UPDATE Livros SET emprestado="0" WHERE id_livro="3"')
#cursor.execute('DELETE FROM Emprestimos WHERE id_emp="3"')

conexao.commit() 
conexao.close()
