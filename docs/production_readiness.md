# Production Readiness Checklist

## 1. Pipeline e qualidade

| Item | Status | Esforço | Prioridade | Observação |
|---|---|---|---|---|
| Lint roda a cada push | ✅ OK | feito | alta | `ruff check .` no `ci.yml`, antes dos testes |
| Testes rodam a cada push | ✅ OK | feito | alta | `pytest` no `ci.yml`, 25 testes e todos estão passando |
| Gate de cobertura ativo | ✅ OK | feito | alta |O gate está configurado em 80% `--cov-fail-under=80`, e a cobertura atual é de ~95% |
| Limiar de 80% é adequado? | ⚠️ PARCIAL | 1 dia | alta | 80% é razoável para o tamanho do projeto, mas não distingue código crítico de código trivial|

## 2. Containerização (avaliação conceitual)

| Item | Status | Esforço | Prioridade | Observação |
|---|---|---|---|---|
| Existe receita de build | ❌ FALTA | 1 dia | média | Não existe nenhum Dockerfile no projeto |
| Build seria reprodutível | ⚠️ PARCIAL | 2-3h | média | `requirements-dev.txt` agora tem versões mínimas fixadas, mas não exatas, sem lockfile, builds em datas diferentes podem puxar versões diferentes |
| Imagem teria tamanho razoável | ❌ FALTA | 2-3h | baixa | Sem Dockerfile não há como avaliar |
| Rodaria sem root | ❌ FALTA | 2-3h | média | Nenhuma configuração de usuário não-root foi definida, porque não existe imagem ainda |
| Há como excluir arquivos do contexto de build | ❌ FALTA | 1-2h | média | O projeto possui não possui .dockerignore |

## 3. Persistência

| Item | Status | Esforço | Prioridade | Observação |
|---|---|---|---|---|
| Empréstimos sobrevivem ao fim do processo | ❌ FALTA | 2-3 dias | alta | Os empréstimos são guardados em uma lista na memória, ao fechar o Main todos os dados somem |
| Equipamentos sobrevivem ao fim do processo | ❌ FALTA | 2-3 dias | alta | A disponibilidade dos equipamentos não é armazenada após fechar o programa |
| Dados sobrevivem ao fim do processo| ❌ FALTA | 2-3 dias | alta | Não existe nenhuma forma de persistência, pois não tem nenhum banco de dados persistente |

## 4. Segurança

| Item | Status | Esforço | Prioridade | Observação |
|---|---|---|---|---|
| Credenciais fora do código | ✅ OK | 2-3h | alta | O sistema não usa nenhuma credencial por que não há login ou BD externo |
| Entradas validadas | ⚠️ PARCIAL | 1 dia | média | Há validação de equipamento existente/disponível e limite de empréstimos por usuário, mas não há validação do formato de e-mail |
| Dependências fixadas | ✅ OK | feito | média | `requirements-dev.txt` com `pytest>=8.0`, `pytest-cov>=4.1`, `ruff>=0.5` desde a Aula 13 |
| Dependências auditadas | ❌ FALTA | 2-3h | média | Nenhuma ferramenta de auditoria de vulnerabilidades está configurada no CI |

## 5. Observabilidade

| Item | Status | Esforço | Prioridade | Observação |
|---|---|---|---|---|
| Logs com nível | ❌ FALTA | 1 dia | média | O sistema envia notificações, mas não há distinção entre os níveis |
| Logs com destino configurável | ❌ FALTA | 1 dia | média | Saída vai só para o console; não há gravação em arquivo nem envio a um serviço externo |
| Métricas | ❌ FALTA | 1-2 dias | média | Não existe nenhuma métrica (quantos empréstimos/dia, taxa de atraso, etc.) |
| Dá para investigar uma falha de ontem | ❌ FALTA | 1-2 dias | alta | Como não há persistência de log nem de dados, uma falha de ontem não deixa rastro nenhum hoje |

## 6. Deployment

| Item | Status | Esforço | Prioridade | Observação |
|---|---|---|---|---|
| Existe processo de deploy | ❌ FALTA | 1-2 dias | alta | O sistema roda só localmente não há deploy nenhum |
| Como uma versão nova chegaria ao usuário | ❌ FALTA | 2-3h | alta | Para entregar uma versão nova o usuário puxar o código do GitHub e rodar manualmente, não existe empacotamento então cada atualização depende de acesso direto ao repositório |
| Plano de rollback | ❌ FALTA | 6-8h | alta | Não tem nenhum procedimento para voltar a uma versão anterior em casos de falha pois não há deploy |