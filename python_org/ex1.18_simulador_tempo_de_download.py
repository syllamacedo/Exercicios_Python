tam = float(input("Qual tamanho do arquivo(em MB) que deseja fazer o download: "))
vel = float(input("Qual a velocidade da sua internet(em Mbps): "))

mbseg = vel / 8
mbmin = mbseg * 60
mbhora = mbmin * 60
totmin = tothora = 0
arquivo = tam

while arquivo > mbhora:
    arquivo -= mbhora
    tothora += 1
while arquivo > mbmin:
    arquivo -= mbmin
    totmin += 1
totmin += 1  # cuidando do resto que será baixado em menos de 1 minuto

print(f"Esse link de internet vai levar {tothora} horas e {totmin} minutos para baixar um arquivo de {tam} MB.")
