import tkinter

#classe button:
def button_clic():
    print("aguardando clique")
    novo_texto = entrada.get()
    minha_label.config(text= novo_texto)



window = tkinter.Tk()
window.title("Test GUI Program")
window.minsize(width=500, height=300)  #tamanho minimo da tela
window.config(padx=100, pady=200) #pad é acochoamento da janela. Acrescenta o espaço/recuo das estremidades da janela.

#classe label do tkinter:  (etiquetasou rótulos):

minha_label = tkinter.Label(text="Eu sou um rótulo", font=("Arial", 24, "bold"))
minha_label.grid(column=0, row= 0)   #faz aparecer o rótulo na janela utilizando o modulo grid
#O METODO PLACE E O METODO GRID. place utilizada coodernadas x e y e grid linhas e colunas como um planilha.
minha_label.config(padx=20, pady=20)

#Button:
button_2 = tkinter.Button(text="novo botão")
button_2.grid(column=2, row=0)
button_2.config(padx=20, pady=20)

button = tkinter.Button(text="Clique aqui", command=button_clic)  #função command é do tkinter.. inicia a função criada acima
button.grid(column=1, row=1)      #para embalar no ecrã
button.config(padx=20, pady=20)

#classe Entry:   (espécie de imput)
entrada = tkinter.Entry(width=10)
print(entrada.get())
entrada.grid(column=3, row=2)




window.mainloop()  #deixar esta linha sempre no fim do programa.... para manter a janela aberta como em uma espécie de while loop até que... 
