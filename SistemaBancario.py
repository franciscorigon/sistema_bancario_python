import textwrap

def menu ():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):


def sacar(*, saldo, valor, extrato, limite, numero_saques):


def exibir_extrato(saldo, /, *, extrato):


def criar_usuario(usuarios):


def filtrar_usuario(cpf, usuarios):


def criar_conta(agencia, numero_conta, usuarios):


def listar_contas(contas):



def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
        
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato = extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":


        elif opcao == "q":
            break

        else:
            print("Opção inválida, por favor selecione a opção desejada: ")