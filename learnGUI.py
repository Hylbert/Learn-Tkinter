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
        self.msg['font'] = ('Verdana', '10', 'italic', 'bold')
        self.msg.pack()
        self.sair = Button(self.widget1)
        self.sair['text'] = 'Sair'
        self.sair['font'] = ('Verdana', '10')
        self.sair['width'] = 5
        self.sair['command'] = self.widget1.quit
        self.sair.pack(side=RIGHT) # SIDE =  Define em que lado o widget se posicionará (Left, Right, Top, Bottom)
root = Tk() # Essa classe permite que os widgets possam ser utilizados na aplicação.
Application(root)
'''
Em Application(root) passamos a variável root como parâmetro do método construtor da classe Application.
E para finalizar, chamamos o método root.mainloop() para exibirmos a tela. Sem o event loop, a interface não será exibida.
'''
root.mainloop()