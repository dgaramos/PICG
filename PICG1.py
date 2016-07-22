'''Primeira Lista PIGC
Alunos: Alexandre Santos Maciel
        Danilo Goncalves Alves Ramos
'''
#Imports necessarios
import matplotlib.pyplot as plt
import matplotlib.image as npimg
import numpy as np


#_____________Funcao imread (segunda questao)
def imread (imagem): #inserindo imagem por parametro
    img = npimg.imread(imagem) #Convertendo a imagem para ndarray
    print img #Verificando conversao da imagem

#    plt.imshow(img) #Convertendo ndarray para pyplot
#    plt.show()  #imprimindo ndarray como imagem

#_____________Funcao nchannels (terceira questao)
def nchannels (imagem): #inserindo imagem por parametro
    img = npimg.imread(imagem) #Convertendo a imagem para ndarray
#verificando se a imagem tem mais de uma cor
    try:
        print len(img[0][0])
    except:
        print 1

#_____________Funcao size (quarta questao)
def size (imagem): #inserindo imagem por parametro
    img = npimg.imread(imagem) #Convertendo a imagem para ndarray
#criando um array size com a primeira posicao sendo a largura e a segunda sendo a altura
    size = [len(img[0]), len(img)]

    print size

#_____________Funcao rgb2gray (quinta questao)
def rgb2gray(imagem):
	img = npimg.imread(imagem)#Convertendo a imagem para ndarray
 	gray = np.dot(img[...,:3],[0.299, 0.587, 0.144])#Multiplicacao de matrizes: a matriz da imagem pelo vetor de pesos.
	plt.imshow(gray, cmap = plt.get_cmap('gray'))
	plt.show()#Imprime a imagem

#_____________Funcao imreadgray (sexta questao)
def imreadgray(imagem):
	img = npimg.imread(imagem) #Convertendo a imagem para ndarray
	try:
		gray = np.dot(img[...,:3],[0.299, 0.587, 0.144])#Multiplicacao de matrizes: a matriz da imagem pelo vetor de pesos.
		plt.imshow(gray, cmap = plt.get_cmap('gray'))
		plt.show()#Imprime a imagem
	except:
		plt.imshow(img, cmap = plt.get_cmap('gray')) #Convertendo ndarray para pyplot
		plt.show() #imprimindo ndarray como imagem


#-------------------testando funcoes------------------------
#imread ('gostosa.jpg') #segunda questao letra a
#imread ('gostosa.tif') #segunda questao letra b
#imread ('50x50.gif') #segunda questao letra c
#nchannels('gostosa.tif') #terceira questao com escala de cinza
#nchannels('gostosa.jpg') #terceira questao com RGB
#size ('gostosa.jpg')#imprimindo quarta questao
#rgb2gray('gostosa.jpg')#quinta questao
#imreadgray('gostosa.jpg')
#imreadgray('gostosa.tif')
