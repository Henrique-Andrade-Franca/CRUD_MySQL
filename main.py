'''
Author: Henrique Andrade
Date: 2023/09/25
'''

import mysql.connector

conexao = mysql.connector.connect(
  host = 'localhost',
  user = 'root',
  password = 'senha_do_usuario_MySQL',
  database = 'nome_do_banco_de_dados',
)

cursor = conexao.cursor()

'''
MODELO BÁSICO PARA CRIAÇÃO DO CRUD

comando = ''                    #comando em SQL
cursor.execute(comando)
conexao.commit()                #edita o banco de dados (create, update, delete)
resultado = cursor.fetchall()   #ler o banco de dados (read)
'''

#PARA A EXECUÇÃO DE UM, COMENTAR OS OUTROS - EVITAR CONFLITO

#CREATE

nome_produto = "anabolizantes"
valor = 15
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'                   
cursor.execute(comando)
conexao.commit()               
resultado = cursor.fetchall()


#READ
'''
comando = f'SELECT * FROM vendas'             
cursor.execute(comando)             
resultado = cursor.fetchall()
print(resultado)
'''

#UPDATE
'''
nome_produto = "bomba"
valor = 50
comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'                   
cursor.execute(comando)
conexao.commit()
'''

#DELETE
'''
nome_produto = "anabolizantes"
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'                   
cursor.execute(comando)
conexao.commit()
'''

cursor.close()
conexao.close()