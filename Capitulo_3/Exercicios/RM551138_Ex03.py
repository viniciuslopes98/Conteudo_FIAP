# Inicialização das variáveis
soma_impar = 0
soma_par = 0
contador_impar = 0
contador_par = 0

# Laço para receber as notas dos alunos ímpares
for i in range(1, 50, 2):
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES.")
    print(f"POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {i}.")
    nota = float(input())
    soma_impar += nota
    contador_impar += 1

# Laço para receber as notas dos alunos pares
for i in range(2, 51, 2):
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES.")
    print(f"POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {i}.")
    nota = float(input())
    soma_par += nota
    contador_par += 1

# Cálculo da média de cada metade da sala
media_impar = soma_impar / contador_impar
media_par = soma_par / contador_par

# Exibição das médias e da metade com a maior nota
if media_impar > media_par:
    print(f"A média dos alunos ímpares é {media_impar:.2f} e é maior do que a média dos alunos pares ({media_par:.2f}).")
else:
    print(f"A média dos alunos pares é {media_par:.2f} e é maior do que a média dos alunos ímpares ({media_impar:.2f}).")

