import sqlite3
# 1-Criando banco de dados
conexao=sqlite3.connect('tabela.db')

# 2-Criando tabela
cursor=conexao.cursor()

cursor.execute(

    """
    INSERT INTO cadastro(nome, idade, cpf)
    VALUES ('Daniel', 19, 7632593223),
    ('Carvalho', 20, 9876542345);
    """
)
conexao.commit()
conexao.close()