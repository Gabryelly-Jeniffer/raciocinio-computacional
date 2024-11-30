
def cadastrar_professor (lista):
    print("===== INCLUSÃO =====")
    codigo = int(input("Por favor, digite o código do professor: "))
    nome = input("Por favor, insira o nome do professor: ")
    cpf = input("Por favorr digite o CPF do professor: ")

    dicionario_professor = {
       "codigo_professor": codigo,
       "nome": nome,
       "cpf": cpf
    }

    lista.append(dicionario_professor)
    input('Pressione ENTER para continuar\n')

def listar_professor (lista):
    print("===== LISTAR =====")
    for professor in lista:
        print(professor)
    input('Pressione ENTER para continuar\n')

def excluir_professor (lista):
    print("===== EXCLUSÃO =====")
    codigo_para_excluir = int(input("Qual é o codigo que deseja excluir?"))
    for professor in lista:
        if professor["codigo_professor"] == codigo_para_excluir:
            print("Estamos prontos para remover esse professor.")
            lista.remove(professor)
            input('Pressione ENTER para continuar\n')


def editar_professor (lista):
    print("===== EDIÇÃO =====")
    codigo_para_editar = int(input("Qual é o codigo que deseja editar?"))
    for professor in lista:
        if professor["codigo_professor"] == codigo_para_editar:
            professor["codigo_professor"] = int(input("Digite o novo código:"))
            professor["nome"] = (input("Digite o novo nome:"))
            professor["cpf"] = (input("Digite o novo CPF:"))
            input('Pressione ENTER para continuar\n')
            break
        else:
            print(f"O codigo {codigo_para_editar} não foi localizado.")


