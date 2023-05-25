import json

arquivo = open("c:\\Users\\Vinicius\\Desktop\\arquivojson.txt", "r", encoding="utf-8")
conteudo = arquivo.read()
arquivo.close()
#Função que converte JSON de string para dicionario
agenda = json.loads(conteudo)
print(type(agenda))

