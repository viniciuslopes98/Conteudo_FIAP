print("Esse programa inverte os conteúdos de duas variáveis")
A = input("Digite o conteúdo da variável 1: ")
B = input("Digite o conteúdo da variável 2: ")
troca = A
A = B
B = troca
print("Agora que trocamos, a variável A contém {} e a variável B contém {}".format(A, B))