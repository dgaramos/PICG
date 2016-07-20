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

#_____________Funcao nchannels (terceira questao)
def nchannels (imagem): #inserindo imagem por parametro
    img = npimg.imread(imagem) #Convertendo a imagem para ndarray
    print len(img[1])




def size (imagem):
    img = npimg.imread(imagem)
    le = img.shape

    print le

#testando funcoes
#imread ('gostosa.tif') #terceira questao
#nchannels('gostosa.tif')
#nchannels('gostosa.jpg')
size('gostosa.jpg')
