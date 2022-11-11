from tkinter import * #dessa forma importa todos as classes

janela = Tk() #importa a classe tk
janela.title("Conversor de milhas para kilometro")
janela.minsize(width=200, height=100)
janela.config(padx=20, pady=10)  #acochoamento da janela

#entrada/entry
milhas_imput = Entry(width=7) #eidth a largura do campo de entrada
milhas_imput.grid(column=1, row=0)


#etiqueta/label
milhas_etiqueta = Label(text="Milhas")
milhas_etiqueta.grid(column=2, row=0)

igual_a = Label(text="é igual a")
igual_a.grid(column=0, row=1)

resultado_km = Label(text= "0")
resultado_km.grid(column=1, row=1)

km_etiqueta = Label(text="Km")
km_etiqueta.grid(column=2, row=1)

#Button
botao_calcular = Button(text="Calcular")
botao_calcular.grid(column=1, row=3)





janela.mainloop()