from models.equipamento import (
    Notebook,
    Projetor,
    Cabo
)


class FabricaEquipamento:

    @staticmethod
    def criar(
        tipo,
        id,
        nome
    ):

        if tipo == "notebook":
            return Notebook(
                id,
                nome,
                True
            )

        if tipo == "projetor":
            return Projetor(
                id,
                nome,
                True
            )

        if tipo == "cabo":
            return Cabo(
                id,
                nome,
                True
            )

        raise ValueError(
            f"Tipo inválido: {tipo}"
        )