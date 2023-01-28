# 1
# print("Hello, world!")

# 2
# num = input()
# print("O número informado foi {}".format(num))

# 3
# num1 = int(input('1º número: '))
# num2 = int(input('2º número: '))
# soma = num1 + num2
# print("Soma: {}", soma)

# 4
# nota1 = float(input('1ª nota: '))
# nota2 = float(input('2ª nota: '))
# nota3 = float(input('3ª nota: '))
# nota4 = float(input('4ª nota: '))
# media = (nota1 + nota2 + nota3 + nota4) / 4
# print("Média: {}", media)

# 5
# metros = float(input('Informe a quantidade de metros: '))
# print("{} metros em centímetros são: {}".format(metros, metros * 100))

# 6
# PI = 3.14
# raio = float(input('Informe o raio da circunferência: '))
# print("A área da circunferência é: {}.".format(PI * raio ** 2))

# 15
# ganho_hora = float(input('Informe quanto você ganha por hora: '))
# horas_mes = int(input('Informe o nº de horas trabalhadas no mês: '))
# salario_bruto = ganho_hora * horas_mes
# imposto_renda = salario_bruto * 0.11
# inss = salario_bruto * 0.08
# sindicato = salario_bruto * 0.05
# salario_liquido = salario_bruto - (imposto_renda + inss + sindicato)
# print("+ Salário Bruto : R$ {}\n- IR (11%) : R$ {}\n- INSS (8%) : R$ {}\n- Sindicato (5%) : R$ {}\n= Salário Líquido : R$ {}".format(salario_bruto, imposto_renda, inss, sindicato, salario_liquido))

# 18
tamanho_arquivo = float(input('Informe o tamanho do arquivo (em MB): '))
velocidade_internet = float(input('Informe a velocidade da internet (em Mbps): '))
print("Levará {:.2f} minutos para baixar o arquivo.".format(tamanho_arquivo * 8 / velocidade_internet / 60))