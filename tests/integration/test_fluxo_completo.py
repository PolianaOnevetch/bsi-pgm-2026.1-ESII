from repositories.repositorio_emprestimo import RepositorioEmprestimo
from services.notificador_email import NotificadorEmail
from services.servico_emprestimo import ServicoEmprestimo


def test_fluxo_completo():

    repo = RepositorioEmprestimo()

    servico = ServicoEmprestimo(repo)

    # 👇 REGISTRA O OBSERVER
    servico.registrar_observer(NotificadorEmail())

    servico.registrar(1, "Ana", "ana@email.com", 7)

    multa = servico.registrar_devolucao(1)

    assert multa == 0
