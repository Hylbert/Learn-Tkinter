'''
Fonte: https://www.devmedia.com.br/tkinter-interfaces-graficas-em-python/33956

'''
from tkinter import*

class Application:
    def __init__(self, master = None):
        self.widget1 = Frame(master) 
        ''' O frame master é o nosso top level, que é o elemento máximo da hierarquia, 
        ou seja, é a nossa janela de aplicação, que contém o título, e botões de maximizar, minimizar e fechar.'''
        self.widget1.pack()
        self.msg = Label(self.widget1, text = 'Primeiro widget')
        self.msg['font'] = ('Calibri', '9', 'italic')
        self.msg.pack()
        self.sair = Button(self.widget1)
        self.sair['text'] = 'Clique aqui'
        self.sair['font'] = ('Calibri', '9')
        self.sair['width'] = 10
        self.sair.bind('<Button-1>', self.mudarTexto) # event handler = são ações executadas como resposta a determinado evento
        #ou self.sair['command'] = self.mudarTexto
        self.sair.pack() # SIDE =  Define em que lado o widget se posicionará (Left, Right, Top, Bottom)

    def mudarTexto(self, event): # event handler
        if self.msg['text'] == 'Primeiro widget':
            self.msg['text'] = 'O botão recebeu um clique'
        else:
            self.msg['text'] = 'Primeiro widget'
root = Tk() # Essa classe permite que os widgets possam ser utilizados na aplicação.
Application(root)
'''
Em Application(root) passamos a variável root como parâmetro do método construtor da classe Application.
E para finalizar, chamamos o método root.mainloop() para exibirmos a tela. Sem o event loop, a interface não será exibida.
'''
root.mainloop()