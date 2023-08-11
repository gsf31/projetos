#Conversor de Segundos ;)
segundos_str = input("Por favor, digite o número de segundos que deseja converter: ")
segundos_int = int(segundos_str)

dias = segundos_int // 86400
seg_restantes_dia = segundos_int % 86400
horas = seg_restantes_dia // 3600
seg_restantes_horas = seg_restantes_dia % 3600
minutos = seg_restantes_horas // 60
seg_restantes_minutos = seg_restantes_horas % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e", seg_restantes_minutos, "segundos.")