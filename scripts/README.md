## Projeto: Criando um validador de bandeiras de cartões de crédito - GitHub Copilot
### Inserindo o número do cartão de crédito, identificar e validar qual a bandeira do cartão.
---

#### 1. Regras de validação das bandeiras

| Bandeira            | Número Inicial                                                                 |
| ------------------- | ------------------------------------------------------------------------------ |
| Visa                | Começa sempre como o número 4 (16 dígitos)                                     |
| MasterCard          | Começa com dígitos entre 51 e 55 ou entre 2221 e 2720                          |
| Elo                 | Pode começar com vários intervalos como 4011, 4312, 4389 entre outros          |
| American Express    | Inicia com 34 ou 37                                                            |
| Discover            | Começa com 6011, 65 ou com a faixa de 644 a 649                                |
| Hipercard           | Geralmente começa com 6062                                                     |

Baseando-se nos dados da tabela acima, foi solicitado ao Copilot inserir os dados das seguintes bandeiras: Diners Club,EnRoute, Voyager e Aura através do seguinte prompt no Copilot Chat:

```
Baseando-se no exemplo selecionado, complete as informações da tabela inserindo as seguintes bandeiras: 
Visa 16 dígitos, Diners Club, EnRoute, Voyager, Aura. Complete os dados em português pt-br.
```
| Bandeira            | Número Inicial                                                                 |
| ------------------- | ------------------------------------------------------------------------------ |
| Visa 16             | Começa sempre com o número 4 (16 dígitos)                                      |
| Visa 8              | Começa sempre com o número 4 (8 dígitos                                        |
| MasterCard          | Começa com dígitos entre 51 e 55 ou entre 2221 e 2720                          |
| Elo                 | Pode começar com vários intervalos como 4011, 4312, 4389 entre outros          |
| American Express    | Inicia com 34 ou 37                                                            |
| Discover            | Começa com 6011, 65 ou com a faixa de 644 a 649                                |
| Hipercard           | Geralmente começa com 6062                                                     |
| Diners Club         | Começa com 36, 38 ou 39                                                        |
| EnRoute             | Começa com 2014 ou 2149                                                        |
| Voyager             | Começa com 8699                                                                |
| Aura                | Começa com 50                                                                  |

Feita a verificação, pude constatar que o Copilot identificou que ambos os Visas de 8 e 16 dígitos iniciam da mesma forma.
Fiz a verificação dos dados usando o site 4Devs.com.br ![](https://www.4devs.com.br/gerador_de_numero_cartao_credito)

#### 2. Criação da função em Python
- A linguagem escolhida para desenvolver a função de validação foi Python, pois é a linguagem que possuo maior familiaridade.

O comando solicitado ao Copilot:
```
Baseando-se na tabela gerada, preciso que você crie uma função em Python que seja capaz de receber um número de cartão de crédito e identificar e validar qual a bandeira correspondente. 
Somente poderá receber dados numéricos e caso o usuário queira parar a execução, que pressione as teclas CTRL+C para parar a execução. 
Crie usando a língua em português pt-br.
```

- O código Python desse projeto encontra-se na pasta SCRIPTS ![](scripts/validador_cartao.py)
- A documentação do código pode ser acessada na pasta DOCS ![]()