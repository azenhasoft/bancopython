class ContaBancaria:
    """
    Representa uma conta bancária com funcionalidades de depósito, saque e extrato.
    Mantém o saldo e o histórico de transações com duas casas decimais, usando vírgula como separador.
    """
    def __init__(self, titular, saldo_inicial=0.00):
        """
        Inicializa uma nova conta bancária.

        Args:
            titular (str): O nome do titular da conta.
            saldo_inicial (float, opcional): O saldo inicial da conta. Defaults to 0.00.
        """
        self.titular = titular
        self.saldo = round(saldo_inicial, 2)  # Garante que o saldo inicial tenha duas casas decimais
        self.historico = []  # Lista para armazenar o histórico de transações
        self.historico.append(f"Saldo inicial: R$ {self.formatar_valor(self.saldo)}")

    def formatar_valor(self, valor):
        """
        Formata um valor numérico para string com duas casas decimais e vírgula como separador.

        Args:
            valor (float): O valor a ser formatado.

        Returns:
            str: O valor formatado como string.
        """
        return f"{valor:.2f}".replace('.', ',')

    def depositar(self, valor):
        """
        Realiza um depósito na conta.

        Args:
            valor (float): O valor a ser depositado.
        """
        if valor > 0:
            self.saldo = round(self.saldo + valor, 2)  # Atualiza o saldo e garante duas casas decimais
            self.historico.append(f"Depósito: +R$ {self.formatar_valor(valor)}")
            print("Depósito realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        """
        Realiza um saque na conta.

        Args:
            valor (float): O valor a ser sacado.
        """
        if valor > 0 and valor <= self.saldo:
            self.saldo = round(self.saldo - valor, 2)  # Atualiza o saldo e garante duas casas decimais
            self.historico.append(f"Saque: -R$ {self.formatar_valor(valor)}")
            print("Saque realizado com sucesso.")
        elif valor <= 0:
            print("Valor inválido para saque.")
        else:
            print("Saldo insuficiente.")

    def exibir_extrato(self):
        """
        Exibe o extrato da conta, mostrando o saldo atual e o histórico de transações
        com formatação de duas casas decimais e vírgula como separador.
        """
        print("\n--- Extrato Bancário ---")
        print(f"Titular: {self.titular}")
        print(f"Saldo atual: R$ {self.formatar_valor(self.saldo)}")
        print("\nHistórico de Transações:")
        for operacao in self.historico:
            print(f"- {operacao}")
        print("-------------------------\n")

def menu():
    """
    Exibe o menu de opções para o usuário.

    Returns:
        str: A opção escolhida pelo usuário.
    """
    print("\n--- Sistema Bancário ---")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Exibir Extrato")
    print("4. Sair")
    print("-------------------------\n")
    return input("Escolha uma opção: ")

def main():
    """
    Função principal que inicia e controla o fluxo do programa.
    Garante que os valores de entrada para depósito e saque sejam tratados com duas casas decimais
    e que a saída utilize vírgula como separador.
    """
    nome_titular = input("Digite o nome do titular da conta: ")
    conta = ContaBancaria(nome_titular)  # Cria uma instância da classe ContaBancaria

    while True:
        opcao = menu()  # Exibe o menu e obtém a escolha do usuário

        if opcao == '1':
            try:
                valor_deposito_str = input("Digite o valor a depositar (use ',' para centavos): R$ ")
                valor_deposito = round(float(valor_deposito_str.replace(',', '.')), 2)
                conta.depositar(valor_deposito)
            except ValueError:
                print("Entrada inválida. Digite um valor numérico válido (ex: 10,50).")
        elif opcao == '2':
            try:
                valor_saque_str = input("Digite o valor a sacar (use ',' para centavos): R$ ")
                valor_saque = round(float(valor_saque_str.replace(',', '.')), 2)
                conta.sacar(valor_saque)
            except ValueError:
                print("Entrada inválida. Digite um valor numérico válido (ex: 5,75).")
        elif opcao == '3':
            conta.exibir_extrato()
        elif opcao == '4':
            print("Obrigado por utilizar nosso sistema bancário!")
            break  # Sai do loop principal
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()  # Executa a função principal se o script for executado diretamente