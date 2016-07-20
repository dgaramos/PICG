#Primeira Lista PIGC

#Imports necessarios
import matplotlib.pyplot as plt
import matplotlib.image as npimg
import numpy as np


#_____________Funcao imread (segunda questao)
def imread (imagem): #inserindo imagem por parametro
    img = npimg.imread(imagem) #Convertendo a imagem para ndarray
    print img #Verificando conversao da imagem

    plt.imshow(img) #Convertendo ndarray para pyplot
    plt.show()  #imprimindo pyplot


def size (imagem):
    img = npimg.imread(imagem)
    imgplot = plt.imshow(img)
    print imgplot

#testando funcoes
#imread ('gostosa.jpg') #terceira questao

size('gostosa.jpg')
