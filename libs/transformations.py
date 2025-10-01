from pyspark.sql import DataFrame

def clean_sales(df: DataFrame) -> DataFrame:
    """ Nettoyage basique des ventes """
    return df.dropna().dropDuplicates()
