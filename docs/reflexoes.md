# Reflexões

---

## Aula 04 — Aplicação do SRP

Durante a reorganização do sistema, uma das principais decisões foi definir quais responsabilidades deveriam permanecer juntas e quais deveriam ser separadas. Inicialmente, a lógica de empréstimos, notificações e manipulação dos dados estava fortemente ligada, o que dificultava identificar limites claros entre as partes do sistema.

A principal dúvida surgiu em relação às notificações. Como o envio de mensagens acontece após operações como empréstimos, devoluções e atrasos, parecia natural que essa funcionalidade permanecesse dentro do serviço principal. No entanto, após analisar o princípio da Responsabilidade Única (SRP), ficou evidente que alterações no mecanismo de notificação poderiam gerar modificações desnecessárias no módulo responsável pelas regras de negócio.

Por esse motivo, foi criada uma classe específica para notificações, deixando o ServicoEmprestimo responsável apenas pelas regras relacionadas ao processo de empréstimo. Essa separação reduz o acoplamento e torna cada módulo mais coeso.

Outra decisão importante foi manter os modelos apenas como representação das entidades do domínio. Dessa forma, Equipamento e Emprestimo armazenam informações, enquanto os serviços concentram os comportamentos e regras do sistema.

Segundo Valente (Capítulo 5), módulos com responsabilidades bem definidas tendem a ser mais fáceis de compreender, manter e evoluir ao longo do tempo. A decomposição realizada buscou seguir exatamente essa orientação.

---

## Aula 05 — Aplicação do OCP

O princípio Aberto/Fechado (OCP) foi aplicado no sistema por meio da utilização de herança e polimorfismo. Antes da refatoração, o cálculo de multas dependia de estruturas condicionais baseadas no tipo do equipamento. Essa abordagem exigia modificações sempre que um novo tipo fosse adicionado ao sistema.

Após a alteração, cada subclasse de Equipamento passou a ser responsável por implementar sua própria regra de cálculo de multa. Dessa forma, o ServicoEmprestimo não precisa conhecer detalhes específicos de cada equipamento, apenas utilizar o método calcular_multa() definido na classe base.

A principal vantagem dessa solução é permitir a expansão do sistema sem necessidade de alterar código já existente. Caso um novo equipamento seja cadastrado futuramente, basta criar uma nova subclasse implementando o comportamento necessário.

Entretanto, conforme discutido por Valente no Capítulo 5, o OCP possui limitações. Se surgirem requisitos muito diferentes dos atuais, como multas calculadas por hora, políticas variáveis conforme calendário acadêmico ou regras associadas ao perfil do usuário, a hierarquia de classes poderá crescer excessivamente.

Nesse cenário, seria necessário considerar outras formas de decomposição, utilizando composição ou estratégias específicas para encapsular essas regras. Portanto, o OCP melhora a extensibilidade do sistema, mas não elimina a necessidade de revisões arquiteturais quando os requisitos mudam significativamente.

---

## Aula 06 — Verificação do LSP

Foi realizada uma análise das subclasses de Equipamento para verificar se todas respeitam o contrato definido pela classe abstrata.

Nos testes realizados, os métodos calcular_multa(0) retornaram sempre o valor 0.0, demonstrando conformidade com a regra de não gerar multas inexistentes.

Também foram avaliados cenários com valores negativos, como calcular_multa(-5). Em todos os casos, o retorno permaneceu igual a 0.0 devido ao uso da função max(), impedindo que multas negativas fossem produzidas.

Além disso, nenhuma das subclasses gera exceções inesperadas durante sua execução. O retorno permanece sempre compatível com o contrato estabelecido pela superclasse, ou seja, um valor numérico não negativo.

Esses resultados indicam que Notebook, Projetor e Cabo HDMI podem substituir Equipamento sem alterar o comportamento esperado pelo ServicoEmprestimo. Portanto, o princípio da Substituição de Liskov (LSP) encontra-se atendido.

De acordo com Valente (Capítulo 5), uma subclasse deve preservar as expectativas estabelecidas pela classe base. A verificação realizada demonstra que essa condição foi respeitada na implementação desenvolvida.

---

## Aula 06 — Aplicação do DIP

A aplicação do princípio da Inversão de Dependência (DIP) alterou significativamente a forma como os componentes do sistema se relacionam.

Antes da refatoração, o ServicoEmprestimo era responsável por criar internamente suas dependências. Isso fazia com que o módulo dependesse diretamente de implementações específicas de repositório e notificação, aumentando o acoplamento.

Após a modificação, essas dependências passaram a ser fornecidas externamente por meio do construtor. Dessa forma, o serviço deixou de controlar a criação dos objetos e passou apenas a utilizar seus comportamentos.

Essa mudança não representa apenas uma alteração sintática. Conceitualmente, o controle da criação dos componentes foi deslocado para um nível superior da aplicação, tornando o serviço menos dependente de implementações concretas.

Um dos benefícios observados foi a possibilidade de utilizar objetos falsos durante testes. Repositórios simulados e notificadores simulados podem ser utilizados sem necessidade de modificar o código principal do sistema.

Segundo Valente (Capítulo 5), a inversão de dependência reduz acoplamento e aumenta flexibilidade arquitetural. No contexto deste projeto, essa mudança contribui diretamente para o atendimento do RNF04, relacionado à testabilidade isolada das regras de negócio.
