import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

#----------CALCULOS----------
#função de custo em função da velocidade de avanço
def C(va):
    taylor = []
    taylor = Taylor(float(tt1.get()), float(va1.get()), float(tt2.get()), float(va2.get()))

    pf = 1000
    L = float(comprimento.get())
    x = taylor[0]
    K = taylor[1]
    so = 10
    ce = 5
    af = float(profundidade.get())
    ae = float(largura.get())
    resistMat = 450#float(resistMat.get()) #450 é para o aço 1045
    rendimento = 0.7#float(rendimento.get())

    return (pf * L * va**(x-1)/K) + (so * L/va) + (ce * af * ae * resistMat/(3600000000 * rendimento))

#retorna os valores de x e K pela equação de Taylor para desgaste
def Taylor(tt1, va1, tt2, va2):
    x = np.log(tt2/tt1) / np.log(va1/va2)
    x = round(x)
    K = tt1 * va1**x
    K = round(K)

    return x, K

#abre uma tela com o grafico de custo X velocidade de avanço
def MostraGrafico():
    xx = np.linspace(int(min.get()), int(max.get()))
    plt.plot(xx, C(xx))
    plt.grid()
    plt.show()

def MostraTabela():
    for i in range(int(min.get()), int(max.get()), 10):
        texto = "vel. avanço: "+ str(i) + "custo: " + str(C(i))
        labelResultado = tk.Label(frameTabela, text=texto)
        labelResultado.pack()

def MostraResultado():
    MostraTabela()
    MostraGrafico()

#----------GUI----------
#instancia de tk
root = tk.Tk()
#root.iconbitmap("usinamais.ico")
root.title("usina+")

#---imagens de referencia---
img1 = tk.PhotoImage(file="ref0.png")
img2 = tk.PhotoImage(file="ref1.png")

#---frames---
frameImagem = tk.Label(root)
frameImagem.grid(row=0, column=0)

frameDados1 = tk.Label(root)
frameDados1.grid(row=1, column=0)

frameDados2 = tk.Label(root)
frameDados2.grid(row=2, column=0)

frameValores = tk.Label(root)
frameValores.grid(row=0, column=1)

frameTabela = tk.Label(root)
frameTabela.grid(row=2, column=1)

#---elementos da frameImagem---
labelImagem = tk.Label(frameImagem, image=img1)
labelImagem.pack()

#---elementos de frameDados1---
tipoUsinagem = tk.StringVar()
tipoUsinagem.set("fresamento")

fresamento = tk.Radiobutton(frameDados1, text="fresamento", variable=tipoUsinagem, value="fresamento")
fresamento.pack(anchor=tk.W)

furacao = tk.Radiobutton(frameDados1, text="furação", variable=tipoUsinagem, value="furacao")
furacao.pack(anchor=tk.W)

#---elementos de frameDados2---
label1 = tk.Label(frameDados2, text="af(m):")
label1.grid(row=0, column=0)
profundidade = tk.Entry(frameDados2, width=10)
profundidade.grid(row=0, column=1)

label2 = tk.Label(frameDados2, text="ae(m):")
label2.grid(row=0, column=2)
largura = tk.Entry(frameDados2, width=10)
largura.grid(row=0, column=3)

label3 = tk.Label(frameDados2, text="L(m):")
label3.grid(row=1, column=0)
comprimento = tk.Entry(frameDados2, width=10)
comprimento.grid(row=1, column=1)

label4 = tk.Label(frameDados2, text="rendimento(%):")
label4.grid(row=1, column=2)
rendimento = tk.Entry(frameDados2, width=10)
rendimento.grid(row=1, column=3)

label5 = tk.Label(frameDados2, text="vida útil 1(min):")
label5.grid(row=2, column=0)
tt1 = tk.Entry(frameDados2, width=10)
tt1.grid(row=2, column=1)

label6 = tk.Label(frameDados2, text="vel. avanço 1(m/min):")
label6.grid(row=2, column=2)
va1 = tk.Entry(frameDados2, width=10)
va1.grid(row=2, column=3)

label7 = tk.Label(frameDados2, text="vida útil 2(min):")
label7.grid(row=3, column=0)
tt2 = tk.Entry(frameDados2, width=10)
tt2.grid(row=3, column=1)

label8 = tk.Label(frameDados2, text="vel. avanço 2(m/min):")
label8.grid(row=3, column=2)
va2 = tk.Entry(frameDados2, width=10)
va2.grid(row=3, column=3)

botaoGrafico = tk.Button(frameDados2, text="gerar resultados", command=MostraResultado)
botaoGrafico.grid(row=4, column=3)

#---elementos da frameValores---
label9 = tk.Label(frameValores, text="vel. de avanço(m/min):")
label9.grid(row=0, column=1)

min = tk.Entry(frameValores, width=10)
min.grid(row=1, column=0)

label10 = tk.Label(frameValores, text="até")
label10.grid(row=1, column=1)

max = tk.Entry(frameValores, width=10)
max.grid(row=1, column=2)

#---loop---
root.mainloop()