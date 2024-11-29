lista_estudantes = []
#para incluir:
# O usuario navegou pelas opções Estudantes -> Incluir até chegar no código abaixo.
for i in range(3):
    codigo = int(input("Por favor, digite o código: "))
    nome = input("Por favor, insira o nome do estudante: ")
    cpf = input("Por favorr digite o CPF: ")

    dicionario_estudantes = {
        "cod_est": codigo,
        "nome": nome,
        "cpf": cpf
    }

    lista_estudantes.append(dicionario_estudantes)

for estudante in lista_estudantes:
    print(estudante)

#para excluir:
codigo_para_excluir = int(input("Qual é o codigo que deseja exclui?"))
for dicionario_estudantes in lista_estudantes:
    if lista_estudantes["codigo"] == codigo_para_excluir:
        print("Estamos prontos para remover esse esdutante.")


# para editar informações:

codigo_para_editar = int(input("Qual é o codigo que deseja editar?"))

estudante_para_ser_modificado = None
for dicionario_estudantes in lista_estudantes:
    if dicionario_estudantes["codigo"] == codigo_para_editar:
        estudante_para_ser_modificado = dicionario_estudantes
        break

if estudante_para_ser_modificado is None:
    print(f"O codigo {codigo_para_editar} não foi localizado.")
else:
    estudante_para_ser_modificado ["codigo"] = int(input("Digite o novo código:"))
    estudante_para_ser_modificado ["nome"] = (input("Digite o novo nome:"))
    estudante_para_ser_modificado ["cpf"] = (input("Digite o novo CPF:"))

for estudante in lista_estudantes:
    print(estudante)

