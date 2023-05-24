dicionario = {"Zeldrys":"Bronze",
              "Bruno":"Prata",
              "M1hawk":"Ouro",
              "Sati":"Ouro",
              "Ornot":"Latão"}

#Exibe as chaves presentes no dicionario.
print("Nicknames")
for keys in dicionario.keys():
   print(keys)
print()
#Exibe os valores presentes no dicionario.
print("Elos")
for value in dicionario.values():
   print(value)
print()
#Exibe chave e valor juntos
print("Nicknames -- Elos")
for chave, valor in dicionario.items():
    print("{} -- {}".format(chave, valor))
print()
#Adicionando chave e valor ao dicionario
dicionario["Mugetsu"] = "Prata"
print()

#Atualizando valor da chave
dicionario["Zeldrys"]= "Latão"

#Removendo iten pela chave
dicionario.pop("Sati")

#Pedindo ao usuário para inserir valores
elo=input("Informe o elo do jogador")
nickname=input("Informe o nickname do jogador")
dicionario[elo] = nickname

#Removendo o ultimo da lista
dicionario.popitem()

#exibindo o dicionario com os valores adicionados
for chave, valor in dicionario.items():
    print("{} -- {}".format(chave, valor))