# Cenário BDD

## Funcionalidade: Limite de empréstimos simultâneos

Scenario: Usuário não pode possuir mais de dois empréstimos ativos

Given que Maria possui dois empréstimos ativos registrados no sistema

When ela tenta registrar um terceiro empréstimo

Then o sistema deve negar o registro

And nenhum novo empréstimo deve ser criado


---

Scenario: Usuário pode registrar novo empréstimo após devolver equipamento

Given que Maria possui dois empréstimos ativos

And um dos empréstimos foi devolvido

When ela solicita um novo empréstimo

Then o sistema deve permitir o registro

And o novo empréstimo deve ser criado