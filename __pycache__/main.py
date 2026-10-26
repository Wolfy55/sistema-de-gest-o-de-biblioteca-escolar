import livros
import leitores
import emprestimos
import relatorios

op = {
    "1": ("Cadastrar livro", livros.cadastrar_livro),
    "2": ("Listar livros", livros.listar_livros),
    "3": ("Pesquisar livros", livros.pesquisar_livros),
    "4": ("Atualizar quantidade", livros.atualizar_quantidade),
    "5": ("Remover livro", emprestimos.remover_livro_seguro),
    "6": ("Listar categorias", livros.listar_categorias),
    "7": ("Ordenar acervo", livros.ordenar_acervo),
    "8": ("Cadastrar leitor", leitores.cadastrar_leitor),
    "9": ("Listar leitores", leitores.listar_leitores),
    "10": ("Remover leitor", emprestimos.remover_leitor_seguro),
    "11": ("Registrar emprestimo", emprestimos.registrar_emprestimo),
    "12": ("Registrar devolucao", emprestimos.registrar_devolucao),
    "13": ("Relatorio: emprestimos ativos", relatorios.relatorio_emprestimos_ativos),
    "14": ("Relatorio: devolucoes", relatorios.relatorio_devolucoes),
    "15": ("Relatorio: totais do acervo", relatorios.relatorio_totais),
    "16": ("Relatorio: livros mais emprestados", relatorios.relatorio_mais_emprestados),
    "17": ("Relatorio: emprestimos por leitor", relatorios.relatorio_por_leitor),
}


def exibir_menu():
    print("\n=== Biblioteca Escolar ===")
    for numero, (texto, _) in op.items():
        print(f"{numero}. {texto}")
    print("0. Sair")


def main():
    while True:
        exibir_menu()
        escolha = input("Escolha:\n").strip()

        if escolha == "0":
            print("Encerrando...")
            break
        elif escolha in op:
            op[escolha][1]()
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()