numero_1 = float(input(('Digite um número: ')))
operador = input("Digite um operador: ")
numero_2 = float(input(('Digite um número: ')))

if operador == '+':
    resposta = numero_1 + numero_2
elif operador == '-':
    resposta = numero_1 - numero_2
elif operador == '*':
    resposta = numero_1 * numero_2
elif operador == '**':
    resposta = numero_1 ** numero_2
elif operador == '/':
    resposta = numero_1 / numero_2
elif operador == '%':
    resposta = numero_1 % numero_2
else:
    resposta = 'error'

print(resposta)