import sys

def identificar_bandeira(numero_cartao):
    """
    Identifica a bandeira de um cartão de crédito com base no número fornecido.

    Args:
        numero_cartao (str): O número do cartão de crédito a ser verificado.

    Returns:
        str: O nome da bandeira do cartão, ou "Bandeira não identificada" se não for possível identificar.
    """
    numero_cartao = str(numero_cartao)  # Garante que o número do cartão seja uma string

    if numero_cartao.startswith('4'):
        if len(numero_cartao) == 16:
            return "Visa (16 dígitos)"
        elif len(numero_cartao) == 8:
            return "Visa (8 dígitos)"
        else:
            return "Visa (Número de dígitos inválido)"
    elif numero_cartao.startswith(('51', '52', '53', '54', '55')) or (2221 <= int(numero_cartao[:4]) <= 2720):
        return "MasterCard"
    elif numero_cartao.startswith(('4011', '4312', '4389')):
        return "Elo"
    elif numero_cartao.startswith(('34', '37')):
        return "American Express"
    elif numero_cartao.startswith(('6011', '65')) or (644 <= int(numero_cartao[:3]) <= 649):
        return "Discover"
    elif numero_cartao.startswith('6062'):
        return "Hipercard"
    elif numero_cartao.startswith(('36', '38', '39')):
        return "Diners Club"
    elif numero_cartao.startswith(('2014', '2149')):
        return "EnRoute"
    elif numero_cartao.startswith('8699'):
        return "Voyager"
    elif numero_cartao.startswith('50'):
        return "Aura"
    else:
        return "Bandeira não identificada"

if __name__ == "__main__":
    print("Para sair do programa, pressione CTRL+C\n")
    
    while True:
        try:
            numero_cartao = input("Digite o número do cartão de crédito: ")

            if not numero_cartao.isdigit():
                print("Entrada inválida. Por favor, digite apenas números.")
                continue

            bandeira = identificar_bandeira(numero_cartao)
            print(f"Bandeira identificada: {bandeira}\n")

        except KeyboardInterrupt:
            print("\nSaindo do programa.")
            sys.exit()