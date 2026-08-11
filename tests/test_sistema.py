from datetime import date, timedelta
from app.sistema import SistemaDeEmprestimos

def test_registrar_retorna_true():
    sistema = SistemaDeEmprestimos()

    resultado = sistema.registrar(1, "Ana", "ana@email.com", 7)

    assert resultado is True

def test_registrar_devolucao_retorna_multa():
    sistema = SistemaDeEmprestimos()
    sistema.registrar(1, "Ana", "ana@email.com", 7)

    multa = sistema.registrar_devolucao(1)

    assert multa == 0

def test_listar_atrasados_retorna_emprestimos_atrasados():
    sistema = SistemaDeEmprestimos()
    sistema.registrar(2, "Bruno", "bruno@email.com", 7)

    emprestimo = sistema._servico.repo.buscar_emprestimos()[0]
    emprestimo.data_devolucao = date.today() - timedelta(days=3)

    atrasados = sistema.listar_atrasados()

    assert len(atrasados) == 1
    assert atrasados[0].email == "bruno@email.com"