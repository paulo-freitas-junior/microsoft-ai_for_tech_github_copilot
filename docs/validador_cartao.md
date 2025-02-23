# Validador de Cartão de Crédito

Este script em Python, `validador_cartao.py`, tem como objetivo identificar a bandeira de um cartão de crédito com base no número fornecido pelo usuário. Ele utiliza uma série de verificações nos primeiros dígitos do número do cartão para determinar a qual bandeira ele pertence.

## Funcionalidades

-   **Identificação da Bandeira:** O script analisa o número do cartão de crédito inserido pelo usuário e tenta identificar a bandeira correspondente (Visa, MasterCard, Elo, American Express, Discover, Hipercard, Diners Club, EnRoute, Voyager, Aura).
-   **Validação do Número:** O script verifica se a entrada do usuário contém apenas dígitos numéricos.
-   **Interface Interativa:** O script roda em loop, permitindo que o usuário insira múltiplos números de cartão para identificação, até que o programa seja interrompido manualmente (CTRL+C).
-   **Suporte a Diferentes Comprimentos de Número Visa:** O script consegue identificar cartões Visa de 16 e 8 dígitos.

## Como Usar

1.  Execute o script `validador_cartao.py` em um ambiente Python.
2.  O script solicitará que você digite o número do cartão de crédito.
3.  Após a inserção do número, o script exibirá a bandeira identificada.
4.  Para sair do programa, pressione `CTRL+C`.

## Lógica de Identificação

O script utiliza a função `identificar_bandeira(numero_cartao)` para determinar a bandeira do cartão. Esta função implementa a seguinte lógica:

-   Verifica os primeiros dígitos do número do cartão para determinar a possível bandeira.
-   Utiliza estruturas condicionais (`if`, `elif`, `else`) para comparar os prefixos do número do cartão com os padrões conhecidos de cada bandeira.
-   Retorna o nome da bandeira correspondente ou "Bandeira não identificada" caso não encontre uma correspondência.

## Bandeiras Suportadas

As seguintes bandeiras são suportadas pelo script:

-   Visa (16 dígitos e 8 dígitos)
-   MasterCard
-   Elo
-   American Express
-   Discover
-   Hipercard
-   Diners Club
-   EnRoute
-   Voyager
-   Aura

