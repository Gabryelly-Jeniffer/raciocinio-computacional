
def cadastrar_estudante (lista):
    print("===== INCLUSÃO =====")
    codigo = int(input("Por favor, digite o código do estudante: "))
    nome = input("Por favor, insira o nome do estudante: ")
    cpf = input("Por favorr digite o CPF do estudante: ")

    dicionario_estudantes = {
       "cod_est": codigo,
       "nome": nome,
       "cpf": cpf
    }

    lista.append(dicionario_estudantes)
    input('Pressione ENTER para continuar\n')

def listar_estudantes (lista):
    print("===== LISTAR =====")
    for estudante in lista:
        print(estudante)
    input('Pressione ENTER para continuar\n')

def excluir_estudante (lista):
    print("===== EXCLUSÃO =====")
    codigo_para_excluir = int(input("Qual é o codigo que deseja excluir?"))
    for estudante in lista:
        if estudante["cod_est"] == codigo_para_excluir:
            print("Estamos prontos para remover esse estudante.")
            lista.remove(estudante)
            input('Pressione ENTER para continuar\n')


def editar_estudante (lista):
    print("===== EDIÇÃO =====")
    codigo_para_editar = int(input("Qual é o codigo que deseja editar?"))
    for estudante in lista:
        if estudante["cod_est"] == codigo_para_editar:
            estudante["cod_est"] = int(input("Digite o novo código:"))
            estudante["nome"] = (input("Digite o novo nome:"))
            estudante["cpf"] = (input("Digite o novo CPF:"))
            input('Pressione ENTER para continuar\n')
            break
        else:
            print(f"O codigo {codigo_para_editar} não foi localizado.")


