
def cadastrar_disciplina (lista):
    print("===== INCLUSÃO =====")
    codigo = int(input("Por favor, digite o código da disciplina: "))
    nome = input("Por favor, insira o nome da disciplina: ")

    dicionario_disciplina = {
       "cod_est": codigo,
       "nome": nome,
    }

    lista.append(dicionario_disciplina)
    input('Pressione ENTER para continuar\n')

def listar_disciplina (lista):
    print("===== LISTAR =====")
    for disciplina in lista:
        print(disciplina)
    input('Pressione ENTER para continuar\n')

def excluir_disciplina (lista):
    print("===== EXCLUSÃO =====")
    codigo_para_excluir = int(input("Qual é o codigo que deseja excluir?"))
    for disciplina in lista:
        if disciplina["cod_est"] == codigo_para_excluir:
            print("Estamos prontos para remover essa disciplina.")
            lista.remove(disciplina)
            input('Pressione ENTER para continuar\n')


def editar_disciplina (lista):
    print("===== EDIÇÃO =====")
    codigo_para_editar = int(input("Qual é o codigo que deseja editar?"))
    for disciplina in lista:
        if disciplina["cod_est"] == codigo_para_editar:
            disciplina["cod_est"] = int(input("Digite o novo código:"))
            disciplina["nome"] = (input("Digite o novo nome:"))
            input('Pressione ENTER para continuar\n')
            break
        else:
            print(f"O codigo {codigo_para_editar} não foi localizado.")


