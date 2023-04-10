#Função que calcula a velocidade média
def calcularVelocidadeMedia(distancia, tempo):
    #calcular a velocidade média
    velocidade_media = distancia/tempo
    #exibir o resultado
    return velocidade_media

#aqui começa o programa principal
distancia = float(input("Informe a distância"))
tempo = float(input("Informe o tempo"))
#chamando a função com valores definidos pelo usuário
print("A velocidade média é {}".format(calcularVelocidadeMedia(distancia, tempo)))

#chamando a função com valores definidos pelo programador
print("A velocidade média é {}".format(calcularVelocidadeMedia(15, 2)))