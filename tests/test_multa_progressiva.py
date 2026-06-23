from models.multa_progressiva import MultaProgressiva


def test_multa_progressiva():

    estrategia = MultaProgressiva()

    assert estrategia.calcular(0) == 0
    assert estrategia.calcular(2) == 10
    assert estrategia.calcular(5) == 50
    assert estrategia.calcular(10) == 200