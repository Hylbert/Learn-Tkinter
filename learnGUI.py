'''
Fonte: https://www.devmedia.com.br/tkinter-interfaces-graficas-em-python/33956

'''
from operator import le
from tkinter import*
from tkinter import font
from turtle import left

class Application:
    def __init__(self, master = None):
        self.fontePadrao = ('Arial', '10')
        self.primeiroContainer = Frame(master)
        self.primeiroContainer['pady'] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer['padx'] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer['padx'] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer['pady'] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text='Dados do usuário')
        self.titulo['font'] = ('Arial', '10', 'bold')
        self.titulo.pack()

        self.nomeLabel = Label(self.segundoContainer, text='Nome', font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.segundoContainer)
        self.nome['width'] = 30
        self.nome['font'] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.senhaLabel = Label(self.terceiroContainer, text='Senha', font = self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)

        self.senha = Entry(self.terceiroContainer)
        self.senha['width'] = 30
        self.senha['font'] = self.fontePadrao
        self.senha['show'] = '*'
        self.senha.pack(side=LEFT)

        self.autenticar = Button(self.quartoContainer)
        self.autenticar['text'] = 'Autenticar'
        self.autenticar['font'] = ('Calibri', '8')
        self.autenticar['width'] = 12
        self.autenticar['command'] = self.verificaSenha
        self.autenticar.pack()

        self.mensagem = Label(self.quartoContainer, text='', font=self.fontePadrao)
        self.mensagem.pack()

    #Método verifica senha
    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == 'hylbert' and senha == 'dev':
            self.mensagem['text'] = 'Autenticado'
        else:
            self.mensagem['text'] = 'Erro na autenticação'
     
root = Tk() # Essa classe permite que os widgets possam ser utilizados na aplicação.
Application(root)
'''
Em Application(root) passamos a variável root como parâmetro do método construtor da classe Application.
E para finalizar, chamamos o método root.mainloop() para exibirmos a tela. Sem o event loop, a interface não será exibida.
'''
root.mainloop()