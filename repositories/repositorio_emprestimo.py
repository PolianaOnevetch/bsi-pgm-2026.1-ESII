from repositories.interfaces import (
    InterfaceRepositorioEmprestimo
)

from models.fabrica_equipamento import (
    FabricaEquipamento
)


class RepositorioEmprestimo(
    InterfaceRepositorioEmprestimo
):

    def __init__(self):

        self.equipamentos = [
            FabricaEquipamento.criar(
                "notebook",
                1,
                "Notebook Dell"
            ),

            FabricaEquipamento.criar(
                "projetor",
                2,
                "Projetor Epson"
            ),

            FabricaEquipamento.criar(
                "cabo",
                3,
                "Cabo HDMI"
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