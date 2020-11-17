import mysql.connector
#Função que ira connectar com o  Mysql de acordo com as informaçoes abaico
mydb = mysql.connector.connect(
    host="localhost",#Nome do host
    user="root",# Nome de usuario do Banco
    password="12345", #Senha do banco de daods
    database="teste"  # colocar o nome do banco de dados que deseja acessar.
)


myquerys = mydb.cursor()  #myquerys é a variavel que é usada quando quer ser declarado um comando em SQL sendo o comando myquerys.execute("Querys")

class ConectionFactory:
    #Mostra todos os dados do banco (teste) da tabela (tab) colocar os arquivos em uma lista e retornar um print da lista
    def showdata(self):
        myquerys.execute("SELECT * FROM users")
        record = myquerys.fetchall()
        return record