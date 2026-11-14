# Databricks notebook source
# MAGIC %md
# MAGIC # 03 - Gold: o resumo para consumo
# MAGIC Soma de `fare_amount` (tarifa do taxímetro, não o total cobrado) por dia e por CEP de embarque.

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE workspace.taxi_do_zero.gold_tarifa_dia_regiao AS
# MAGIC SELECT
# MAGIC   to_date(tpep_pickup_datetime) AS dia,
# MAGIC   pickup_zip                    AS cep_embarque,
# MAGIC   count(*)                      AS corridas,
# MAGIC   round(sum(fare_amount), 2)    AS soma_fare_amount
# MAGIC FROM workspace.taxi_do_zero.silver_corridas
# MAGIC GROUP BY ALL

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM workspace.taxi_do_zero.gold_tarifa_dia_regiao
# MAGIC ORDER BY dia, soma_fare_amount DESC
# MAGIC LIMIT 20
