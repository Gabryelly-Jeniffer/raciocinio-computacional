#Aluna: Gabryelly Jeniffer
#Disciplia: Raciociono Computacional

def cadastrar_disciplina (lista):
    print("===== INCLUSÃO =====")
    codigo = int(input("Por favor, digite o código da disciplina: "))
    nome = input("Por favor, insira o nome da disciplina: ")

    dicionario_disciplina = {
       "codigo_disciplina": codigo,
       "nome": nome,
    }

    lista.append(dicionario_disciplina)
    input('Pressione ENTER para continuar\n')

def listar_disciplina (lista):
    print("===== LISTAR =====")
    for disciplina in lista:
        print(disciplina)
    input('Pressione ENTER para continuar\n')


def editar_disciplina (lista):
    print("===== EDIÇÃO =====")
    codigo_para_editar = int(input("Qual é o codigo que deseja editar?"))
    for disciplina in lista:
        if disciplina["codigo_disciplina"] == codigo_para_editar:
            disciplina["codigo_disciplina"] = int(input("Digite o novo código:"))
            disciplina["nome"] = (input("Digite o novo nome:"))
            input('Pressione ENTER para continuar\n')
            break
        else:
            print(f"O codigo {codigo_para_editar} não foi localizado.")


