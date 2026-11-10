from conexao import Conexao

class Usuario:
    def __init__(self, nome, email, idade):
        self.nome = nome
        self.email = email
        self.idade = idade

    # Metodo que salva um usuário no banco de dados
    def salvar(self):
        banco =  Conexao()

        #variavel que guarda o metodo conectar da classe Conexao
        conexao = banco.conectar()

        #Se a conexao for diferente de none entao executa o bloco
        if conexao:

            #Metodo do conector que permite inseirir sintaxes SQL via python
            cursor = conexao.cursor()
            #Sintaxe SQL para inserir registros em uma tabela
            sql = """
                INSERT INTO usuarios (nome, email, idade)
                VALUES (%s, %s, %s)

            """
            
            #Atributos do objeto usuario que serao registrados na tabela 
            valores = (
                self.nome,
                self.email,
                self.idade
            )

            #
            try: 

                ##Faz com que o método cursor do conector execute a junção entre a sintaxe SQL e os atributos do objeto
                cursor.execute(sql, valores)

                #Submete a Query SQL para o banco
                conexao.commit()

                print('Usuario cadastrado com sucesso!')

            #trata i erri e retorna uma mensagem do banco de dados
            except Exception as erro:
                print(f'Erro ao cadastrar usuário: {erro}')

            #encerra o cursor e encerra a conexao com o banco
            finally:
                cursor.close()
                banco.desconectar()

    #Metodo responsavel por consultar todos os usuarios cadastrados
    #Um metodo estatico nao precisa de um objeto para realziar sua ação.
    @staticmethod
    def listar():

        banco = Conexao()
        conexao = banco.conectar()

        if conexao:
            cursor = conexao.cursor()

            sql = """
                SELECT id, nome, email, idade
                FROM usuarios
                ORDER BY nome
                """

            try:
                cursor.execute(sql)
                usuarios = cursor.fetchall()

                for u in usuarios:
                    print(f'ID: {u[0]} | Nome: {u[1]} | Email: {u[2]} | Idade: {u[3]}\n')

            except Exception as erro:
                print(f'Erro: {erro}')

            finally:
                cursor.close()
                banco.desconectar()
    def atualizar(self, id):
        banco = Conexao()
        conexao = banco.conectar()

        if conexao:

            cursor = conexao.cursor()

            sql = """
                UPDATE usuarios
                SET nome = %s,
                    email = %s,
                    idade = %s
                WHERE id = %s
"""

            valores = (
                self.nome,
                self.email,
                self.idade,
                id
            )

            try:
                cursor.execute(sql, valores) # faz a juncao da sintaxe sqç com os valores
                conexao.commit()

                print('Usuáio atualizado!')
            except Exception as erro:
                print(f'Erro: {erro}')

            finally: 
                cursor.close()
                banco.desconectar()
    @staticmethod
    def excluir(id):
        banco = Conexao()
        conexao = banco.conectar()

        if conexao:
            cursor = conexao.cursor()

            sql = """
                DELETE FROM usuarios
                WHERE id= %s
            """

            valor = (id,)

            try:
                cursor.execute(sql, valor)
                conexao.commit()

            except Exception as erro:
                print(f'Erro: {erro}')

            finally:
                cursor.close()
                banco.desconectar()