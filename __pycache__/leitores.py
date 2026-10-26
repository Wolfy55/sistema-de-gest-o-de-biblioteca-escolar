leitores = []

def mostrar_leitor(leitor):
    print("Identificador:", leitor['id'])
    print("Nome:", leitor['nome'])
    print("Turma/setor:", leitor['turma'])
    print()

def buscar_leitor_por_id(identificador):
    for leitor in leitores:
        if leitor['id'] == identificador:
            return leitor
        return None

def cadastrar_leitor():
    identificador = input("Digite o leitor:\n").strip()
    if buscar_leitor_por_id(identificador) is not None:
        print("Não foi possível cadastrar, este identificador já existe.")
        return
    nome = input("Digite o nome do leitor:\n")
    turma = input("Digite a turma ou setor:\n")

    leitores.append({'id': identificador, 'nome': nome, 'turma': turma})
    print("Leitor cadastrado com sucesso.")

def listar_leitores():
    if not leitores:
        print("Não há leitores registrados.")
        return
    print("Os leitores registrados são:\n")
    for leitor in leitores:
        mostrar_leitor(leitor)
        