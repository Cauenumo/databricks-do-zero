# Databricks notebook source
# MAGIC %md
# MAGIC # 01 - Bronze: o dado cru
# MAGIC Lê as corridas de táxi de Nova York da tabela de exemplo `samples.nyctaxi.trips` e grava uma cópia fiel, sem limpar nada.

# COMMAND ----------

CATALOGO = "workspace"
SCHEMA = "taxi_do_zero"
spark.sql(f"CREATE SCHEMA IF NOT EXISTS {CATALOGO}.{SCHEMA}")

# COMMAND ----------

from pyspark.sql import functions as F

corridas = (
    spark.read.table("samples.nyctaxi.trips")
    .withColumn("_ingerido_em", F.current_timestamp())
)

corridas.write.mode("overwrite").saveAsTable(f"{CATALOGO}.{SCHEMA}.bronze_corridas")

# COMMAND ----------

# MAGIC %sql
# MAGIC -- A mesma tabela, agora em SQL, no mesmo notebook
# MAGIC SELECT count(*) AS corridas FROM workspace.taxi_do_zero.bronze_corridas

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Corridas com distância zero: vão ser barradas na silver
# MAGIC SELECT tpep_pickup_datetime, trip_distance, fare_amount, pickup_zip
# MAGIC FROM workspace.taxi_do_zero.bronze_corridas
# MAGIC WHERE trip_distance = 0
# MAGIC ORDER BY fare_amount DESC
# MAGIC LIMIT 5

# COMMAND ----------

# MAGIC %sql
# MAGIC -- As duas corridas do vídeo:
# MAGIC --   amarela  = a que vamos acompanhar até o dashboard (5,2 milhas, US$ 95)
# MAGIC --   vermelha = distância zero (US$ 105), vai ser barrada na silver
# MAGIC SELECT
# MAGIC   CASE WHEN trip_distance = 0 THEN 'vermelha: distância zero' ELSE 'amarela: a que vamos acompanhar' END AS corrida,
# MAGIC   tpep_pickup_datetime, trip_distance, fare_amount, pickup_zip
# MAGIC FROM workspace.taxi_do_zero.bronze_corridas
# MAGIC WHERE (trip_distance = 5.2 AND fare_amount = 95  AND pickup_zip = 10009)
# MAGIC    OR (trip_distance = 0   AND fare_amount = 105 AND pickup_zip = 7114)
# MAGIC ORDER BY trip_distance DESC
