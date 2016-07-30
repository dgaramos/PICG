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
	img = imread(imagem) #Convertendo a imagem para ndarray
	newimg = img.copy() #Hardcopy
	if ( nchannels(imagem) == 3): #Se for colorida, converte e retorna a imagem convertida
		gray = np.dot(newimg[...,:3],[0.299, 0.587, 0.144])#Multiplicacao de matrizes: a matriz da imagem pelo vetor de pesos.
		return gray
	else: # Se nao for, retorna a imagem
		return newimg


#_____________Funcao imreadgray (sexta questao)
def imreadgray(imagem):
	if (nchannels(imagem) == 3):
		return rgb2gray(imagem)
	else:
		return imread(imagem)

#_____________Funcao imshow (setima questao)
def imshow(imagem):
	img = imread(imagem)
	newimg = img.copy() #Hardcopy da imagem
	if (nchannels(imagem) != 3):
		#Se a imagem for cinza
		plt.imshow(newimg,cmap = plt.get_cmap('gray'),interpolation="nearest")
		plt.show()
	else:
		image=plt.imshow(newimg, interpolation="nearest")
		plt.show()


#_____________Funcao thresh (oitava questao)
def thresh(imagem, lim):
    img = imread(imagem)
    newImg = img.copy()
    if (nchannels(imagem) == 1): #verificando imagem em escala de cinza
        for x in range(0, len(newImg)): #iterando array em largura e altura
            for y in range(0, len(newImg[0])):
                if (newImg[x][y] >= lim): #Verificando limiar
                    newImg[x][y] = 255
                else:
                    newImg[x][y] = 0
    else: #verificando imagem RGB
        for x in range(0, len(newImg)): #iterando array em largura e altura
            for y in range(0, len(newImg[0])):
                if (newImg[x][y][0] >= lim): #Verificando limiar
                    newImg[x][y][0] = 255
                else:
                    newImg[x][y][0] = 0
                if (newImg[x][y][1] >= lim):
                    newImg[x][y][1] = 255
                else:
                    newImg[x][y][1] = 0
                if (newImg[x][y][2] >= lim):
                    newImg[x][y][2] = 255
                else:
                    newImg[x][y][2] = 0
    #plt.imshow(newImg) #Convertendo ndarray para pyplot
    #plt.show()
    return newImg

#_____________Funcao negative (nona questao)
def negative(imagem):
    img = imread(imagem)
    newImg = img.copy()
    if (nchannels(imagem) == 1): #verificando imagem em escala de cinza
        for x in range(0, len(newImg)): #iterando array em largura e altura
            for y in range(0, len(newImg[0])):
                newImg[x][y] = 255 - newImg[x][y] #Invertendo a imagem
    else: #verificando imagem RGB
        for x in range(0, len(newImg)): #iterando array em largura e altura
            for y in range(0, len(newImg[0])):
                newImg[x][y][0] = 255 - newImg[x][y][0] #Invertendo a imagem
                newImg[x][y][1] = 255 - newImg[x][y][1]
                newImg[x][y][2] = 255 - newImg[x][y][2]
    #plt.imshow(newImg) #Convertendo ndarray para pyplot
    #plt.show()
    return newImg

#_____________Funcao contrast (decima questao)
def contrast(imagem, r, m):
    img = imread(imagem)
    newImg = img.copy()
    if (nchannels(imagem) == 1): #verificando imagem em escala de cinza
        for x in range(0, len(newImg)): #iterando array em largura e altura
            for y in range(0, len(newImg[0])):
                newImg[x][y] = r*(img[x][y]-m)+m
    else: #verificando imagem RGB
        for x in range(0, len(newImg)): #iterando array em largura e altura
            for y in range(0, len(newImg[0])):
                newImg[x][y][0] = r*(img[x][y][0]-m)+m
                newImg[x][y][1] = r*(img[x][y][1]-m)+m
                newImg[x][y][2]= r*(img[x][y][2]-m)+m
    plt.imshow(newImg) #Convertendo ndarray para pyplot
    plt.show()
    return newImg

#_______________Funcao hist (Decia primeira questao)
def hist(imagem):
		
	img = imread(imagem)
	tamanho = size(imagem)
	resultado_colorido = [[0 for x in range(3)] for y in range(256)] #Cria uma matriz de 3 coluna e 255 linhas
	resultado_cinza = [0 for x in range (256)] #Cria um vetor de 255 posicoes

	if (nchannels(imagem) == 3):#Imagem colorida
		for x in range(0, len(img)): 	#Eixo x
			for y in xrange(0, len(img[0])): #Eixo y
				resultado_colorido[img[x][y][0]] [0] = (resultado_colorido[img[x][y][0]][0]) + 1 #R
				resultado_colorido[img[x][y][1]] [1] = (resultado_colorido[img[x][y][1]][0]) + 1 #G
				resultado_colorido[img[x][y][2]] [2] = (resultado_colorido[img[x][y][0]][0]) + 1 #B
		return resultado_colorido

	else: #Imagem cinza
		for x in xrange(0, len(img)):
			for y in xrange(0, len(img[0])):
				resultado_cinza[img[x][y]] = (resultado_cinza[img[x][y]]) + 1
		return resultado_cinza
	

#-------------------testando funcoes------------------------
#print imread ('gostosa.jpg') #segunda questao letra a
#print imread ('gostosa.tif') #segunda questao letra b
#print imread ('50x50.gif') #segunda questao letra c
#print nchannels('gostosa.tif') #terceira questao com escala de cinza
#print nchannels('gostosa.jpg') #terceira questao com RGB
#print size ('gostosa.jpg') #imprimindo quarta questao
#print rgb2gray('gostosa.tif')#quinta questao
#print rgb2gray('gostosa.tif') #quinta questao
#print imreadgray('gostosa.jpg') #sexta questao
#print imreadgray('gostosa.tif') #sexta questao
#print imshow('gostosa.jpg') #setima questao
#print imshow('gostosa.tif') #setima questao
#thresh('gostosa.jpg', 100) #oitava questao
#negative('gostosa.jpg') #nona questao
#contrast('gostosa.jpg', 0.761354, 1000)
#print hist('gostosa.tif')

'''SCRATCHPAD
=========================SATURACAO===================
newImg[x][y][0] = r*(img[x][y][0]-m)+m
if (newImg[x][y][0] >= 255):
    newImg[x][y][0]  = 255
elif (newImg[x][y][0] <= 0):
    newImg[x][y][0] = 0
newImg[x][y][1] = r*(img[x][y][1]-m)+m
if (newImg[x][y][1] >= 255):
    newImg[x][y][1]  = 255
elif (newImg[x][y][1] <= 0):
    newImg[x][y][1] = 0
newImg[x][y][2]= r*(img[x][y][2]-m)+m
if (newImg[x][y][2]  >= 255):
    newImg[x][y][2]  = 255
elif (newImg[x][y][2] <= 0):
    newImg[x][y][2] = 0'''
