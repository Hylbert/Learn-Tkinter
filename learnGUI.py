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
        self.msg.pack()

root = Tk() # Essa classe permite que os widgets possam ser utilizados na aplicação.
Application(root)
'''
Em Application(root) passamos a variável root como parâmetro do método construtor da classe Application.
E para finalizar, chamamos o método root.mainloop() para exibirmos a tela. Sem o event loop, a interface não será exibida.
'''
root.mainloop()