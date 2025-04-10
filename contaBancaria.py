# Classe principal que representa uma conta bancária
class ContaBancaria:
    def __init__(self, titular, saldo=0.0):
        """Inicializa uma nova conta bancária"""
        self.titular = titular      # Nome do dono da conta
        self.saldo = saldo          # Saldo inicial (default = 0)
        self.historico = []         # Lista para armazenar transações

    def depositar(self, valor):
        """Adiciona dinheiro à conta"""
        if valor > 0:  # Só deposita valores positivos
            self.saldo += valor
            self.historico.append(f"Depósito: R$ {valor:.2f}")
            print("Depósito realizado!")
        else:
            print("Valor inválido!")  # Mensagem se valor for negativo

    def sacar(self, valor):
        """Retira dinheiro da conta"""
        if valor > 0 and valor <= self.saldo:  # Verifica saldo e valor positivo
            self.saldo -= valor
            self.historico.append(f"Saque: R$ {valor:.2f}")
            print("Saque realizado!")
        else:
            # Mensagem para saldo insuficiente ou valor inválido
            print("Saldo insuficiente ou valor inválido!")

    def extrato(self):
        """Mostra o saldo e histórico de transações"""
        print(f"\n--- Extrato ---")
        print(f"Titular: {self.titular}")
        print(f"Saldo atual: R$ {self.saldo:.2f}")  # Formata com 2 casas decimais
        print("\nHistórico:")
        for operacao in self.historico:  # Imprime cada transação
            print(f"- {operacao}")

# Função principal que controla o programa
def main():
    # Cria a conta com o nome do usuário
    nome = input("Digite seu nome: ")
    conta = ContaBancaria(nome)

    # Menu interativo
    while True:
        print("\n1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Sair")
        opcao = input("Opção: ")  # Recebe a escolha do usuário

        if opcao == "1":  # Depósito
            try:
                valor = float(input("Valor para depositar: R$ "))
                conta.depositar(valor)
            except:
                print("Valor inválido!")  # Se usuário digitar texto
        
        elif opcao == "2":  # Saque
            try:
                valor = float(input("Valor para sacar: R$ "))
                conta.sacar(valor)
            except:
                print("Valor inválido!")
        
        elif opcao == "3":  # Extrato
            conta.extrato()
        
        elif opcao == "4":  # Sair
            print("Até logo!")
            break  # Encerra o programa
        
        else:  # Opção inválida
            print("Opção inválida!")

# Ponto de entrada do programa
if __name__ == "__main__":
    main()
