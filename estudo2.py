from tkinter import *

#Criando uma nova janela e configurações:
window = Tk()
window.title("Exemplos de widget")
window.minsize(width=500, height=500)

#Rótulos
label = Label(text="Este é um texto antigo")
label.config(text="Este é um novo texto")
label.pack()

#Buttons
def action():
    print("Faça alguma coisa")

#chama action() quando pressionado:
button = Button(text="Clique em mim", command=action)
button.pack()

#Entradas
entry = Entry(width=30)
#Adicione algum texto para começar:
entry.insert(END, string="Algum texto para começar.")
#Obtém texto na entrada:
print(entry.get())
entry.pack()

#Texto
text = Text(height=5, width=30)
#Coloca o cursor na caixa de texto:
text.focus()
#Adiciona algum texto para começar:
text.insert(END, "Exemplo de entrada de texto de várias linhas.")
#Get valor atual na caixa de texto na linha 1, caractere 0:
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    #obtém o valor atual no spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Escala
#Chamado com valor de escala atual.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton #botão de verificação:
def checkbutton_used():
    # Imprime 1 se o botão Ligado estiver marcado, caso contrário, 0.:
    print(checked_state.get())
#variável para manter o estado verificado, 0 está desligado, 1 está ligado.:
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton #Botao de radio:
def radio_used():
    print(radio_state.get())
#Variável para manter o valor do botão de opção verificado:
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Obtém a seleção atual da caixa de listagem
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Maçã", "Pera", "Laranja", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

#para manter a janela aberta:
window.mainloop()
