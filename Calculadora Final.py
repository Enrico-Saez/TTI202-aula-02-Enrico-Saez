import operacoes_basicas
import calculadora

a = float(input("Digite o primeiro número: "))

b = float(input("Digite o segundo número: "))

choice = input("Selecione a operação:\n \
                1 - Soma\n \
                2 - Subtração\n \
                3 - Multiplicação\n \
                4 - Divisão\n \
                5 - Potenciação\n \
                6 - Radiciação\n \
")
choiceList = ['1','2','3','4','5','6']

while choice not in choiceList:
    choice = input("Operação inválida, digite novamente: ")

if choice == '1':
    result = operacoes_basicas.soma(a, b)
if choice == '2':
    result = operacoes_basicas.subtracao(a, b)
if choice == '3':
    result = operacoes_basicas.multiplicacao(a, b)
if choice == '4':
    result = operacoes_basicas.divisao(a, b)
if choice == '5':
    result = calculadora.potenciacao(a, b)
if choice == '6':
    result = calculadora.radiciacao(a, b)
    
print(f'Resultado: {result}')