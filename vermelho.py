import cv2
from matplotlib import pyplot

def mostrar_imagem(imagem):
    imagem = cv2.cvtColor(imagem, cv2.COLOR_RGB2BGR)
    pyplot.imshow(imagem)
    pyplot.show()
    
def alt_cor_vermelho(imagem):
    imagem = cv2.cvtColor(imagem, cv2.COLOR_RGB2BGR)
    altura, largura, canais = imagem.shape
    for y in range(0,altura): # percore a linha, percorre linha por linha
        for x in range (0,largura): #percorre a coluna, percorre coluna por coluna
            imagem.itemset((y,x,2),255) #Cor vermelha
         
    cv2.imwrite("img/vermelho.png",imagem)
    mostrar_imagem(imagem)