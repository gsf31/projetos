segundos_str = input("Por favor, digite o número de segundos que deseja converter: ")
total_segs = int(segundos_str)

dias = total_segs // 86400
segs_restantes_dia = total_segs % 86400
horas = segs_restantes_dia // 3600
segs_restantes_horas = segs_restantes_dia % 3600
minutos = segs_restantes_horas // 60
segs_restantes_minutos = segs_restantes_horas % 60

print(dias, "dias, ",horas, "horas, ",minutos, "minutos e",segs_restantes_minutos, "segundos.")
  