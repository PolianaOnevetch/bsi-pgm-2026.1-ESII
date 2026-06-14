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

        repositorio = (
            RepositorioEmprestimo()
        )

        notificador = (
            Notificador()
        )

        self.servico = (
            ServicoEmprestimo(
                repositorio,
                notificador
            )
        )

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