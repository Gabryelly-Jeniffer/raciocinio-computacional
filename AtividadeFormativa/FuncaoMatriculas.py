#Aluna: Gabryelly Jeniffer
#Disciplia: Raciociono Computacional


def listar_matricula(lista):
    print("===== LISTAR =====")
    for matricula in lista:
        print(matricula)
    input('Pressione ENTER para continuar\n')


"""
Cria uma matricula em uma turma.

Args:
    lista (list): A lista que sera adicionada a matricula.
    estudantes (list): A lista de estudantes cadastrados.
    turmas (list): A lista de turmas cadastradas.

Returns:
    None
"""
def criar_matricula (lista, estudantes, turmas):

    print("===== INCLUSÃO =====")
    matricula = int(input("Por favor, digite o código da Matricula: "))
    turma = int(input("Por favor, digite o código da Turma: "))
    estudante = int(input("Por favor, digite o código da Estudante: "))

    if procurar_item(estudante,"codigo_estudante",estudantes) == None:
        print("Estudante nao cadastrado")
        return
    if procurar_item(turma, "codigo_turma", turmas) == None:
        print("Turma nao cadastrada")
        return

    if procurar_item(matricula, "codigo_matricula", lista) !=None:
        print("Matricula já cadastrada!")
        return

    dicionario_matricula = {
        "codigo_matricula": matricula,
        "codigo_turma": turma,
        "codigo_estudante": estudante
    }

    lista.append(dicionario_matricula)
    input('Pressione ENTER para continuar\n')


def editar_matricula (lista, estudantes, turmas):
    print("===== EDIÇÃO =====")
    codigo_matricula = int(input("Qual é o codigo que deseja alterar?"))
    for matricula in lista:
        if matricula["codigo_matricula"] == codigo_matricula:

            cod_matricula = int(input("Por favor, digite o código da Matricula: "))
            turma = int(input("Por favor, digite o código da Turma: "))
            estudante = int(input("Por favor, digite o código da Estudante: "))

            if procurar_item(estudante,"codigo_estudante",estudantes) == None:
                print("Estudante nao cadastrado")
                return
            if procurar_item(turma, "codigo_turma", turmas) == None:
                print("Turma nao cadastrada")
                return
            if procurar_item(cod_matricula, "codigo_matricula", lista) != None:
                print("Codigo da Matricula já cadastrada!")
                return

            matricula["codigo_matricula"] = (cod_matricula)
            matricula["codigo_turma"] = turma
            matricula["codigo_estudante"] = estudante
            break
    input('Pressione ENTER para continuar\n')


def procurar_item(item, item_procura, lista_informacoes):
    """
    Procura um item em uma lista de informacoes.

    Args:
        item (int): O item a ser procurado.
        item_procura (str): O nome da chave do dicionario que sera usada para a busca.
        lista_informacoes (list): A lista de informacoes que sera procurada.

    Returns:
        dict: O dicionario que contem o item procurado, caso ele seja encontrado.
    """
    for resultado in lista_informacoes:
        if resultado[item_procura] == item:
            return resultado



