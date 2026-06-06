def calcular_multa_com_carencia(
    dias_atraso,
    carencia,
    valor_dia
):
    if dias_atraso <= carencia:
        return 0.0

    excedente = dias_atraso - carencia

    return excedente * valor_dia