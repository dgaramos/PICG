'''Primeira Lista PIGC
Alunos: Alexandre Santos Maciel
        Danilo Goncalves Alves Ramos
'''
#Imports necessarios
import matplotlib.pyplot as plt
import matplotlib.image as npimg
import matplotlib.colors as plt_color
import numpy as np


#_____________Funcao imread (segunda questao)
def imread (imagem): #inserindo imagem por parametro
    img = npimg.imread(imagem) #Convertendo a imagem para ndarray
    return img #Verificando conversao da imagem

#_____________Funcao nchannels (terceira questao)
def nchannels (imagem): #inserindo imagem por parametro
    img = imread(imagem) #Convertendo a imagem para ndarray
#verificando se a imagem tem mais de uma cor
    try:
        return len(img[0][0])
    except:
        return 1

#_____________Funcao size (quarta questao)
def size (imagem): #inserindo imagem por parametro
    img = imread(imagem) #Convertendo a imagem para ndarray
    size = [len(img[0]), len(img)] #criando um array size com a primeira posicao sendo a largura e a segunda sendo a altura
    return size

#_____________Funcao rgb2gray (quinta questao)
def rgb2gray(imagem):
	if (nchannels(imagem) == 3):
		img = imread(imagem)#Convertendo a imagem para ndarray
		gray = np.dot(img[...,:3],[0.299, 0.587, 0.144])#Multiplicacao de matrizes: a matriz da imagem pelo vetor de pesos.
		return gray
	else:
		print "Essa imagem ja esta em escala de cinza.\nPor favor insira uma imagem RGB para que possa ser convertida"

#_____________Funcao imreadgray (sexta questao)
def imreadgray(imagem):
	if (nchannels(imagem) == 3):
		return rgb2gray(imagem)
	else:
		return imread(imagem)

#_____________Funcao rgb2gray2 (quinta questao)
def rgb2gray2(imagem):
	img = imread(imagem) #Convertendo a imagem para ndarray
	try:
		gray = np.dot(img[...,:3],[0.299, 0.587, 0.144])#Multiplicacao de matrizes: a matriz da imagem pelo vetor de pesos.
		plt.imshow(gray, cmap = plt.get_cmap('gray'))
		plt.show()#Imprime a imagem
	except:
		plt.imshow(img, cmap = plt.get_cmap('gray')) #Convertendo ndarray para pyplot
		plt.show() #imprimindo ndarray como imagem


#_____________Funcao negative (nona questao)
def imshow(imagem):
	img = imread(imagem)
	if (nchannels(imagem) != 3):
		
		plt.imshow(img,cmap = plt.get_cmap('gray'))
		plt.show()
	else:
		image=plt.imshow(img, interpolation="nearest")
		plt.show()
		


#-------------------testando funcoes------------------------
#print imread ('gostosa.jpg') #segunda questao letra a
#print imread ('gostosa.tif') #segunda questao letra b
#print imread ('50x50.gif') #segunda questao letra c
#print nchannels('gostosa.tif') #terceira questao com escala de cinza
#print nchannels('gostosa.jpg') #terceira questao com RGB
#print size ('gostosa.jpg') #imprimindo quarta questao
#print rgb2gray('gostosa.jpg') #quinta questao
#print rgb2gray('gostosa.tif') #quinta questao
#print imreadgray('gostosa.jpg') #sexta questao
#print imreadgray('gostosa.tif') #sexta questao
#print imshow('gostosa.jpg') #setima questao
#print imshow('gostosa.tif') #setima questao
imshow('gostosa.tif')
