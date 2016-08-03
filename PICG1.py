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
def nchannels (img): #inserindo imagem por parametro
    #verificando se a imagem tem mais de uma cor
    try:
        return len(img[0][0])
    except:
        return 1

#_____________Funcao size (quarta questao)
def size (img): #inserindo imagem por parametro
    size = [len(img[0]), len(img)] #criando um array size com a primeira posicao sendo a largura e a segunda sendo a altura
    return size

#_____________Funcao rgb2gray (quinta questao)
def rgb2gray(img):
	newImg = img.copy() #Hardcopy
	if ( nchannels(img) == 3): #Se for colorida, converte e retorna a imagem convertida
		gray = np.dot(newImg[...,:3],[0.299, 0.587, 0.144])#Multiplicacao de matrizes: a matriz da imagem pelo vetor de pesos.
		return gray
	else: # Se nao for, retorna a imagem
		return newImg

#_____________Funcao imreadgray (sexta questao)
def imreadgray(img):
	if (nchannels(img) == 3):
		return rgb2gray(img)
	else:
		return img

#_____________Funcao imshow (setima questao)
def imshow(img):
	newImg = img.copy() #Hardcopy da imagem
	if (nchannels(img) != 3):
		#Se a imagem for cinza
		plt.imshow(newImg,cmap = plt.get_cmap('gray'),interpolation="nearest")
		plt.show()
	else:
		image=plt.imshow(newImg, interpolation="nearest")
		plt.show()


#_____________Funcao thresh (oitava questao)
def thresh(img, lim):
    newImg = img.copy()
    if (nchannels(img) == 1): #verificando imagem em escala de cinza
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
    return newImg

#_____________Funcao negative (nona questao)
def negative(img):
    newImg = img.copy()
    if (nchannels(img) == 1): #verificando imagem em escala de cinza
        for x in range(0, len(newImg)): #iterando array em largura e altura
            for y in range(0, len(newImg[0])):
                newImg[x][y] = 255 - newImg[x][y] #Invertendo a imagem
    else: #verificando imagem RGB
        for x in range(0, len(newImg)): #iterando array em largura e altura
            for y in range(0, len(newImg[0])):
                newImg[x][y][0] = 255 - newImg[x][y][0] #Invertendo a imagem
                newImg[x][y][1] = 255 - newImg[x][y][1]
                newImg[x][y][2] = 255 - newImg[x][y][2]
    return newImg

#_____________Funcao contrast (decima questao)
def contrast(img, r, m):
    newImg = img.copy()
    if (nchannels(img) == 1): #verificando imagem em escala de cinza
        for x in range(0, len(newImg)): #iterando array em largura e altura
            for y in range(0, len(newImg[0])):
                tmp = r*(img[x][y]-m)+m
                if (tmp >= 255):
                    newImg[x][y]  = 255
                elif (tmp <= 0):
                    newImg[x][y] = 0
    else: #verificando imagem RGB
        for x in range(0, len(newImg)): #iterando array em largura e altura
            for y in range(0, len(newImg[0])):
                tmp = r*(img[x][y][0]-m)+m
                if (tmp >= 255):
                    newImg[x][y][0]  = 255
                elif (tmp <= 0):
                    newImg[x][y][0] = 0
                tmp = r*(img[x][y][1]-m)+m
                if (tmp >= 255):
                    newImg[x][y][1]  = 255
                elif (tmp <= 0):
                    newImg[x][y][1] = 0
                tmp= r*(img[x][y][2]-m)+m
                if (tmp  >= 255):
                    newImg[x][y][2]  = 255
                elif (tmp <= 0):
                    newImg[x][y][2] = 0
    return newImg

#_______________Funcao hist (Decia primeira questao)
def hist(img):
	tamanho = size(img)
	if (nchannels(img) == 3):#Imagem colorida
		resultado_colorido = [[0 for x in range(3)] for y in range(256)] #Cria uma matriz de 3 coluna e 255 linhas
		for x in xrange(0, len(img)): 	#Eixo x
			for y in xrange(0, len(img[0])): #Eixo y
				resultado_colorido[img[x][y][0]] [0] = (resultado_colorido[img[x][y][0]][0]) + 1 #R
				resultado_colorido[img[x][y][1]] [1] = (resultado_colorido[img[x][y][1]][0]) + 1 #G
				resultado_colorido[img[x][y][2]] [2] = (resultado_colorido[img[x][y][0]][0]) + 1 #B
		return resultado_colorido

	else: #Imagem cinza
		resultado_cinza = [0 for x in range (256)] #Cria um vetor de 255 posicoes
		for x in xrange(0, len(img)):
			for y in xrange(0, len(img[0])):
				resultado_cinza[img[x][y]] = (resultado_cinza[img[x][y]]) + 1
		return resultado_cinza

#_______________Funcao showhist( Decima segunda questao)
def showhist(imagem):
	try:
		red_pixels 		= [0 for x in range(256)]
		green_pixels 	= [0 for x in range(256)]
		blue_pixels 	= [0 for x in range(256)]

		for x in xrange(0,256):
			red_pixels[x] 		= imagem[x][0]
			green_pixels[x] 	= imagem[x][1]
			blue_pixels[x]		= imagem[x][2]

		fig, ax = plt.subplots()
		index = np.arange(256)
		bar_width = 0.10
		opacity = 0.8

		red = plt.bar(index, red_pixels, bar_width,
				           alpha=opacity,
				           color='r',
				           label='Red')

		green = plt.bar(index + bar_width, green_pixels, bar_width,
				           alpha=opacity,
				           color='g',
				           label='Green')

		blue = plt.bar(index + (bar_width * 2), blue_pixels, bar_width,
				           alpha=opacity,
				           color='b',
				           label='Blue')

		plt.xlabel('Intensidade')
		plt.ylabel('Frequencia')
		plt.title('Histograma')
		plt.xticks(index + bar_width, range(0,256))
		plt.legend()

		plt.tight_layout()
		plt.show()

	except:
		gray_pixels = [0 for x in range(256)]
		for x in range(0,256):
			gray_pixels[x] = imagem[x]

		fig, ax = plt.subplots()
		index = np.arange(256)
		bar_width = 0.10
		opacity = 0.8

		gray = plt.bar(index, gray_pixels, bar_width,
				           alpha=opacity,
				           color='g',
				           label='Gray')

		plt.xlabel('Intensidade')
		plt.ylabel('Frequencia')
		plt.title('Histograma')
		plt.xticks(index, range(0,256))
		plt.legend()

		plt.tight_layout()
		plt.show()

#_______________Funcao showhist ( Decima terceira questao)
#_______________Funcao showhist ( Decima terceira questao)
def showhist2(imagem,bin):
	
	try:
		red_pixels 		= [0 for x in range(256+1/bin)]
		green_pixels 	= [0 for x in range(256+1/bin)]	
		blue_pixels 	= [0 for x in range(256+1/bin)]
		counter = 0
		print 'okau'			
		for x in xrange(0,256):		
			if( x % bin == 0 and x != 0):
				counter +=1				
			
			red_pixels[counter] 		+= imagem[x][0]
			green_pixels[counter] 	+= imagem[x][1]
			blue_pixels[counter] 	+= imagem[x][2]
		print 'okau'	
		fig, ax = plt.subplots()
		index = np.arange(256+1/bin)
		bar_width = 0.15
		opacity = 0.8	
			 
		red = plt.bar(index, red_pixels, bar_width,
				           alpha=opacity,
				           color='r',
				           label='Red')
		 
		green = plt.bar(index + bar_width, green_pixels, bar_width,
				           alpha=opacity,
				           color='g',
				           label='Green')

		blue = plt.bar(index + (bar_width*2), blue_pixels, bar_width,
				           alpha=opacity,
				           color='b',
				           label='Blue')

		plt.xlabel('Intensidade')
		plt.ylabel('Frequencia')
		plt.title('Histograma')
		plt.xticks(index + bar_width, range(0,256/bin))
		plt.legend()
		 
		plt.tight_layout()
		plt.show()
	
	except:
		
		gray_pixels = [0 for x in range(0,256/bin)]
		counter = 0
		
		for x in range(0,256):
			if( x % bin == 0 and x != 0):
				counter +=1					
			gray_pixels[counter] += imagem[x]
			
	
		fig, ax = plt.subplots()
		index = np.arange(256/bin)
		bar_width = 0.102
		opacity = 0.8	

		gray = plt.bar(index, gray_pixels, bar_width,
				           alpha=opacity,
				           color='g',
				           label='Gray')

		plt.xlabel('Intensidade')
		plt.ylabel('Frequencia')
		plt.title('Histograma')
		plt.xticks(index, range(0,256/bin))
		plt.legend()
		 
		plt.tight_layout()
		plt.show()


#_______________Funcao convolve ( Decima quinta questao)
def convolve(img,mask):



#-------------------testando funcoes------------------------

scarlet = imread('gostosa.jpg')
scarletG = imread('gostosa.tif')

#print scarlet #segunda questao letra a
#print scarletG #segunda questao letra b
#print imread ('50x50.gif') #segunda questao letra c
#print nchannels(scarlet) #terceira questao com RGB
#print nchannels(scarletG) #terceira questao com escala de cinza
#print size (scarlet) #imprimindo quarta questao
#print rgb2gray(scarlet)#quinta questao
#print rgb2gray(scarletG) #quinta questao
#print imreadgray(scarlet) #sexta questao
#imshow(scarlet) #setima questao
#print imreadgray(scarletG) #sexta questao
#imshow(scarlet) #setima questao
#imshow(scarletG) #setima questao
#imshow(thresh(scarlet, 100)) #oitava questao
#imshow(negative(scarlet)) #nona questao
#imshow(contrast(scarlet, 3.0, 128))
#print hist(scarletG)
#showhist(hist(scarlet))
#showhist(hist(scarlet))
showhist2(hist(scarlet),5)
#showhist2(hist(scarlet),5)
