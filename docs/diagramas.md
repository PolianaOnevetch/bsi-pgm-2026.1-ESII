# Diagramas e Decomposição

## Visão Geral

A estrutura proposta para a versão 2.0 busca resolver os problemas identificados na versão inicial do sistema, principalmente aqueles relacionados à concentração de responsabilidades, dificuldade de manutenção e baixa testabilidade.

A solução adotada segue a arquitetura em camadas definida no ADR-001, separando os componentes conforme suas responsabilidades.

---

# Decomposição do Sistema

## Camada de Modelos (models)

### Equipamento

Responsável por representar os equipamentos cadastrados no sistema.

A classe define os atributos comuns dos equipamentos e estabelece o contrato para cálculo de multas através do método `calcular_multa()`.

Subclasses especializadas implementam as regras específicas de cada tipo de equipamento.

### Emprestimo

Responsável por representar um empréstimo realizado.

Armazena informações como:

- identificador;
- equipamento associado;
- nome do solicitante;
- e-mail;
- data prevista para devolução;
- situação do empréstimo;
- valor da multa.

---

## Camada de Serviços (services)

### ServicoEmprestimo

Centraliza as regras de negócio relacionadas ao processo de empréstimo.

Principais responsabilidades:

- registrar empréstimos;
- registrar devoluções;
- calcular multas;
- verificar atrasos;
- solicitar notificações.

### Notificador

Responsável pela comunicação com os usuários.

Suas funções incluem:

- informar empréstimos realizados;
- informar devoluções;
- informar situações de atraso.

A separação dessa responsabilidade evita que regras de negócio fiquem misturadas com mecanismos de comunicação.

---

## Camada de Persistência (repositories)

### RepositorioEmprestimo

Responsável pelo gerenciamento dos dados do sistema.

Funções principais:

- armazenar equipamentos;
- armazenar empréstimos;
- localizar registros;
- atualizar disponibilidade dos equipamentos.

---

## Camada de Interface

### main.py

Responsável pela interação direta com o usuário.

Apresenta o menu principal, recebe entradas e encaminha as solicitações para os serviços apropriados.

Não contém regras de negócio.

---

# Diagrama de Sequência — UC01 Registrar Empréstimo

```mermaid
sequenceDiagram

actor Atendente

participant Main
participant ServicoEmprestimo
participant Repositorio
participant Notificador

Atendente->>Main: Solicita registro de empréstimo
Main->>ServicoEmprestimo: registrar(...)

ServicoEmprestimo->>Repositorio: buscar_equipamento(id)

Repositorio-->>ServicoEmprestimo: equipamento

alt Equipamento disponível

ServicoEmprestimo->>Repositorio: salvar_emprestimo()

ServicoEmprestimo->>Repositorio: marcar_indisponivel()

ServicoEmprestimo->>Notificador: notificar_emprestimo()

ServicoEmprestimo-->>Main: sucesso

else Equipamento indisponível

ServicoEmprestimo-->>Main: erro

end
```

---

# Diagrama de Sequência — UC02 Registrar Devolução

```mermaid
sequenceDiagram

actor Atendente

participant Main
participant ServicoEmprestimo
participant Repositorio
participant Notificador

Atendente->>Main: Solicita devolução

Main->>ServicoEmprestimo: registrar_devolucao(id)

ServicoEmprestimo->>Repositorio: buscar empréstimo

Repositorio-->>ServicoEmprestimo: empréstimo

alt Empréstimo válido

ServicoEmprestimo->>Repositorio: marcar disponível

ServicoEmprestimo->>Notificador: notificar devolução

ServicoEmprestimo-->>Main: devolução realizada

else Empréstimo inválido

ServicoEmprestimo-->>Main: erro

end
```

---

# Diagrama de Sequência — UC03 Listar Empréstimos em Atraso

```mermaid
sequenceDiagram

actor Coordenador

participant Main
participant ServicoEmprestimo
participant Repositorio
participant Notificador

Coordenador->>Main: Solicita atrasados

Main->>ServicoEmprestimo: listar_atrasados()

ServicoEmprestimo->>Repositorio: buscar_emprestimos()

Repositorio-->>ServicoEmprestimo: lista

loop Para cada empréstimo

ServicoEmprestimo->>ServicoEmprestimo: calcular multa

alt Em atraso

ServicoEmprestimo->>Notificador: notificar atraso

end

end

ServicoEmprestimo-->>Main: lista de atrasados
```

---

# Justificativa da Decomposição

A divisão adotada procura aumentar a coesão interna dos módulos e reduzir o acoplamento entre componentes.

Cada camada possui uma responsabilidade específica:

- Models representam entidades do domínio.
- Services implementam regras de negócio.
- Repositories gerenciam dados.
- Main realiza interação com o usuário.

Essa organização facilita manutenção, evolução e testes isolados, contribuindo diretamente para o atendimento dos requisitos RNF03 e RNF04.

---

# Diagrama Simplificado após Refatoração

```mermaid
classDiagram

class SistemaDeEmprestimos {
    +registrar()
    +registrar_devolucao()
    +listar_atrasados()
}

class ServicoEmprestimo

class RepositorioEmprestimo

class Notificador

class FabricaEquipamento {
    +criar()
}

SistemaDeEmprestimos --> ServicoEmprestimo

ServicoEmprestimo --> RepositorioEmprestimo
ServicoEmprestimo --> Notificador

RepositorioEmprestimo --> FabricaEquipamento
```