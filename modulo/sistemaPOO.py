class ContaBancaria:
    def __init__(self, numero_conta, titular, saldo=0):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo
        self.extrato = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                self.extrato.append(f"Saque: R$ {valor:.2f}")
                print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("O valor do saque deve ser positivo.")

    def exibir_extrato(self):
        print(f"Extrato da conta {self.numero_conta}:")
        for operacao in self.extrato:
            print(operacao)
        print(f"Saldo atual: R$ {self.saldo:.2f}")

class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.contas = []

    def criar_conta(self, numero_conta, titular):
        nova_conta = ContaBancaria(numero_conta, titular)
        self.contas.append(nova_conta)
        print(f"Conta {numero_conta} criada com sucesso para {titular}.")

    def buscar_conta(self, numero_conta):
        for conta in self.contas:
            if conta.numero_conta == numero_conta:
                return conta
        return None

    def depositar(self, numero_conta, valor):
        conta = self.buscar_conta(numero_conta)
        if conta:
            conta.depositar(valor)
        else:
            print("Conta não encontrada.")

    def sacar(self, numero_conta, valor):
        conta = self.buscar_conta(numero_conta)
        if conta:
            conta.sacar(valor)
        else:
            print("Conta não encontrada.")

    def exibir_extrato(self, numero_conta):
        conta = self.buscar_conta(numero_conta)
        if conta:
            conta.exibir_extrato()
        else:
            print("Conta não encontrada.")

# Exemplo de uso do sistema bancário
banco = Banco("Meu Banco")

# Criar contas
banco.criar_conta(123, "Alice")
banco.criar_conta(456, "Bob")

# Operações na conta da Alice
banco.depositar(123, 1000)
banco.sacar(123, 500)
banco.exibir_extrato(123)

# Operações na conta do Bob
banco.depositar(456, 1500)
banco.sacar(456, 300)
banco.exibir_extrato(456)
