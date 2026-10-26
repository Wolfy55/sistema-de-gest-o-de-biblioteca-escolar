import livros
import leitores
import emprestimos


def titulo_do_livro(codigo):
    livro = livros.buscar_livro_por_codigo(codigo)
    if livro is None:
        return f"(livro {codigo} removido)"
    return livro['titulo']


def nome_do_leitor(id_leitor):
    leitor = leitores.buscar_leitor_por_id(id_leitor)
    if leitor is None:
        return f"(leitor {id_leitor} removido)"
    return leitor['nome']


def relatorio_emprestimos_ativos():
    encontrou = False
    print("Empréstimos ativos (livros ainda não devolvidos):")
    for emp in emprestimos.emprestimos:
        if emp['ativo']:
            print("-", titulo_do_livro(emp['codigo_livro']),
                "| leitor:", nome_do_leitor(emp['id_leitor']))
            encontrou = True
    if not encontrou:
        print("Nenhum empréstimo ativo.")


def relatorio_devolucoes():
    encontrou = False
    print("Devoluções registradas:")
    for emp in emprestimos.emprestimos:
        if not emp['ativo']:
            print("-", titulo_do_livro(emp['codigo_livro']),
                "| leitor:", nome_do_leitor(emp['id_leitor']))
            encontrou = True
    if not encontrou:
        print("Nenhuma devolução registrada.")


def relatorio_totais():
    total_titulos = len(livros.livros)
    disponiveis = 0
    for livro in livros.livros:
        disponiveis += livro['quantidade']
    emprestados = 0
    for emp in emprestimos.emprestimos:
        if emp['ativo']:
            emprestados += 1

    print("Resumo do acervo:")
    print("Livros cadastrados (títulos):", total_titulos)
    print("Exemplares disponíveis:", disponiveis)
    print("Exemplares emprestados agora:", emprestados)


def relatorio_mais_emprestados():
    if not emprestimos.emprestimos:
        print("Ainda não há empréstimos.")
        return

    contagem = {}
    for emp in emprestimos.emprestimos:
        codigo = emp['codigo_livro']
        contagem[codigo] = contagem.get(codigo, 0) + 1

    ranking = sorted(contagem.items(), key=lambda item: item[1], reverse=True)
    print("Livros mais emprestados:")
    for codigo, quantidade in ranking:
        print("-", titulo_do_livro(codigo), ":", quantidade, "empréstimo(s)")


def relatorio_por_leitor():
    id_leitor = input("Identificador do leitor:\n").strip()
    if leitores.buscar_leitor_por_id(id_leitor) is None:
        print("Leitor não existe.")
        return

    encontrou = False
    print("Empréstimos de", nome_do_leitor(id_leitor) + ":")
    for emp in emprestimos.emprestimos:
        if emp['id_leitor'] == id_leitor:
            situacao = "ativo" if emp['ativo'] else "devolvido"
            print("-", titulo_do_livro(emp['codigo_livro']), "|", situacao)
            encontrou = True
    if not encontrou:
        print("Este leitor ainda não fez empréstimos.")