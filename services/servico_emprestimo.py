from datetime import date, timedelta
from services.observer import Subject
from services.evento import Evento
from models.emprestimo import Emprestimo
from repositories.interfaces import InterfaceRepositorioEmprestimo


class ServicoEmprestimo(Subject):
    def __init__(
        self,
        repositorio: InterfaceRepositorioEmprestimo,
    ):
        super().__init__()
        self.repo = repositorio

    def contar_emprestimos_ativos_usuario(self, nome):

        return len(
            [
                emprestimo
                for emprestimo in self.repo.buscar_emprestimos()
                if (emprestimo.nome_usuario == nome and not emprestimo.devolvido)
            ]
        )

    def registrar(self, equip_id, nome, email, dias_emprestimo):

        equipamento = self.repo.buscar_equipamento(equip_id)

        if equipamento is None:
            return False

        if not equipamento.disponivel:
            return False

        if self.contar_emprestimos_ativos_usuario(nome) >= 2:
            return False

        devolucao = date.today() + timedelta(days=dias_emprestimo)

        emprestimo = Emprestimo(
            id=len(self.repo.emprestimos) + 1,
            equipamento_id=equip_id,
            nome_usuario=nome,
            email=email,
            data_devolucao=devolucao,
            devolvido=False,
        )

        self.repo.salvar_emprestimo(emprestimo)

        self.repo.marcar_indisponivel(equip_id)

        self.notificar(Evento(tipo="emprestimo", email=email, data=devolucao))

        return True

    def registrar_devolucao(self, emprestimo_id):

        for emprestimo in self.repo.buscar_emprestimos():
            if emprestimo.id == emprestimo_id and not emprestimo.devolvido:
                multa = self.calcular_multa(emprestimo)

                emprestimo.devolvido = True

                self.repo.marcar_disponivel(emprestimo.equipamento_id)

                self.notificar(
                    Evento(tipo="devolucao", email=emprestimo.email, multa=multa)
                )

                return multa

        return None

    def calcular_multa(self, emprestimo):

        equipamento = self.repo.buscar_equipamento(emprestimo.equipamento_id)

        dias_atraso = (date.today() - emprestimo.data_devolucao).days

        return equipamento.calcular_multa(dias_atraso)

    def listar_atrasados(self):

        atrasados = []

        for emprestimo in self.repo.buscar_emprestimos():
            if self._esta_atrasado(emprestimo):
                self._processar_atraso(emprestimo)
                atrasados.append(emprestimo)

        return atrasados

    def _esta_atrasado(self, emprestimo):
        return emprestimo.data_devolucao < date.today() and not emprestimo.devolvido

    def _processar_atraso(self, emprestimo):
        emprestimo.multa = self.calcular_multa(emprestimo)
        self.notificar(Evento(tipo="atraso", email=emprestimo.email))
