
import pytest
from pyspark.sql import SparkSession
from libs.transformations import clean_sales

spark = SparkSession.builder.master("local[1]").appName("tests").getOrCreate()

def test_clean_sales():
    df = spark.createDataFrame(
        [(1, "Paris"), (1, "Paris"), (2, None)],
        ["id", "city"]
    )
    df_clean = clean_sales(df)
    assert df_clean.count() == 1  # Suppression doublon + null
