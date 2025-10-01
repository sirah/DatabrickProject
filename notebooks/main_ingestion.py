
import json
from libs.io_utils import write_delta
from libs.transformations import clean_sales

# Paramètre d'environnement
env = dbutils.widgets.get("env")

# Charger la config JSON
with open(f"/dbfs/FileStore/config/{env}.json") as f:
    config = json.load(f)

input_path = config["input_path"]
output_path = config["output_path"]

# Lire les données brutes
df = spark.read.csv(input_path, header=True)

# Transformer
df_clean = clean_sales(df)

# Sauvegarder en Delta
write_delta(df_clean, output_path)
