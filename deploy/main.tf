terraform {
  required_providers {
    databricks = {
      source  = "databricks/databricks"
      version = "1.31.1" # ou plus récent
    }
  }
}

provider "databricks" {
  host  = "https://<your-workspace>.cloud.databricks.com"
  token = "<your-personal-access-token>"
}

resource "databricks_job" "pipeline_ingestion" {
  name = "pipeline_ingestion"

  task {
    task_key = "ingestion"

    notebook_task {
      notebook_path   = "/Workspace/Users/mohcine.sirah@gmail.com/DatabrickProject/jobs/pipeline_ingestion.py"
      base_parameters = {
        input_path = "/mnt/dev/raw/"
      }
    }

    new_cluster {
      spark_version = "14.3.x-scala2.12"
      node_type_id  = "Standard_DS3_v2"
      num_workers   = 2
    }
  }
}
