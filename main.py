import tkinter

window = tkinter.Tk()
window.title("Test GUI Program")
window.minsize(width=500, height=300)  #tamanho minimo da tela

#classe label do tkinter:  (etiquetasou rótulos):

minha_label = tkinter.Label(text="Eu sou um rótulo", font=("Arial", 24, "bold"))
minha_label.pack()   #faz aparecer o rótulo na janela







window.mainloop()  #deixar esta linha sempre no fim do programa.... para manter a janela aberta como em uma espécie de while loop até que... 
