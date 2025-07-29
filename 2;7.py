dia = int(input())

dias_semana = {
    1: "DOMINGO",
    2: "SEGUNDA-FEIRA",
    3: "TERCA-FEIRA",
    4: "QUARTA-FEIRA",
    5: "QUINTA-FEIRA",
    6: "SEXTA-FEIRA",
    7: "SABADO"
}

if 1 <= dia <= 7:
    print(dias_semana[dia])
