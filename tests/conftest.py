import pytest

from models.fabrica_equipamento import FabricaEquipamento
from services.servico_emprestimo import (
    ServicoEmprestimo
)


class FakeRepositorio:

    def __init__(self):

        self.equipamentos = [
        FabricaEquipamento.criar("notebook", 1, "Notebook")
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

        equipamento = self.buscar_equipamento(
            equip_id
        )

        if equipamento:
            equipamento.disponivel = False

    def marcar_disponivel(
        self,
        equip_id
    ):

        equipamento = self.buscar_equipamento(
            equip_id
        )

        if equipamento:
            equipamento.disponivel = True


class FakeNotificador:

    def notificar_emprestimo(
        self,
        email,
        data
    ):
        pass

    def notificar_atraso(
        self,
        email
    ):
        pass

    def notificar_devolucao(
        self,
        email,
        multa
    ):
        pass


@pytest.fixture
def servico():

    repo = FakeRepositorio()

    notif = FakeNotificador()

    return ServicoEmprestimo(
        repo,
        notif
    )