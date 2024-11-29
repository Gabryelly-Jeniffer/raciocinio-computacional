

def listar_matricula(lista):
    print("===== LISTAR =====")
    for matricula in lista:
        print(matricula)
    input('Pressione ENTER para continuar\n')

def excluir_matricula (lista):
    print("===== EXCLUSÃO =====")
    codigo_para_excluir = int(input("Qual é o codigo que deseja excluir?"))
    for matricula in lista:
        if matricula["cod_est"] == codigo_para_excluir:
            print("Estamos prontos para remover essa Matricula.")
            lista.remove(matricula)
            input('Pressione ENTER para continuar\n')
            return

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

    dicionario_matricula = {
        "codigo_matricula": matricula,
        "codigo_turma": turma,
        "codigo_estudante": estudante
    }

    lista.append(dicionario_matricula)
    input('Pressione ENTER para continuar\n')



"""
Procura um item em uma lista de informacoes.

Args:
    item (int): O item a ser procurado.
    item_procura (str): O nome da chave do dicionario que sera usada para a busca.
    lista_informacoes (list): A lista de informacoes que sera procurada.

Returns:
    dict: O dicionario que contem o item procurado, caso ele seja encontrado.
"""
def procurar_item(item, item_procura, lista_informacoes):
    for resultado in lista_informacoes:
        if resultado[item_procura] == item:
            return resultado
