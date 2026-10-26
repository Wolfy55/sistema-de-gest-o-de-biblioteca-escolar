import utils 

livros = []

def mostrar_livro(livro):
    print("Título:", livro['titulo'])
    print("Código:", livro['codigo'])
    print("Autor:", livro['autor'])
    print("Categoria:", livro['categoria'])
    print("Quantidade:", livro['quantidade'])
    print()

def buscar_livro_por_codigo(codigo):
    for livro in livros:
        if livro['codigo'] == codigo:
            return livro
    return None

def cadastrar_livro():
    codigo = input("Digite o código do livro:\n")
    if buscar_livro_por_codigo(codigo) is not None:
        print("Não foi possível realizar o registro do livro, este livro já existe.")
        return

    titulo = input("Insira o nome do livro:\n")
    autor = input("Insira o autor do livro:\n")
    categoria = input("Digite a categoria do livro:\n")
    quantidade = utils.ler_inteiro("Insira a quantidade de estoque:\n", 0)

    livros.append({
        'codigo': codigo,
        'titulo': titulo,
        'autor': autor,
        'categoria': categoria,
        'quantidade': quantidade,
    })
    print("Livro cadastrado com sucesso")

def listar_livros():
        if not livros:
            print("Não há livros registrados.")
            return
        print("Os livros registrados são:")
        for livro in livros:
            mostrar_livro(livro)

def pesquisar_livros():
    print("Escolha o critério de busca:")
    print("--- 1. Código")
    print("--- 2. Título")
    print("--- 3. Autor")
    print("--- 4. Categoria")
    print("--- 0. Voltar")
    escolha = input("Escolha: ").lower()

    if escolha == "1" or escolha == "codigo":
        encontrado = False
        escolha1 = input("Digite o código do livro:\n")
        for livro in livros:
            if livro['codigo'] == escolha1:
                mostrar_livro(livro)
                encontrado = True
        if not encontrado:
            print(f"O livro de código {escolha1} não foi encontrado.")

    elif escolha == "2" or escolha == "titulo":
        encontrado = False
        escolha1 = input("Digite o título do livro:\n").lower()
        for livro in livros:
            if escolha1 in livro['titulo'].lower():
                mostrar_livro(livro)
                encontrado = True
        if not encontrado:
            print(f"O livro {escolha1} não foi encontrado.")
            
    elif escolha == "3" or escolha == "autor":
        encontrado = False
        escolha1 = input("Digite o autor do livro:\n").lower()
        for livro in livros:
            if escolha1 in livro['autor'].lower():
                mostrar_livro(livro)
                encontrado = True
        if not encontrado:
            print(f"O livro de autor {escolha1} não foi encontrado.")

    elif escolha == "4" or escolha == "categoria":
        encontrado = False
        escolha1 = input("Digite a categoria do livro:\n").lower()
        for livro in livros:
            if escolha1 in livro['categoria'].lower():
                mostrar_livro(livro)
                encontrado = True
        if not encontrado:
            print(f"O livro de categoria {escolha1} não foi encontrado.")

    elif escolha == "0" or escolha == "sair":
        return
    else:
        print("Opção inválida")
        return

def atualizar_quantidade():
    pedidoCodigo = input("Informe o código do livro: ")
    livro = buscar_livro_por_codigo(pedidoCodigo)
    if livro is None:
        print("Livro não existe.")
        return
    novo = utils.ler_inteiro("Nova quantidade:\t", 0)
    livro['quantidade'] = novo
    print("Quantidade atualizada")

def remover_livro():
    pedidoCodigo = input("Informe o código do livro: ")
    livro = buscar_livro_por_codigo(pedidoCodigo)
    if livro is None:
        print("Livro não existe.")
        return
    livros.remove(livro)
    print("Sucesso! O livro foi removido com sucesso!")

def listar_categorias():
    if not livros:
        print("Não há livros.")
        return
    categorias = set()
    for livro in livros:
        categorias.add(livro['categoria'].strip().title())
    print("Categorias existentes:")
    for categoria in sorted(categorias):
        print("-", categoria)

def ordenar_acervo():
    if not livros:
        print("Não há livros.")
        return
    print("--- 1. Título")
    print("--- 2. Autor")
    escolha = input("Escolha: ").strip()
    if escolha == "1":
        chave = 'titulo'
    elif escolha == "2":
        chave = 'autor'
    else:
        print("Opção inválida.")
        return

    livros.sort(key=lambda livro: livro[chave].lower())
    print(f"Acervo ordenado por {chave}:\n")
    for livro in livros:
        mostrar_livro(livro)