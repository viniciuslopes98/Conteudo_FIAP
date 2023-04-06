# Captura a quantidade de votos para cada dia da semana
votos_segunda = int(input("Digite a quantidade de votos para segunda-feira: "))
votos_terca = int(input("Digite a quantidade de votos para terça-feira: "))
votos_quarta = int(input("Digite a quantidade de votos para quarta-feira: "))
votos_quinta = int(input("Digite a quantidade de votos para quinta-feira: "))
votos_sexta = int(input("Digite a quantidade de votos para sexta-feira: "))

# Verifica qual dia teve mais votos
mais_votado = "segunda-feira"
if votos_terca > votos_segunda and votos_terca > votos_quarta and votos_terca > votos_quinta and votos_terca > votos_sexta:
    mais_votado = "terça-feira"
elif votos_quarta > votos_segunda and votos_quarta > votos_terca and votos_quarta > votos_quinta and votos_quarta > votos_sexta:
    mais_votado = "quarta-feira"
elif votos_quinta > votos_segunda and votos_quinta > votos_terca and votos_quinta > votos_quarta and votos_quinta > votos_sexta:
    mais_votado = "quinta-feira"
elif votos_sexta > votos_segunda and votos_sexta > votos_terca and votos_sexta > votos_quarta and votos_sexta > votos_quinta:
    mais_votado = "sexta-feira"
else:
    mais_votado = "Houve um empate, uma nova votação será feita!"

# Exibe o resultado
print("Resultado: ", mais_votado)
