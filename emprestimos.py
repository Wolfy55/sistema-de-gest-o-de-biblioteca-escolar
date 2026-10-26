import livros
import leitores

emprestimos = []

def buscar_emprestimo_ativo(codigo_livro, id_leitor):
    for emp in emprestimos:
        if (emp['codigo_livro'] == codigo_livro
                and emp['id_leitor'] == id_leitor
                and emp['ativo']):
            return emp
        return None

def registrar_emprestimo():
    codigo = input("Código do livro:\n").strip()
    livro = livros.buscar_livro_por_codigo(codigo)
    if livro is None:
        print("Livro não existe.")
        return

    id_leitor = input("Identificador do leitor\n").strip()
    leitor = leitores.buscar_leitor_por_id(id_leitor)
    if leitor is None:
        print("Leitor não existe.")
        return

    if livro['quantidade'] <= 0:
        print("Não há exemplares disponíveis deste livro.")
        return

    emprestimos.append({'codigo_livro': codigo, 'id_leitor': id_leitor, 'ativo': True})
    livro['quantidade'] -= 1
    print(f"Empréstimo registrado: '{livro['titulo']}' para {leitor['nome']}.")
 
 
def registrar_devolucao():
    codigo = input("Código do livro:\n").strip()
    id_leitor = input("Identificador do leitor:\n").strip()
 
    emprestimo = buscar_emprestimo_ativo(codigo, id_leitor)
    if emprestimo is None:
        print("Não existe empréstimo ativo deste livro para este leitor.")
        return
 
    emprestimo['ativo'] = False
    livro = livros.buscar_livro_por_codigo(codigo)
    if livro is not None:
        livro['quantidade'] += 1
    print("Devolução registrada com sucesso.")
 
 
def livro_tem_emprestimo_ativo(codigo):
    for emp in emprestimos:
        if emp['codigo_livro'] == codigo and emp['ativo']:
            return True
    return False
 
 
def leitor_tem_emprestimo_ativo(id_leitor):
    for emp in emprestimos:
        if emp['id_leitor'] == id_leitor and emp['ativo']:
            return True
    return False
 
 
def remover_livro_seguro():
    codigo = input("Informe o código do livro: ").strip()
    livro = livros.buscar_livro_por_codigo(codigo)
    if livro is None:
        print("Livro não existe.")
        return
    if livro_tem_emprestimo_ativo(codigo):
        print("Não é possível remover: há empréstimo ativo deste livro.")
        return
    livros.livros.remove(livro)
    print("Livro removido com sucesso!")
 
 
def remover_leitor_seguro():
    id_leitor = input("Informe o identificador do leitor: ").strip()
    leitor = leitores.buscar_leitor_por_id(id_leitor)
    if leitor is None:
        print("Leitor não existe.")
        return
    if leitor_tem_emprestimo_ativo(id_leitor):
        print("Não é possível remover: o leitor tem empréstimo ativo.")
        return
    leitores.leitores.remove(leitor)
    print("Leitor removido com sucesso!")
