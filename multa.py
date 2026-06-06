def calcular_multa_com_carencia(
    dias_atraso,
    carencia,
    valor_dia
):
    dias_cobrados = max(
        0,
        dias_atraso - carencia
    )

    return round(
        dias_cobrados * valor_dia,
        2
    )