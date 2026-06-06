from repositories.interfaces import (
    InterfaceRepositorioEmprestimo
)

from models.equipamento import (
    Notebook,
    Projetor,
    Cabo
)


class RepositorioEmprestimo(
    InterfaceRepositorioEmprestimo
):

    def __init__(self):

        self.equipamentos = [
            Notebook(
                1,
                "Notebook Dell",
                True
            ),
            Projetor(
                2,
                "Projetor Epson",
                True
            ),
            Cabo(
                3,
                "Cabo HDMI",
                True
            )
        ]

        self.emprestimos = []

    def buscar_equipamento(
        self,
        equip_id
    ):

        for equipamento in self.equipamentos:

            if equipamento.id == equip_id:
                return equipamento

        return None

    def salvar_emprestimo(
        self,
        emprestimo
    ):

        self.emprestimos.append(
            emprestimo
        )

    def buscar_emprestimos(
        self
    ):

        return self.emprestimos

    def marcar_indisponivel(
        self,
        equip_id
    ):

        equipamento = (
            self.buscar_equipamento(
                equip_id
            )
        )

        if equipamento:
            equipamento.disponivel = False

    def marcar_disponivel(
        self,
        equip_id
    ):

        equipamento = (
            self.buscar_equipamento(
                equip_id
            )
        )

        if equipamento:
            equipamento.disponivel = True
