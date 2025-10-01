## DatabrickProject
# My Project - Databricks PySpark

## Structure
- `conf/` : fichiers de configuration par environnement
- `libs/` : fonctions réutilisables (IO, transformations, validation)
- `notebooks/` : points d’entrée pour les jobs
- `tests/` : tests unitaires (pytest)
- `jobs/` : définition des jobs Databricks

## Installation locale
```bash
pip install -r requirements.txt
pytest tests/
