from pyspark.sql import SparkSession

def read_delta(spark: SparkSession, path: str):
    return spark.read.format("delta").load(path)

def write_delta(df, path: str, mode="overwrite"):
    df.write.format("delta").mode(mode).save(path)
