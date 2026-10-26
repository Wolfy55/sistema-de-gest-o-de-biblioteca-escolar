def ler_inteiro(mensagem, minimo=None):
    while True:
        try:
            numero = int(input(mensagem))
            if minimo is not None and numero < minimo:
                print("O número não pode ser menor que", minimo)
                continue
            return numero
        except ValueError:
            print("O valor não é um número válido")