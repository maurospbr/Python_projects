from types import DynamicClassAttribute


nome = input(" insira seu nome: ")
print("Bem vindo", nome)
def idade():
    nascimento =  int(input("informe seu ano de nascimento: " ))
    anoatual = int(input("informe o anual atual: "))
    idade = anoatual-nascimento
    print("Sua idade é: ", idade)
    
idade()
nome1 = input(" insira seu nome: ")
print("Bem vindo", nome1)
def idade1():
    nascimento1 =  int(input("informe seu ano de nascimento: " ))
    anoatual_1 = int(input("informe o anual atual: "))
    idade1 = anoatual_1-nascimento1
    print("Sua idade é: ", idade1)
idade1()

if idade > idade1:
    print("O mais velho é: ", idade)
    print("O mais velhoe é: ", nome)
elif idade < idade1:
    print("O mais velho é: ", idade1)
    print("O mais velhoe é: ", nome1)
