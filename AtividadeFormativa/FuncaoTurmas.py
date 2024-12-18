#Aluna: Gabryelly Jeniffer
#Disciplia: Raciociono Computacional

def listar_turma (lista):
    print("===== LISTAR =====")
    for turma in lista:
        print(turma)
    input('Pressione ENTER para continuar\n')


def criar_turma (lista, professores, disciplinas):

    print("===== INCLUSÃO =====")
    turma = int(input("Por favor, digite o código da turma: "))
    professor = int(input("Por favor, digite o código do professor: "))
    disciplina = int(input("Por favor, digite o código da disciplina: "))

    if procurar_item(professor,"codigo_professor",professores) == None:
        print("Professor nao cadastrado")
        return

    if procurar_item(turma, "codigo_turma", lista) !=None:
        print("Turma já cadastrada!")
        return

    if procurar_item(disciplina, "codigo_disciplina", disciplinas) == None:
        print("Disciplina nao cadastrada")
        return

    dicionario_turma = {
        "codigo_turma": turma,
        "codigo_professor": professor,
        "codigo_disciplina": disciplina
    }

    lista.append(dicionario_turma)
    input('Pressione ENTER para continuar\n')


def procurar_item(item, item_procura, lista_informacoes):
    """
    Procura um item em uma lista de informacoes.

    Args:
        item matricula (int): O item a ser procurado.
        item_procura (str): O nome da chave do dicionario que sera usada para a busca.
        lista_informacoes (list): A lista de informacoes que sera procurada.

    Returns:
        dict: O dicionario que contem o item procurado, caso ele seja encontrado.
    """
    for resultado in lista_informacoes:
        if resultado[item_procura] == item:
            return resultado


def editar_turma(turmas, professores, disciplinas):
    print("===== EDIÇÃO =====")
    codigo_turma = int(input("Qual é o codigo que deseja alterar?"))
    for turma in turmas:
        if turma["codigo_turma"] == codigo_turma:

            cod_turma= int(input("Por favor, digite o código da turma: "))
            professor = int(input("Por favor, digite o código do profesor: "))
            disciplina = int(input("Por favor, digite o código da disciplina: "))

            if procurar_item(professor,"codigo_professor",professores) == None:
                print("Professor nao cadastrado")
                return
            if procurar_item(cod_turma, "codigo_turma", turmas) != None:
                print("Turma nao cadastrada")
                return
            if procurar_item(disciplina, "codigo_disciplina", disciplinas) == None:
                print("Codigo da disciplina já cadastrada!")
                return

            turma["codigo_turma"] = (cod_turma)
            turma["codigo_professor"] = professor
            turma["codigo_disciplina"] = disciplina
            break
    input('Pressione ENTER para continuar\n')
