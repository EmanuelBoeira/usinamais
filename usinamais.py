from turtle import width
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

#----------CALCULOS----------
#função de custo em função da velocidade de avanço
def C(va):
    taylor = []
    taylor = Taylor(float(tt1.get()), float(va1.get()), float(tt2.get()), float(va2.get()))

    resistMat = 450#float(resistMat.get()) #450 é para o aço 1045

    for material, tensao in listaDeMateriais:
        if(str(material) == str(tipoMaterial.get())):
            resistMat = int(tensao)

    pf = 1000
    L = float(comprimento.get())
    x = taylor[0]
    K = taylor[1]
    so = 10
    ce = 5
    af = float(profundidade.get())
    ae = float(largura.get())
    rendimento = 0.7#float(rendimento.get())

    return (pf * L * va**(x-1)/K) + ((so/60) * L/va) + (ce * af * ae * resistMat * L/(60000 * rendimento))

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
    labelVa = tk.Label(frameTabela, text="vel. avanço(m/min)")
    labelVa.grid(row=0, column=0, padx=10)
    labelCusto = tk.Label(frameTabela, text="custo(R$)")
    labelCusto.grid(row=0, column=1, padx=10)

    for i in range(int(min.get()), int(max.get()), 10):
        labelResultadoVa = tk.Label(frameTabela, text=str(i))
        labelResultadoVa.grid(row=i+1, column=0, padx=10)
        labelResultadoCusto = tk.Label(frameTabela, text=str(C(i)))
        labelResultadoCusto.grid(row=i+1, column=1, padx=10)

def MostraResultado():
    MostraTabela()
    MostraGrafico()


#----------GUI----------
#instancia de tk
root = tk.Tk()
#icone do app
#root.iconbitmap("usinamais.ico")
root.title("usina+")

#---imagens de referencia---
img1 = tk.PhotoImage(file="ref0.png")
img2 = tk.PhotoImage(file="ref1.png")

#---matriz com resistencias dos materiais---
listaDeMateriais = [["aço 1045", "450"], ["ferro fundido", "750"]]

#---frames---
frameDados = tk.Label(root)
frameDados.grid(row=0, column=0)

frameImagem = tk.Label(frameDados)
frameImagem.grid(row=0, column=0)

frameDados1 = tk.Label(frameDados)
frameDados1.grid(row=1, column=0, pady=20)

frameDados2 = tk.Label(frameDados)
frameDados2.grid(row=2, column=0, pady=20)

frameValores = tk.Label(frameDados)
frameValores.grid(row=3, column=0, pady=20)

frameTabela = tk.Label(root)
frameTabela.grid(row=0, column=1)

#---elementos da frameImagem---
labelImagem = tk.Label(frameImagem, image=img1)
labelImagem.grid(row=0, column=0)

#---elementos de frameDados1---
tipoUsinagem = tk.StringVar()
tipoUsinagem.set("fresamento")

fresamento = tk.Radiobutton(frameDados1, text="fresamento", variable=tipoUsinagem, value="fresamento")
fresamento.pack(anchor=tk.W)

furacao = tk.Radiobutton(frameDados1, text="furação", variable=tipoUsinagem, value="furacao")
furacao.pack(anchor=tk.W)

tipoMaterial = tk.StringVar()
tipoMaterial.set("aço 1045")

dropMateriais = tk.OptionMenu(frameDados1, tipoMaterial, "aço 1045", "ferro fundido")
dropMateriais.pack(anchor=tk.W)

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

#---elementos da frameValores---
label9 = tk.Label(frameValores, text="vel. de avanço(m/min):")
label9.grid(row=0, column=1)

min = tk.Entry(frameValores, width=10)
min.grid(row=1, column=0)

label10 = tk.Label(frameValores, text="até")
label10.grid(row=1, column=1)

max = tk.Entry(frameValores, width=10)
max.grid(row=1, column=2)

botaoGrafico = tk.Button(frameValores, text="gerar resultados", command=MostraResultado)
botaoGrafico.grid(row=2, column=1, pady=10)

#---loop---
root.mainloop()
