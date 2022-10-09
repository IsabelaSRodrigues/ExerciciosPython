#Lista 1 
#Questão 2

peso = int(input('Digite o valor do peso:'))
if(peso>50):
  excesso = peso - 50
  multa = excesso * 4
  print(f'O total de peso dos peixes é {peso} quilos, excedeu {excesso} quilos e terá que pagar uma multa de R${multa}')
else:
  print(f'O peso dos peixes é {peso} quilos e não gerá cobrança de multa.')


#Questão 3

salario = float(input('Informe o valor recebido por hora:'))
horas = int(input('Informe a quatidade de horas trabalhadas:'))

salarioB = salario * horas
inss = salarioB * 0.08
sindicato = salarioB * 0.05
ir = salarioB * 0.11
salarioL = salarioB - inss - sindicato - ir

print(f'Salário Bruto:R${salarioB}')
print(f'Valor do desconto para o INSS:R${inss}')
print(f'Valor do desconto para o sindicato:R${sindicato}')
print(f'Valor de desconto Imposto de Renda:R${ir}')
print(f'Valor do salário líquido:R${salarioL}')

#Questão 4

area = int(input('Informe o valor da área a ser pintada em metros quadrados: '))
tinta = area / 3  
lata = tinta / 18
valor = lata * 80

print(f'Quantidade de latas necessárias = {lata}')
print(f'Valor total  = R${valor}')


#Lista 2

#Questão 2

numero = int(input('Digite um número inteiro:'))
if(numero % 2 == 0):
  print('Número par!')
else:
  print('Número impar!')

#Questão 4

idades = []
alturas = []
for i in range(1, 6):
    idade = int(input(f'Digite a idade da posição {i}: '))
    altura = float(input(f'Digite a altura da posição {i}: '))
    idades.append(idade)
    alturas.append(altura)

print('Ordem inversa')
print('Alturas')
print(alturas[::-1])
print('Idades')
print(idades[::-1])

print('Ordem lida')
print('Alturas')
print(alturas)

print('Idades')
print(idades)


#Questão 5

soma = 0
for i in range(10):
    soma += int(input(f"Digite o {i+1}º numero inteiro: ")) ** 2
print(f"A soma dos quadrados dos numeros digitados é {soma}")


