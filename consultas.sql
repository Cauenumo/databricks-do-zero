-- Consultas usadas no SQL Editor do vídeo "Databricks do zero na prática".
-- Rode depois do job (ou dos 3 notebooks), na Databricks Free Edition.

-- 1. A gold inteira: soma da tarifa do taxímetro (fare_amount) por dia e por CEP de embarque
SELECT * FROM workspace.taxi_do_zero.gold_tarifa_dia_regiao;

-- 2. Onde está a corrida amarela (4 de janeiro de 2016, CEP 10009): 13 corridas, US$ 179,50
SELECT * FROM workspace.taxi_do_zero.gold_tarifa_dia_regiao
WHERE dia = '2016-01-04' AND cep_embarque = 10009;

-- 3. As 13 corridas que formam esses US$ 179,50 (a amarela é a de US$ 95)
SELECT tpep_pickup_datetime, trip_distance, fare_amount
FROM workspace.taxi_do_zero.silver_corridas
WHERE to_date(tpep_pickup_datetime) = '2016-01-04' AND pickup_zip = 10009
ORDER BY fare_amount DESC;
