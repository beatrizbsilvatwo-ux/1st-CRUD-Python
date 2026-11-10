# CREATE - INSERT
# READ - SELECT
# UPDATE - UPDATE
# DELETE - DELETE

import mysql.connector

class Conexao:

    def __init__(self):

        self.host = 'localhost'
        self.database = 'db_escola'
        self.user = 'admin_python'
        self.password = 'Senha123!'

        self.conexao  = None
    
    def conectar(self):

        try:

            self.conexao = mysql.connector.connect(
                host = self.host,
                database = self.database,
                user=self.user,
                password = self.password

            )

            print('Conexão realizada com sucesso!')

            return self.conexao
        
        except mysql.connector.Error as erro:
            print(f'Erro ao conectar com o banco: {erro}')
            return None
    def desconectar(self):
        if self.conexao is not None and self.conexao.is_connected():

            self.conexao.close()
            print('Conexao encerrada.')