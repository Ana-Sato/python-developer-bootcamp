def sacar(valor): 
    saldo = 500

    if saldo >= valor:
        print("valor sacado!")
        print("retire o seu dinheiro na boca do caixa.")

    print("Obrigado por se nosso cliente, tenha um bom dia!")

sacar(100)

def depositar(valor): 

    saldo = 500
    saldo += valor 
