class MultaProgressiva:

    def calcular(self, dias_atraso):

        if dias_atraso <= 0:
            return 0

        if dias_atraso <= 3:
            return dias_atraso * 5

        elif dias_atraso <= 7:
            return dias_atraso * 10

        else:
            return dias_atraso * 20