from services.interfaces import (
    InterfaceNotificador
)


class Notificador(
    InterfaceNotificador
):

    def notificar_emprestimo(
        self,
        email,
        data_devolucao
    ):

        print(
            f"[EMAIL] Empréstimo registrado para "
            f"{email}. Devolução prevista: "
            f"{data_devolucao}"
        )

    def notificar_devolucao(
        self,
        email,
        multa
    ):

        print(
            f"[EMAIL] Devolução registrada. "
            f"Multa: R$ {multa:.2f}"
        )

    def notificar_atraso(
        self,
        email
    ):

        print(
            f"[EMAIL] Aviso de atraso enviado "
            f"para {email}"
        )
