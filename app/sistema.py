from services.notificador_email import NotificadorEmail
from repositories.repositorio_emprestimo import (
    RepositorioEmprestimo
)

from services.notificador import (
    Notificador
)

from services.servico_emprestimo import (
    ServicoEmprestimo
)


class SistemaDeEmprestimos:

    def __init__(self):

        self._repositorio = RepositorioEmprestimo()
        self._servico = ServicoEmprestimo(self._repositorio)
        self._servico.registrar_observer(NotificadorEmail())

    def registrar(
        self,
        equipamento_id,
        nome,
        email,
        dias
    ):
        return self.servico.registrar(
            equipamento_id,
            nome,
            email,
            dias
        )

    def registrar_devolucao(
        self,
        emprestimo_id
    ):
        return (
            self.servico
            .registrar_devolucao(
                emprestimo_id
            )
        )

    def listar_atrasados(
        self
    ):
        return (
            self.servico
            .listar_atrasados()
        )