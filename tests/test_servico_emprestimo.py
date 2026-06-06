from datetime import date, timedelta


def test_registrar_retorna_true(
    servico
):

    resultado = servico.registrar(
        1,
        "Ana",
        "ana@email.com",
        7
    )

    assert resultado is True


def test_registrar_retorna_false_quando_equipamento_nao_existe(
    servico
):

    resultado = servico.registrar(
        999,
        "Ana",
        "ana@email.com",
        7
    )

    assert resultado is False


def test_registrar_torna_equipamento_indisponivel(
    servico
):

    servico.registrar(
        1,
        "Ana",
        "ana@email.com",
        7
    )

    equipamento = (
        servico.repo.buscar_equipamento(1)
    )

    assert equipamento.disponivel is False


def test_registrar_cria_emprestimo(
    servico
):

    servico.registrar(
        1,
        "Ana",
        "ana@email.com",
        7
    )

    assert (
        len(
            servico.repo.buscar_emprestimos()
        )
        == 1
    )


def test_registrar_devolucao_retorna_zero(
    servico
):

    servico.registrar(
        1,
        "Ana",
        "ana@email.com",
        7
    )

    resultado = (
        servico.registrar_devolucao(
            1
        )
    )

    assert resultado == 0


def test_registrar_devolucao_inexistente(
    servico
):

    resultado = (
        servico.registrar_devolucao(
            999
        )
    )

    assert resultado is None


def test_listar_atrasados(
    servico
):

    servico.registrar(
        1,
        "Ana",
        "ana@email.com",
        7
    )

    emprestimo = (
        servico.repo.buscar_emprestimos()[0]
    )

    emprestimo.data_devolucao = (
        date.today()
        - timedelta(days=2)
    )

    atrasados = (
        servico.listar_atrasados()
    )

    assert len(atrasados) == 1