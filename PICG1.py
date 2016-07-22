#Primeira Lista PIGC

#Imports necessarios
import matplotlib.pyplot as plt
import matplotlib.image as npimg
import numpy as np

#_____________Funcao imread (segunda questao)
def imread (imagem): #inserindo imagem por parametro
    img = npimg.imread(imagem) #Convertendo a imagem para ndarray
    print img #Verificando conversao da imagem

#    plt.imshow(img) #Convertendo ndarray para pyplot
#    plt.show()  #imprimindo imagem como imagem

#_____________Funcao nchannels (terceira questao)
def nchannels (imagem): #inserindo imagem por parametro
    img = npimg.imread(imagem) #Convertendo a imagem para ndarray
    print len(img[0])

#_____________Funcao rgb2gray (quinta questao)
def rgb2gray(imagem):
	img = npimg.imread(imagem)
 	gray = np.dot(img[...,:3],[0.299, 0.587, 0.144])#Pesos especificados no pdf
	plt.imshow(gray, cmap = plt.get_cmap('gray'))
	plt.show()	

def size (imagem):
    img = npimg.imread(imagem)
    size = [len(img[0]), len(img)]

    print size

#testando funcoes
#imread ('gostosa.jpg') #segunda questao letra a
#imread ('gostosa.tif') #segunda questao letra b
#imread ('50x50.gif') #segunda questao letra c
#nchannels('gostosa.tif')
#nchannels('gostosa.jpg')
rgb2gray('gostosa.jpg')
#size ('gostosa.jpg')
#size('gostosa.jpg')
