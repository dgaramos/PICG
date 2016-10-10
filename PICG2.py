import PICG1 as picg


a = (picg.imread("len_std.jpg"))

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
    print i0
    print i1
    if ( j0 < j1 ) :
        for y in range(j0,j1):
            #print 'asdasd'   
            newImg = drawPoint(newImg,i1,y,cor)
        for y in range (j0,j1):
            newImg = drawPoint(newImg,i0,y,cor)
            
    if (i0 < i1 ):
        print "Entrou"
        for x in range(i0,i1):
            newImg = drawPoint(newImg,x,i1,cor)
            newImg = drawPoint(newImg,x,i0,cor)
            
    return newImg

result = a

#Terceira questao usa DDA
#print (drawRect(a,0,0,10,10,[1,100,50],1))
#picg.imshow(result)
#print a
result = (drawRect(a,100,50,200,200,[100,50,200],1))
picg.imshow(result)
#print a
