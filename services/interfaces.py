from abc import ABC, abstractmethod


class InterfaceNotificador(ABC):

    @abstractmethod
    def notificar_emprestimo(
        self,
        email,
        data_devolucao
    ):
        pass

    @abstractmethod
    def notificar_atraso(
        self,
        email
    ):
        pass

    @abstractmethod
    def notificar_devolucao(
        self,
        email,
        multa
    ):
        pass
