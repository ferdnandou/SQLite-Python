# Sistema de Biblioteca

Este é um sistema simples de gerenciamento de biblioteca, desenvolvido em Python utilizando SQLite como banco de dados. O sistema permite cadastrar livros e usuários, realizar empréstimos, atualizar devoluções e listar livros emprestados.

## Funcionalidades

- **Cadastro de Livros**: Insira novos livros com título, autor, editora, ano de publicação e ISBN.
- **Cadastro de Usuários**: Cadastre novos usuários com nome, sobrenome, endereço, e-mail e telefone.
- **Empréstimos de Livros**: Registre empréstimos de livros para usuários cadastrados.
- **Atualização de Devoluções**: Atualize a data de devolução de um livro emprestado.
- **Listagem de Livros Emprestados**: Visualize todos os livros que estão atualmente emprestados.

## Estrutura do Banco de Dados

O banco de dados contém três tabelas principais:

1. **livros**:
   - `id`: Identificador único do livro (chave primária).
   - `titulo`: Título do livro.
   - `autor`: Nome do autor.
   - `editora`: Nome da editora.
   - `ano_publicacao`: Ano de publicação do livro.
   - `isbn`: Código ISBN do livro.

2. **usuarios**:
   - `id`: Identificador único do usuário (chave primária).
   - `nome`: Nome do usuário.
   - `sobrenome`: Sobrenome do usuário.
   - `endereco`: Endereço do usuário.
   - `email`: E-mail do usuário.
   - `telefone`: Telefone do usuário.

3. **emprestimos**:
   - `id`: Identificador único do empréstimo (chave primária).
   - `id_livro`: Identificador do livro emprestado (chave estrangeira).
   - `id_usuario`: Identificador do usuário que fez o empréstimo (chave estrangeira).
   - `data_emprestimo`: Data em que o empréstimo foi realizado.
   - `data_devolucao`: Data de devolução do livro (pode ser nula).

## Requisitos

- Python 3.x
- Biblioteca `sqlite3` (já inclusa na instalação padrão do Python)

## Como Executar

1. **Clone o repositório**:
    ```bash
    git clone https://github.com/ferdnandou/SQLite-Python.git
    ```
2. **Navegue até o diretório do projeto**:
    ```bash
    cd SQLite-Python
    ```
3. **Execute o programa**:
    ```bash
    python biblioteca.py
    ```
4. **Utilize o menu** para acessar as funcionalidades:
    - Opção 1: Inserir um novo livro.
    - Opção 2: Inserir um novo usuário.
    - Opção 3: Realizar um empréstimo.
    - Opção 4: Atualizar a data de devolução de um empréstimo.
    - Opção 5: Exibir todos os livros emprestados no momento.
    - Opção 0: Sair do sistema.

## Notas Importantes

- Certifique-se de que os IDs de livros e usuários existem antes de tentar realizar um empréstimo.
- A data deve ser inserida no formato `AAAA-MM-DD`.
- As funcionalidades de atualização de devolução e listagem de livros emprestados estão disponíveis apenas para empréstimos sem data de devolução registrada.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um `pull request` ou relatar problemas na aba de `issues`.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
