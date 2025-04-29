# Classe que guarda os dados de uma conta no banco
class ContaBancaria:
    def __init__(self, nome, cpf, numero_conta, agencia="0001", saldo=0.0):
        # Cria uma conta nova
        self.nome = nome            # Nome do dono da conta
        self.cpf = cpf              # CPF do dono
        self.numero_conta = numero_conta  # Número da conta
        self.agencia = agencia      # Agência do banco (sempre 0001)
        self.saldo = saldo          # Quanto dinheiro tem na conta
        self.historico = []         # Lista de tudo que aconteceu na conta

# Função para colocar dinheiro na conta
def depositar(conta, valor):
    if valor > 0:  # Só aceita valores maiores que zero
        conta.saldo += valor
        conta.historico.append(f"Depósito: R$ {valor:.2f}")
        print("Depósito feito com sucesso!")
    else:
        print("Valor não pode ser zero ou negativo!")

# Função para tirar dinheiro da conta
def sacar(conta, valor):
    if valor > 0 and valor <= conta.saldo:  # Verifica se tem dinheiro suficiente
        conta.saldo -= valor
        conta.historico.append(f"Saque: R$ {valor:.2f}")
        print("Saque feito com sucesso!")
    else:
        print("Sem saldo suficiente ou valor inválido!")

# Função para mostrar o extrato da conta
def extrato(conta):
    print("\n--- Extrato da Conta ---")
    print(f"Nome: {conta.nome}")
    print(f"CPF: {conta.cpf}")
    print(f"Conta: {conta.numero_conta} | Agência: {conta.agencia}")
    print(f"Saldo: R$ {conta.saldo:.2f}")
    print("\nHistórico:")
    if not conta.historico:
        print("- Nada aconteceu ainda.")
    else:
        for item in conta.historico:
            print(f"- {item}")

# Função para cadastrar um cliente novo
def cadastrar_usuario(clientes, nome, cpf):
    if cpf in clientes:  # Verifica se o CPF já existe
        print("Erro: Este CPF já está cadastrado!")
        return False
    clientes[cpf] = {"nome": nome}  # Guarda o nome do cliente
    print(f"Cliente {nome} cadastrado!")
    return True

# Função para criar uma conta nova para um cliente
def cadastrar_conta_bancaria(clientes, contas, cpf, numero_conta):
    if cpf not in clientes:  # Verifica se o CPF existe
        print("Erro: CPF não encontrado!")
        return False
    if cpf in contas:  # Verifica se o CPF já tem conta
        print("Erro: Este CPF já tem uma conta!")
        return False
    nome = clientes[cpf]["nome"]
    conta = ContaBancaria(nome, cpf, numero_conta)  # Cria a conta
    contas[cpf] = conta  # Guarda a conta
    print(f"Conta {numero_conta} (Agência: 0001) criada para {nome}!")
    return True

# Função principal que roda o programa
def main():
    clientes = {}  # Lista de clientes (CPF -> nome)
    contas = {}    # Lista de contas (CPF -> conta)
    numero_conta = 1  # Começa o número da conta em 1

    # Menu que aparece sempre
    while True:
        print("\n--- Banco ---")
        print("1. Cadastrar Cliente")
        print("2. Criar Conta")
        print("3. Depositar")
        print("4. Sacar")
        print("5. Ver Extrato")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":  # Cadastrar um cliente novo
            nome = input("Digite o nome: ").strip()
            cpf = input("Digite o CPF (só números): ").strip()
            if not nome or not cpf.isdigit():
                print("Nome ou CPF errado!")
                continue
            cadastrar_usuario(clientes, nome, cpf)

        elif opcao == "2":  # Criar uma conta nova
            cpf = input("Digite o CPF: ").strip()
            if not cpf.isdigit():
                print("CPF errado!")
                continue
            if cadastrar_conta_bancaria(clientes, contas, cpf, numero_conta):
                numero_conta += 1  # Aumenta o número para a próxima conta

        elif opcao == "3":  # Depositar dinheiro
            cpf = input("Digite o CPF: ").strip()
            if cpf not in contas:
                print("Conta não existe!")
                continue
            try:
                valor = float(input("Valor para depositar: R$ "))
                depositar(contas[cpf], valor)
            except:
                print("Valor errado!")

        elif opcao == "4":  # Sacar dinheiro
            cpf = input("Digite o CPF: ").strip()
            if cpf not in contas:
                print("Conta não existe!")
                continue
            try:
                valor = float(input("Valor para sacar: R$ "))
                sacar(contas[cpf], valor)
            except:
                print("Valor errado!")

        elif opcao == "5":  # Mostrar extrato
            cpf = input("Digite o CPF: ").strip()
            if cpf not in contas:
                print("Conta não existe!")
                continue
            extrato(contas[cpf])

        elif opcao == "6":  # Sair do programa
            print("Tchau!")
            break

        else:
            print("Opção errada!")

# Começa o programa
if __name__ == "__main__":
    main()