contatos = {
    "Clark Kent":{
        "celular":"123456",
        "email":"clark@krypton.com"
    },
    "Bruce Wayne":{
        "celular":"654321",
        "email":"bat@caverna.com"
    }
}
for nome, formas_contato in contatos.items():
    print("O contato {}".format(nome))
    for forma, valor in formas_contato.items():
        print("pode ser contatado pelo seu {} através do {}"
              .format(forma,valor))
    print("\n\n")
