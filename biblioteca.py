import sqlite3

# Função para conectar ao banco de dados
def connect():
    conn = sqlite3.connect('biblioteca.db')
    return conn

# Função para criar as tabelas necessárias no banco de dados
def create_tables():
    conn = connect()

    # Criar tabela de livros
    conn.execute('''CREATE TABLE IF NOT EXISTS livros (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT,
                    autor TEXT,
                    editora TEXT,
                    ano_publicacao INTEGER,
                    isbn TEXT)''')

    # Criar tabela de usuários
    conn.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    sobrenome TEXT,
                    endereco TEXT,
                    email TEXT,
                    telefone TEXT)''')

    # Criar tabela de empréstimos
    conn.execute('''CREATE TABLE IF NOT EXISTS emprestimos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_livro INTEGER,
                    id_usuario INTEGER,
                    data_emprestimo TEXT,
                    data_devolucao TEXT,
                    FOREIGN KEY(id_livro) REFERENCES livros(id),
                    FOREIGN KEY(id_usuario) REFERENCES usuarios(id))''')

    conn.commit()
    conn.close()

# Função para inserir um novo livro
def insert_book(titulo, autor, editora, ano_publicacao, isbn):
    conn = connect()
    conn.execute("INSERT INTO livros (titulo, autor, editora, ano_publicacao, isbn) VALUES (?, ?, ?, ?, ?)",
                 (titulo, autor, editora, ano_publicacao, isbn))
    conn.commit()
    conn.close()

# Função para inserir um novo usuário
def insert_user(nome, sobrenome, endereco, email, telefone):
    conn = connect()
    conn.execute("INSERT INTO usuarios (nome, sobrenome, endereco, email, telefone) VALUES (?, ?, ?, ?, ?)",
                 (nome, sobrenome, endereco, email, telefone))
    conn.commit()
    conn.close()

# Função para realizar um novo empréstimo
def insert_loan(id_livro, id_usuario, data_emprestimo, data_devolucao=None):
    conn = connect()
    conn.execute("INSERT INTO emprestimos (id_livro, id_usuario, data_emprestimo, data_devolucao) VALUES (?, ?, ?, ?)",
                 (id_livro, id_usuario, data_emprestimo, data_devolucao))
    conn.commit()
    conn.close()

# Função para recuperar todos os livros atualmente emprestados
def get_books_on_loan():
    conn = connect()
    result = conn.execute('''SELECT livros.titulo, usuarios.nome, usuarios.sobrenome, 
                             emprestimos.data_emprestimo, emprestimos.data_devolucao
                             FROM livros
                             INNER JOIN emprestimos ON livros.id = emprestimos.id_livro
                             INNER JOIN usuarios ON usuarios.id = emprestimos.id_usuario
                             WHERE emprestimos.data_devolucao IS NULL''').fetchall()
    conn.close()
    return result

# Função para atualizar a data de devolução de um empréstimo
def update_loan_return_date(id_emprestimo, data_devolucao):
    conn = connect()
    conn.execute("UPDATE emprestimos SET data_devolucao = ? WHERE id = ?", (data_devolucao, id_emprestimo))
    conn.commit()
    conn.close()

# Função para exibir o menu principal
def show_menu():
    print("\n--- Menu da Biblioteca ---")
    print("1. Inserir um novo livro")
    print("2. Inserir um novo usuário")
    print("3. Realizar um empréstimo")
    print("4. Atualizar a data de devolução de um empréstimo")
    print("5. Exibir todos os livros emprestados no momento")
    print("0. Sair")

    choice = input("Digite o número da opção desejada: ")
    return choice

# Função para verificar se o livro existe
def book_exists(book_id):
    conn = connect()
    result = conn.execute("SELECT id FROM livros WHERE id = ?", (book_id,)).fetchone()
    conn.close()
    return result is not None

# Função para verificar se o usuário existe
def user_exists(user_id):
    conn = connect()
    result = conn.execute("SELECT id FROM usuarios WHERE id = ?", (user_id,)).fetchone()
    conn.close()
    return result is not None

# Função principal do sistema
def main():
    # Cria as tabelas se elas ainda não existirem
    create_tables()

    # Loop principal do sistema
    while True:
        choice = show_menu()

        if choice == "1":
            title = input("Digite o título do livro: ")
            author = input("Digite o nome do autor: ")
            publisher = input("Digite o nome da editora: ")
            try:
                year = int(input("Digite o ano de publicação: "))
            except ValueError:
                print("Ano inválido! Digite um número inteiro.")
                continue
            isbn = input("Digite o ISBN do livro: ")
            insert_book(title, author, publisher, year, isbn)
            print("Livro inserido com sucesso!")

        elif choice == "2":
            first_name = input("Digite o primeiro nome do usuário: ")
            last_name = input("Digite o sobrenome do usuário: ")
            address = input("Digite o endereço: ")
            email = input("Digite o e-mail: ")
            phone = input("Digite o telefone: ")
            insert_user(first_name, last_name, address, email, phone)
            print("Usuário inserido com sucesso!")

        elif choice == "3":
            try:
                user_id = int(input("Digite o ID do usuário: "))
            except ValueError:
                print("ID de usuário inválido! Digite um número inteiro.")
                continue
            if not user_exists(user_id):
                print("Usuário não encontrado!")
                continue

            try:
                book_id = int(input("Digite o ID do livro: "))
            except ValueError:
                print("ID do livro inválido! Digite um número inteiro.")
                continue
            if not book_exists(book_id):
                print("Livro não encontrado!")
                continue

            loan_date = input("Digite a data do empréstimo (AAAA-MM-DD): ")
            insert_loan(book_id, user_id, loan_date)
            print("Empréstimo realizado com sucesso!")

        elif choice == "4":
            try:
                loan_id = int(input("Digite o ID do empréstimo: "))
            except ValueError:
                print("ID do empréstimo inválido! Digite um número inteiro.")
                continue

            return_date = input("Digite a data de devolução (AAAA-MM-DD): ")
            update_loan_return_date(loan_id, return_date)
            print("Data de devolução atualizada com sucesso!")

        elif choice == "5":
            books_on_loan = get_books_on_loan()
            if books_on_loan:
                print("Livros atualmente emprestados:")
                for book in books_on_loan:
                    print(f"Título: {book[0]}, Usuário: {book[1]} {book[2]}, Empréstimo: {book[3]}")
            else:
                print("Não há livros emprestados no momento.")

        elif choice == "0":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa principal
if __name__ == "__main__":
    main()
