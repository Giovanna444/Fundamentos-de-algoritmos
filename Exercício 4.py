valor_salario= float(input("Digite o quanto você ganha por hora:"))
valor_horas=float(input("Digte o quanto de horas você trabalha por mês:"))
salario_bruto= valor_salario * valor_horas 
ir= salario_bruto * 0.11
inss= salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido= salario_bruto - ir - inss - sindicato 
print("+ Salário Bruto: %.2f" % salario_bruto)
print("- IR: %.2f" % ir)
print("- INSS: %.2f" %inss)
print("- Sindicato: %.2f" %sindicato)
print("+ Salário Líquido: %.2f" %salario_liquido)