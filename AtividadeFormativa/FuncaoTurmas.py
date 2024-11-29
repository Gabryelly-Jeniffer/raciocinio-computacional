
def listar_turma (lista):
    print("===== LISTAR =====")
    for turma in lista:
        print(turma)
    input('Pressione ENTER para continuar\n')

def excluir_turma (lista):
    print("===== EXCLUSÃO =====")
    codigo_para_excluir = int(input("Qual é o codigo que deseja excluir?"))
    for turma in lista:
        if turma["cod_est"] == codigo_para_excluir:
            print("Estamos prontos para remover essa Turma.")
            lista.remove(turma)
            input('Pressione ENTER para continuar\n')


