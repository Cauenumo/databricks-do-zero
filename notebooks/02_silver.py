# Databricks notebook source
# MAGIC %md
# MAGIC # 02 - Silver: regras deste exemplo
# MAGIC Fica só o que passa pelas regras didáticas do vídeo: **distância maior que zero** e **tarifa não negativa** (`fare_amount` é a tarifa do taxímetro, não o total cobrado).

# COMMAND ----------

from pyspark.sql import functions as F

CATALOGO = "workspace"
SCHEMA = "taxi_do_zero"

bronze = spark.read.table(f"{CATALOGO}.{SCHEMA}.bronze_corridas")

silver = (
    bronze
    .filter((F.col("trip_distance") > 0) & (F.col("fare_amount") >= 0))
    .select(
        "tpep_pickup_datetime",
        "tpep_dropoff_datetime",
        "trip_distance",
        "fare_amount",
        "pickup_zip",
        "dropoff_zip",
    )
)

silver.write.mode("overwrite").saveAsTable(f"{CATALOGO}.{SCHEMA}.silver_corridas")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC   (SELECT count(*) FROM workspace.taxi_do_zero.bronze_corridas) AS bronze,
# MAGIC   (SELECT count(*) FROM workspace.taxi_do_zero.silver_corridas) AS silver

# COMMAND ----------

# MAGIC %sql
# MAGIC -- As duas corridas do vídeo, agora na silver: só a amarela passou
# MAGIC SELECT
# MAGIC   CASE WHEN trip_distance = 0 THEN 'vermelha: distância zero' ELSE 'amarela: a que vamos acompanhar' END AS corrida,
# MAGIC   tpep_pickup_datetime, trip_distance, fare_amount, pickup_zip
# MAGIC FROM workspace.taxi_do_zero.silver_corridas
# MAGIC WHERE (trip_distance = 5.2 AND fare_amount = 95  AND pickup_zip = 10009)
# MAGIC    OR (trip_distance = 0   AND fare_amount = 105 AND pickup_zip = 7114)
