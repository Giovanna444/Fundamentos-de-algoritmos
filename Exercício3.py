dia=float(input("Digite a quantidade de dias:"))
hora=float(input("Digite a quantidade de horas:"))
minuto=float(input("Digite a quantidade de minutos:"))
segundo=float(input("Digite a quantidade de segundos:"))
seg_dia=86400*dia
seg_hora=3600*hora
seg_minuto=60*minuto
seg_segundo= segundo
total_seg= seg_dia + seg_hora + seg_minuto + seg_segundo 
print("O valor total em segundos é de %.2f:"% total_seg)