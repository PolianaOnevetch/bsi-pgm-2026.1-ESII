import pytest

from models.equipamento import (
    Notebook,
    Projetor,
    Cabo
)


@pytest.mark.parametrize(
    "dias,multa_esperada",
    [
        (0, 0),
        (1, 10),
        (3, 30),
    ]
)
def test_multa_notebook(
    dias,
    multa_esperada
):

    notebook = Notebook(
        1,
        "Notebook",
        True
    )

    assert (
        notebook.calcular_multa(dias)
        == multa_esperada
    )


@pytest.mark.parametrize(
    "dias,multa_esperada",
    [
        (0, 0),
        (1, 15),
        (3, 45),
    ]
)
def test_multa_projetor(
    dias,
    multa_esperada
):

    projetor = Projetor(
        2,
        "Projetor",
        True
    )

    assert (
        projetor.calcular_multa(dias)
        == multa_esperada
    )