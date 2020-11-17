import PySimpleGUI as sg
from LeituraDeRosto import VerificarRosto
from Conexao import ConectionFactory


class TelaPython:

    #Tela inicial de Login
    def janelaLogin(self):
        sg.theme('Green') #Cor da tela
        layout = [
            [sg.Text('O Nome de Usuario ira ser o Nome da Imagem e a Senha sera o Rosto ')],
            [sg.Text('Aperte em Reconher para Entrar ou Cancelar para sair do Programa')], #Texto
            [sg.Button("Reconhecer"),sg.Button('Cancelar')], #Botões

                ]
        return sg.Window("Tela Login", layout=layout,finalize=True)

    # Tela que sera acessada para pegar informaçoes do banco
    def infoDoBanco(self):
        sg.theme('Green')
        layout = [[sg.Text('Informações do Banco')],
                  [sg.Output(size=(80, 10))], # Uma mine tela de terminal que ira mostrar as informaçoes do banco.
                  [sg.Button('Pegar info'),sg.Button('Fechar'),sg.Button('Voltar')]
                  ]
        return sg.Window("Tela de Info", layout=layout,finalize=True)
    #Função que ira rodar as telas, oque cada botão faz e suas funções
    def comecar(self):
        janela_login, janela_infoBanco = self.janelaLogin(), self.infoDoBanco() #Ira mostrar as telas inicialmente
        janela_infoBanco.hide() # esconde a janela infoDoBanco
        while True:
            window,evento,values = sg.read_all_windows() #ira guardar todos os aquivos passando pela janela como evento
            if evento == janela_login and evento == sg.WIN_CLOSED:
                break
            if evento == janela_infoBanco and evento == sg.WIN_CLOSED:
                break
            if window == janela_login and evento == 'Cancelar':
                break
            if window == janela_infoBanco and evento == 'Fechar':
                break
            if window == janela_login and evento == "Reconhecer":
                rosto = self.lerRosto() #Acessa uma função na classe ler rosto que fara o reconhecimento facial / porem inicialmente não retorna nada
                nomes_users = self.verifyNames()
                if rosto in nomes_users: #Verifica se o nome que ira vir em retorno da funçao é compativel com os nomes de imagem que irão servir como Nome dos usuario/ Nomes do Usuario = nome da foto/ Senha = Rosto.
                    janela_infoBanco.un_hide()  #comando que ira fazera janela de login se aparecer
                    janela_login.hide()#comando que ira fazera janela de login se esconder
                else:
                    janela_login.hide()
                    sg.popup('Seu Rosto Não Foi Reconhecido')# popup que ira aparecer quando um rosto não for reconhecido
                    break
            if window == janela_infoBanco and evento == 'Voltar':
                janela_infoBanco.hide()
                janela_login.un_hide()
            if window == janela_infoBanco and evento == 'Pegar info':
                banco = ConectionFactory()
                informacoes = banco.showdata() #Comomando que ira mostrar as iformaçoes na banco declarado na classe Conexao
                print(*informacoes, sep= '\n') # ira printar toda a lista e ira pular uma linha para cada item da lista


    #Função que ler o Rosto
    def lerRosto(self):
        reconRosto = VerificarRosto
        return reconRosto.leituraDORosto(reconRosto)
    #Fução que ira olhar na pasta imagem e ira pegar todos os nomes de arquivos dentro da pasta e retornar uma lista com os nomes
    def verifyNames(self):
        f1 = VerificarRosto
        return f1.VerifyNameUsers(f1)




tela = TelaPython()
tela.comecar()
