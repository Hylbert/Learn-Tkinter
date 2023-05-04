'''

Fonte: https://www.devmedia.com.br/tkinter-interfaces-graficas-em-python/33956

'''
from operator import le
from tkinter import*
from tkinter import font
from turtle import left

'''
Container – É uma analogia a um container físico e tem como objetivo organizar e guardar objetos. Da mesma forma este conceito serve para um container em interface. Nesse caso, os objetos que estamos armazenando são os widgets;
Widget – É um componente qualquer na tela, que pode ser um botão, um ícone, uma caixa de texto, etc.;
Event Handler – São tratadores de eventos. Por exemplo, ao clicarmos em um botão para executar uma ação, uma rotina é executada. Essa rotina é chamada de event handler;
Event Loop – O event loop verifica constantemente se outro evento foi acionado. Caso a hipótese seja verdadeira, ele irá executar a rotina correspondente.

'''
class Application:
    def __init__(self, master = None):

        '''
        O módulo Tkinter oferece três formas de trabalharmos com geometria e posicionamento:

        1. Pack;
        2. Grid;
        3. Place

        Caso um widget não seja aplicado a nenhum gerenciador geométrico, ele continua existindo, mas invisível ao usuário.
        
        '''
              
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

        '''
        Vamos ver algumas configurações de estilo mais comuns que podemos definir:

        Width – Largura do widget;
        Height – Altura do widget;
        Text – Texto a ser exibido no widget;
        Font – Família da fonte do texto;
        Fg – Cor do texto do widget;
        Bg – Cor de fundo do widget;
        Side – Define em que lado o widget se posicionará (Left, Right, Top, Bottom).
        '''

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