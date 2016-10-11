import PICG1 as picg
import math as math


a = (picg.imread("len_std.jpg"))
white = picg.imread("White.png")
gray_lena = picg.imread("lena.jpg")
#Dado um par de coordenadas (i,j), muda a posicao [i][j] da imagem, atribuindo
# a cor a essa posicao.
def drawPoint(imagem,i,j,cor):
    newImg = imagem.copy()
    #print newImg
    #Se a imagem for colorida, ou seja, tem tres canais
    if (picg.nchannels(newImg) == 3):
        newImg[i][j][0] = cor[0] #R
        newImg[i][j][1] = cor[1] #G
        newImg[i][j][2] = cor[2] #B
    else:
        newImg[i][j] = cor
    return newImg

#Recebe uma imagem, dois pares de coordenadas (i0,j0) e (i1,j1), uma cor
# e booleano fill.Desenha um retangulo nas coordenadas dadas e se fill for
#true, preenche o interior do retangulo com a cor
def drawRect(imagem,i0,j0,i1,j1,cor,fill):
    newImg = imagem.copy()
    if( i0 < i1 ):
            menorX = i0
            maiorX = i1
    else:
            menorX = i1
            maiorX = i0
    if ( j0 < j1):
            menorY = j0
            maiorY = j1
    else:
            menorY = j1
            maiorY = j0
    for y in range(menorY,maiorY):
        #print 'asdasd'   
        newImg = drawPoint(newImg,i1,y,cor)
    for y in range (menorY,maiorY):
        newImg = drawPoint(newImg,i0,y,cor)
            
    for x in range(menorX,maiorX):
        newImg = drawPoint(newImg,x,i1,cor)
        newImg = drawPoint(newImg,x,i0,cor)

    if( fill):
        for x in xrange(menorX,maiorX):
            for y in xrange(menorY,maiorY):
                newImg = drawPoint(newImg,x,y,cor)
    return newImg

#Terceira questao usa DDA
def drawLine(imagem,i0,j0,i1,j1,c):
    newImg = imagem.copy()

    dx = i1 - i0
    dy = j1 - j0
    x = i0
    y = j0
    steps = dx
    if ((dx) > (dy)):
        step = dx
    else:
        steps = dy
    print steps
    if( steps > 0):
        xInc = float(dx)/float(steps)

        yInc = float(dy)/float(steps)

    newImg = drawPoint(newImg,i0,j0,c)

    for k in xrange(0,steps):
        x += xInc
        y += yInc
        newImg = drawPoint(newImg,x,y,c)
  
    return newImg


#Quarta questao
def drawCircle(imagem,ci,cj,r,c):
    newImg = imagem.copy()
    x = 0.0
    y = float(r)
    newImg = drawPoint(newImg,(ci + 0),(cj + y),c)
    newImg = drawPoint(newImg,(ci + 0),(cj - y),c)
    newImg = drawPoint(newImg,(ci + y),(cj + x),c)
    newImg = drawPoint(newImg,(ci - y),(cj + x),c)
    while ( x <= y):
        x = x + 1.0
        y = math.sqrt( r * r- x * x)
        newImg = drawPoint(newImg,(ci + x), (cj + y),c)
        newImg = drawPoint(newImg,(ci + x), (cj - y),c)
        newImg = drawPoint(newImg,(ci - x), (cj + y),c)
        newImg = drawPoint(newImg,(ci - x), (cj - y),c)
        newImg = drawPoint(newImg,(ci + y), (cj + x),c)
        newImg = drawPoint(newImg,(ci + y), (cj - x),c)
        newImg = drawPoint(newImg,(ci - y), (cj + x),c)
        newImg = drawPoint(newImg,(ci - y), (cj - x),c)
    return newImg

#Quinta questao
def drawPoint2(imagem,S,i,j,c):
    newImg = imagem.copy
    size = picg.size(imagem)
    altura = size[1]
    largura = size[0]
    newImg = drawPoint(newImg,(i * S + altura/2),( j * S + largura/2), c)
    return newImg

#Sexta questao
def drawAxis(imagem,cor):
    newImg = imagem.copy()
    size = picg.size(imagem)
    altura = size[1]
    largura = size[0]
    #linha horizontal
    newImg = drawLine(newImg, altura / 2, 0, altura / 2, largura - 1, cor)
    #linha vertical
    newImg = drawLine(newImg, 0, altura / 2, largura - 1, altura / 2, cor) 
    return newImg

#Oitava questao
def translatePoint(imagem,i,j,ti,tj):
    return imagem[i+ti][j+tj]
    
#result = (drawRect(a,0,0,10,10,[1,100,50],0))
#picg.imshow(result)

#result = drawLine(gray_lena,11,0,200,200,0)
#print result
#picg.imshow(result)
#result = drawCircle(gray_lena, 50,50,40,50)
#picg.imshow(result)
#result = drawAxis(gray_lena,100)
#picg.imshow(result)
#print result
result = drawAxis(gray_lena,50)
picg.imshow(result)
#print a
