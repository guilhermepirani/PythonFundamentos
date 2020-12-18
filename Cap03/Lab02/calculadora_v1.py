# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************\n")

# Funções

def soma(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

# Main

print("\nSelecione o número da operação desejada: ")

# Imprime na tela as operações possíveis
operacoes = ["1 - Soma", "2 - Subtração", "3 - Multiplicação", "4 - Divisão"]

for i in operacoes:
    print(i)

op = 0
while not op in [1, 2, 3, 4]:
    op = int(input("\nDigite sua opção (1/2/3/4): "))


# Decidi usar floats para posibilitar operações com números fracionados, diferente do exemplo
num1 = float(input("\nDigite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Calcula e imprime o resultado
opcoes = [soma(num1, num2), sub(num1, num2), mult(num1, num2), div(num1, num2)]
print(f"Resultado {operacoes[op - 1][4::]} = {opcoes[op - 1]}")