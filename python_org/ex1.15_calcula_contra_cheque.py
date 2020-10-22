valorhora = float(input("Quanto você ganha por hora? R$ "))
horasmes = int(input("Quantas horas você trabalhou esse mês? "))
salariobruto = valorhora * horasmes
ir = (salariobruto * 11)/100
inss = (salariobruto * 8)/100
sindicato = (salariobruto * 5)/100
salarioliquido = salariobruto - (ir + inss + sindicato)
print(f"Segue seu contracheque do mês atual:"
      f"\nSalário Bruto: R$ {salariobruto:.2f}"
      f"\nDescontos: "
      f"\n    Imposto de Renda: R$ {ir:.2f}"
      f"\n    INSS: R$ {inss:.2f}"
      f"\n    Sindicato: R$ {sindicato:.2f}"
      f"\nSalário Líquido: R$ {salarioliquido:.2f}")
