# Databricks do zero na prática

Código do vídeo **"Databricks do zero na prática: do dado cru ao dashboard (e um pipeline que quebra)"**, do canal [Cauê Moreira](https://www.youtube.com/@devcauemoreira).

No vídeo, uma corrida de táxi de Nova York atravessa um pipeline inteiro na Databricks Free Edition: bronze, silver, gold, um job agendado que quebra de propósito, o conserto com Repair run, o SQL Editor, um dashboard e a Lineage.

## O que tem aqui

| Arquivo | O que faz |
|---|---|
| `notebooks/01_bronze.py` | Lê `samples.nyctaxi.trips` e grava a cópia fiel em `workspace.taxi_do_zero.bronze_corridas`. Mostra as duas corridas do vídeo |
| `notebooks/02_silver.py` | Fica só com corrida de distância maior que zero e tarifa não negativa. Mostra que só a corrida amarela passou |
| `notebooks/03_gold.py` | Soma de `fare_amount` (tarifa do taxímetro) por dia e por CEP de embarque |
| `consultas.sql` | As consultas do SQL Editor, incluindo onde a corrida amarela aparece na gold |
| `dashboard/corridas-de-taxi.lvdash.json` | O dashboard do vídeo, para importar |

## Passo a passo

### 1. Crie a conta
Databricks Free Edition: https://www.databricks.com/learn/free-edition (grátis).

### 2. Traga os notebooks
No menu **Workspace**, clique em **Create > Git folder** e cole a URL deste repositório. Os três notebooks aparecem dentro da pasta `notebooks`.

Outra opção: baixe os arquivos `.py` e use **Import** no Workspace.

### 3. Rode na ordem
`01_bronze`, `02_silver`, `03_gold`. O compute serverless liga sozinho na primeira célula.

### 4. Monte o job
Em **Jobs & Pipelines > Create > Job**, crie três tarefas do tipo notebook, cada uma dependendo da anterior:

`bronze (01_bronze)` → `silver (02_silver)` → `gold (03_gold)`

Para quebrar de propósito, como no vídeo: no `02_silver`, troque `fare_amount` por `fare_amout`, rode o job e veja a silver falhar e a gold ficar em "Upstream failed". Corrija o nome e use **Repair run**: só a silver e a gold rodam de novo.

Na Free Edition, o serverless já vem com repetição automática (até 4 tentativas). Para ver a falha na hora, tire o retry na tarefa.

### 5. Consulte e monte o dashboard
- Rode as consultas de `consultas.sql` no **SQL Editor**.
- Em **Dashboards > Create > Import dashboard from file**, escolha `dashboard/corridas-de-taxi.lvdash.json`.

## Sobre os dados
`samples.nyctaxi.trips` é uma tabela de exemplo da Databricks, com corridas de táxi de Nova York de janeiro e fevereiro de 2016. As regras da silver (distância maior que zero, tarifa não negativa) são didáticas, só para este exemplo.

## Dúvidas
Deu erro em algum passo? Abra uma issue neste repositório com o número do passo e a mensagem de erro.

## Mais conteúdo
- YouTube: https://www.youtube.com/@devcauemoreira
- Cursos e simulados: https://www.udemy.com/user/caue-nunes-moreira/
- LinkedIn: https://www.linkedin.com/in/cauemoreira/

Databricks é marca da Databricks, Inc. Este repositório não tem vínculo com a empresa.
