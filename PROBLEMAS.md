# Problemas Identificados — Leitura Inicial do Código

Este arquivo é preenchido pelos estudantes na Aula 1 após a leitura do código legado.
Descreva em linguagem livre tudo que parecer estranho, errado ou difícil de entender.
Não é necessário usar termos técnicos neste momento.

---

## Minha leitura inicial

Exemplo de entradas:
- "O código usa variáveis globais (listas de equipamentos e empréstimos) que são acessadas diretamente pela classe. Isso deixa confuso de onde os dados vêm e pode causar problemas se o sistema crescer."
- "A classe faz muitas coisas ao mesmo tempo, como registrar empréstimo, calcular multa e ainda “enviar e-mail” (print). Fica difícil entender qual é a responsabilidade principal dela."
- "O cálculo de multa aparece mais de uma vez no código, o que é ruim porque, se precisar mudar a regra, tem que alterar em vários lugares."
- "O controle de disponibilidade do equipamento é feito manualmente em vários pontos, o que pode gerar erro se esquecer de atualizar."
- "Tem mistura de lógica com interface: o sistema imprime mensagens direto na tela dentro dos métodos, o que dificulta reutilizar o código em outro lugar (por exemplo, um sistema web)."

  
---

## Revisão com vocabulário técnico

*(Este espaço será preenchido após a Aula 4, quando os termos técnicos corretos forem aprendidos)*
