import sqlite3
# 1- Conectando no BD
conexao = sqlite3.connect('tabela.db')
cursor = conexao.cursor()

# 2 - Atualização do Banco de dados
id = 1
cursor.execute(

    """
    UPDATE cadastro set nome = ?
    WHERE id = ?
    """,
    ('Oliveira', id)
)
conexao.commit()