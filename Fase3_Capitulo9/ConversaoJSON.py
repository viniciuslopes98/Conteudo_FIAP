import json

contatos = {
    "Clark Kent":{
       "Celular":"123456",
       "Email":"super@krypton.com"
    },
    "Bruce Wayne":{
       "Celular":"654321",
       "Email":"bat@caverna.com.br"
    }
 }
#Função para converter o código em JSON
#print(json.dumps(contatos, indent=4))

arquivojson = open("c:\\Users\\Vinicius\\Desktop\\arquivojson.txt", "w", encoding="UTF-8")
conteudo = json.dumps(contatos, indent=4)
arquivojson.write(conteudo)
arquivojson.close()