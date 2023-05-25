arquivo = open("c:\\Users\\Vinicius\\Desktop\\Arquivo-teste.txt", encoding="UTF-8")

#Leitura de uma linha do arquivo
print(arquivo.readline())

for linha in arquivo.readlines():
    print(linha)

#Fechando a função
    arquivo.close()

conteudo = "Bora testar essa função!!"

#Declarando o diretório e o tipo do novo arquivo.
novo_arquivo = open("c:\\Users\\Vinicius\\Desktop\\arquivo-text.txt", "w", encoding="UTF-8")

#Função que vai criar o arquivo
novo_arquivo.write(conteudo)

novo_arquivo.close()