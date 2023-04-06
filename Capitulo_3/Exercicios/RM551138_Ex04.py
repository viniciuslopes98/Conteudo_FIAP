# Recebe o valor atual de minutos da máquina
minutos = int(input("Digite os minutos atuais: "))

# Calcula o fatorial
fatorial = 1
for i in range(1, minutos+1):
    fatorial *= i

# Exibe a senha
senha = "LIBERDADE" + str(fatorial)
print("Senha: ", senha)
