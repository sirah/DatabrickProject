# COMMAND ----------
from pyspark.sql import SparkSession

def read_delta(spark: SparkSession, path: str):
    return spark.read.format("delta").load(path)

def write_delta(df, path: str, mode="overwrite"):
    df.write.format("delta").mode(mode).save(path)

def saveAsTable(spark: SparkSession,df, name: str):
    spark.sql(f"DROP TABLE IF EXISTS {name}")
    df.write.saveAsTable(name)