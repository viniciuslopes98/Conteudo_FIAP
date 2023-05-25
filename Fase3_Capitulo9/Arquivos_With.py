#o with usará o open para abrir o arquivo indicado, dentro do objeto arquivo e fará sozinho o encerramento do acesso quando a última linha de código dentro dele for executada
with open("c:\arquivos\arquivo_de_texto.txt", "r") as arquivo:
    #aqui devemos escrever todos os códigos que usam o arquivo aberto, pois após a última linha de código dentro dessa estrutura, o arquivo será automaticamente encerrado
    print(arquivo.read())