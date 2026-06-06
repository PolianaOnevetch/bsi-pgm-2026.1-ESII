from repositories.repositorio_emprestimo import (
    RepositorioEmprestimo
)

from services.notificador import (
    Notificador
)

from services.servico_emprestimo import (
    ServicoEmprestimo
)


def exibir_menu():

    print("\n===== Sistema de Empréstimos =====")
    print("1 - Registrar empréstimo")
    print("2 - Registrar devolução")
    print("3 - Listar atrasados")
    print("0 - Sair")


def main():

    repositorio = (
        RepositorioEmprestimo()
    )

    notificador = (
        Notificador()
    )

    servico = ServicoEmprestimo(
        repositorio,
        notificador
    )

    while True:

        exibir_menu()

        opcao = input(
            "Escolha uma opção: "
        )

        if opcao == "1":

            sucesso = servico.registrar(
                int(
                    input(
                        "ID do equipamento: "
                    )
                ),
                input(
                    "Nome do usuário: "
                ),
                input(
                    "Email: "
                ),
                int(
                    input(
                        "Quantidade de dias: "
                    )
                )
            )

            if sucesso:
                print(
                    "Empréstimo registrado com sucesso."
                )
            else:
                print(
                    "Equipamento inválido ou indisponível."
                )

        elif opcao == "2":

            resultado = (
                servico.registrar_devolucao(
                    int(
                        input(
                            "ID do empréstimo: "
                        )
                    )
                )
            )

            if resultado is None:

                print(
                    "Empréstimo inválido ou já devolvido."
                )

            else:

                print(
                    f"Devolução registrada. "
                    f"Multa: R$ {resultado:.2f}"
                )

        elif opcao == "3":

            atrasados = (
                servico.listar_atrasados()
            )

            if not atrasados:

                print(
                    "Nenhum empréstimo em atraso."
                )

            else:

                print(
                    "\nEmpréstimos em atraso:"
                )

                for emprestimo in atrasados:

                    print(
                        f"Usuário: "
                        f"{emprestimo.nome_usuario}"
                    )

                    print(
                        f"Multa: "
                        f"R$ {emprestimo.multa:.2f}"
                    )

                    print("-" * 30)

        elif opcao == "0":

            print(
                "Encerrando sistema..."
            )

            break

        else:

            print(
                "Opção inválida."
            )


if __name__ == "__main__":
    main()
