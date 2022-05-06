import cv2
import numpy

from Azul import alt_cor
from Verde import alt_cor_verde
from vermelho import alt_cor_vermelho

from matplotlib import pyplot




#Mostra a Imagem Original
def mostrar_imagem(imagem):
    #Converterndo para RGB
    imagem = cv2.cvtColor(imagem, cv2.COLOR_RGB2BGR)
    pyplot.imshow(imagem)
    pyplot.show()

#exibir o valor de cada pix
def exibir_valor_pixel(imagem):
    altura, largura, canais = imagem.shape
    for y in range(0, altura):
        for x in range(0, largura):
            # Imprime todos os valores dos pixels com valores de cada cor
            print("linha = {} <> coluna = {} === {}".format(y, x, imagem[y][x]))

#Recorta a Imagem
def img_corte(imagem):    
    imagem = imagem[0:62, 55:140]
    mostrar_imagem(imagem)
    cv2.imwrite("img/modificada.png",imagem)

#função principal
def main():
    imge22 = cv2.imread("img/py.png")
    #Exibe a dimensão da imagem
    altura, largura, canais = imge22.shape
    print("\nAltura da Imagem = {}\nLargura da Imagem = {}\n".format(altura, largura))
    #Mostra a imagem original
    mostrar_imagem(imge22)
    #Exibe o valor de cada pixel da imagem
    exibir_valor_pixel(imge22)
    #Alterar para cor azul
    alt_cor(imge22) #azul
    #Alterar para cor verde
    alt_cor_verde(imge22) #verde
    #Alterar para cor vermelho
    alt_cor_vermelho(imge22) #vermelho"
    #Imagem recortada
    img_corte(imge22)


main()