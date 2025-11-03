# Projeto caixa Eletrônico de Banco Virtual
# Funções
# Menu principal

def exibir_menu():
    """Exibir as opções do menu"""
    print("======================================")
    print("              Banco py                ")
    print("======Simulador caixa eletrônico======")
    print("======================================")
    print("Opções disponiveis:                   ")
    print(" 1 - Depositar                        ")
    print(" 2 - Sacar                            ")
    print(" 3 - Ver extrato                      ")
    print(" 4 - Sair                             ")
    print("======================================")


def depositar(saldo_atual, historico_atual):
    """Realizar operação depósito"""
    try:
        valor = float(input("Digite o valor do depósito: R$"))
        if valor > 0:
            saldo_atual + valor
            historico_atual.append(f"Depóstiro: +R$ {valor:.2f}")
            print(f"Depósito de: R$ {valor:.2f}")
        else:
            print("Valor inválido, o depósito deve ser positivo")
    except ValueError:
        print("Erro: por favor digite um valor válido")
    return saldo_atual, historico_atual

def sacar(saldo_atual, historico_atual):
    """Realiza a operação de saque."""
    try:
        valor = float(input("Digite o valor do saque:R$"))
        if valor < 0:
            print("Valor inválido. O saque deve ser positivo")
        elif valor > saldo_atual:
            print("Saldo insuficiente para este saque!")
        else:
            saldo_atual -= valor
            historico_atual.append(f"Saque: - R$ {valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    except ValueError:
        print("Erro: por favor, digite um valor válido")
    return saldo_atual, historico_atual


# Realizar consulta de transação e saldo final
def ver_extrato(saldo_atual, historico_atual):
    print("\n ---- Extrato da conta ----\n")
    if not historico_atual:
        print("Nenhuma transação realizada ainda")
    else:
        for transacao in historico_atual:
            print(transacao)
        # exibir saldo final
        print("==============================")
        print(f"Saldo atual: R${saldo_atual:.2f}")
        print("==============================")


def main():
    saldo = 0.0
    historico = []

    while True:
        exibir_menu()

        opcao = input("Escolha uma opção de 1 a 4:")
        if opcao == "1":
           saldo, historico = depositar(saldo, historico)
        elif opcao == "2":
           saldo, historico = sacar(saldo, historico)
        elif opcao == "3":
            ver_extrato(saldo, historico)
        elif opcao == "4":
             print("Obrigada por usar nossos caixas eletronicos. Até logo!")
             break
        else:
            print("Opção inválida!")
    # Encerramaneto do programa
if __name__ == "__menu__":
 main()
