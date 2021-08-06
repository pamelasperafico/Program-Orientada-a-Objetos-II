from classes.banco import Banco
from classes.cliente import Cliente
from classes.contas import ContaPoupanca, ContaCorrente


cp1 = ContaPoupanca(1234, 987654, 0)
cc1 = ContaCorrente(9876, 123456, 50)
cp2 = ContaPoupanca(7654, 345678, 10)
ccnc1 = ContaCorrente(9638, 527410, 0)
cpnc1 = ContaPoupanca(1234, 741852, 50)
ccnc2 = ContaCorrente(7654, 321654, 0)

cliente1 = Cliente("Fulano", 31, cp1)
cliente2 = Cliente("Ciclano", 28, cc1)
cliente3 = Cliente("Beltrano", 40, cp2)
cliente4 = Cliente("Fulana", 35, ccnc1)
cliente5 = Cliente("Ciclana", 35, cpnc1)
cliente6 = Cliente("Beltrana", 40, ccnc2)

banco = Banco()
banco.cadastrar_agencia(1234)
banco.cadastrar_agencia(9876)
banco.cadastrar_agencia(7654)
banco.cadastrar_agencia(2468)
banco.cadastrar_agencia(1357)
banco.cadastrar_cliente(cliente1)
banco.cadastrar_cliente(cliente2)
banco.cadastrar_cliente(cliente3)


print(cliente1.nome)
if banco.autenticar(cliente1):
    cliente1.conta.depositar(100)
else:
    print("Autenticação inválida!")
print()

print(cliente2.nome)
if banco.autenticar(cliente2):
    cliente2.conta.sacar(30)
    print()
    cliente2.conta.sacar(30)
    print()
    cliente2.conta.sacar(100)
else:
    print("Autenticação inválida!")
print()

print(cliente3.nome)
if banco.autenticar(cliente3):
    cliente3.conta.sacar(20)
else:
    print("Autenticação inválida!")
print()

print(cliente4.nome)
if banco.autenticar(cliente4):
    cliente5.conta.sacar(10)
else:
    print("Autenticação inválida!")
print()

print(cliente5.nome)
if banco.autenticar(cliente5):
    cliente5.conta.sacar(50)
else:
    print("Autenticação inválida!")
print()

print(cliente6.nome)
if banco.autenticar(cliente6):
    cliente5.conta.sacar(10)
else:
    print("Autenticação inválida!")
print()
