# COMMAND ----------
# Widget et paramètres
dbutils.widgets.text("env", "dev", "Environnement")
env = dbutils.widgets.get("env")

# COMMAND ----------
# Imports
import json
from libs.io_utils import write_delta, saveAsTable
from libs.transformations import clean_sales

# COMMAND ----------
# Charger configuration
with open(f"/Workspace/Users/mohcine.sirah@gmail.com/DatabrickProject/conf/{env}.json") as f:
    config = json.load(f)

input_path = config["input_path"]
output_path = config["output_path"]

# COMMAND ----------
# Lire données CSV
df = spark.read.parquet(input_path, header=True)

# COMMAND ----------
# Transformer
df_clean = clean_sales(df)

#filter etat_sin = INDETERMINE
df_clean = df_clean.filter(df_clean.etat_sin == "INDETERMINE")

# COMMAND ----------
# Sauvegarde Delta
write_delta(df_clean, output_path)


# COMMAND ----------
# Sauvegarde Table sql sales_clean
saveAsTable(spark,df_clean, "sinistres_out")

print("Data saved")
display(df_clean,100)
