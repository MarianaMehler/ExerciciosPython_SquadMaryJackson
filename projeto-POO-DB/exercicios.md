#### POO:

1. **OPÇÃO 1: Gerenciamento de Biblioteca**
    Vamos criar um sistema orientado a objetos para representar um sistema de biblioteca seguindo os requisitos abaixo
    - Cada livro pode ter um ou mais autores;
    - A biblioteca controla apenas o nome, o telefone e a nacionalidade de cada usuário;
    - Cada livro tem um título, editora, uma lista de gêneros aos quais pertence e uma lista de exemplares disponíveis;
    - Quando um exemplar é emprestado, ele é removido da lista de exemplares disponíveis;
    - Alguns livros podem ter um número máximo de renovações permitidas; 
    - A biblioteca mantém um registro de todos os empréstimos realizados, incluindo detalhes como data de empréstimo, data de devolução e estado do exemplar (por exemplo, emprestado ou devolvido);
    Para modelar o sistema, utilize obrigatoriamente os conceitos de classe, herança, propriedade, encapsulamento e classe abstrata.

2. **OPÇÃO 2: Gerenciamento de Mercado**
    Vamos criar um sistema orientado a objetos para representar um sistema de mercado seguindo os requisitos fornecidos
    - Cada livro pode ter um ou mais autores;
    - O mercado controla apenas o nome, o telefone e o endereço de cada cliente;
    - Cada produto tem um nome, uma lista de categorias às quais pertence e uma quantidade disponível em estoque;
    - Quando um produto é comprado, sua quantidade disponível em estoque é reduzida;
    - O mercado mantém um registro de todas as transações realizadas, incluindo detalhes como data da compra, cliente envolvido e quantidade de produtos comprados;


#### BD:

1. **OPÇÃO 1: Exercício Gerenciamento Biblioteca**

    Criação das Tabelas:
    - Utilizando SQL, crie as tabelas necessárias para armazenar as informações do sistema. Certifique-se de definir as chaves primárias e estrangeiras conforme apropriado.

    Inserção de Dados:
    - Insira dados de exemplo nas tabelas para simular um ambiente de biblioteca. Certifique-se de incluir uma variedade de livros, autores e editoras.

    Consultas SQL:
    - Escreva consultas SQL para realizar as seguintes operações:
    - Listar todos os livros disponíveis
    - Encontrar todos os livros emprestados no momento
    - Localizar os livros escritos por um autor específico
    - Verificar o número de cópias disponíveis de um determinado livro.
    - Mostrar os empréstimos em atraso.

    Atualizações e Exclusões:
    - Escreva consultas SQL para atualizar e excluir registros do banco de dados, por exemplo, para marcar um livro como devolvido ou remover um autor.

2. **OPÇÃO 2: Exercício Gerenciamento Mercado**

    Criação das Tabelas:
    - Utilizando SQL, crie as tabelas necessárias para armazenar as informações do sistema. Defina as chaves primárias e estrangeiras conforme apropriado.

    Inserção de Dados:
    - Insira dados de exemplo nas tabelas para simular um ambiente de venda de eletrônicos. Certifique-se de incluir uma variedade de produtos e clientes.

    Consultas SQL:
    - Escreva consultas SQL para realizar as seguintes operações:
    - Listar todos os produtos em estoque
    - Encontrar as vendas realizadas por um cliente específico.
    - Calcular o total de vendas por categoria de produto
    - Identificar os produtos mais vendidos

    Atualizações e Exclusões:
    - Escreva consultas SQL para atualizar e excluir registros do banco de dados, por exemplo, para atualizar a quantidade em estoque após uma venda ou remover um cliente.

