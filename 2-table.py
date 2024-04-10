import sqlite3
# 1-Criando banco de dados
conexao=sqlite3.connect('tabela.db')

# 2-Criando tabela
cursor=conexao.cursor()

cursor.execute(

    """
    CREATE TABLE cadastro(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,    
        cpf INTEGER NOT NULL
    );
    """
)

conexao.close()
print("Tabela criada.")