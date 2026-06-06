from repositories.repositorio_emprestimo import (
    RepositorioEmprestimo
)

from services.notificador import (
    Notificador
)

from services.servico_emprestimo import (
    ServicoEmprestimo
)


def test_fluxo_completo():

    repo = (
        RepositorioEmprestimo()
    )

    notif = (
        Notificador()
    )

    servico = (
        ServicoEmprestimo(
            repo,
            notif
        )
    )

    servico.registrar(
        1,
        "Ana",
        "ana@email.com",
        7
    )

    multa = (
        servico.registrar_devolucao(
            1
        )
    )

    assert multa == 0