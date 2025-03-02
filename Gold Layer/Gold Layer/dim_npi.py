# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS audit.dim_npi (
# MAGIC   npi_id STRING,
# MAGIC   first_name STRING,
# MAGIC   last_name STRING,
# MAGIC   position STRING,
# MAGIC   organisation_name STRING,
# MAGIC   last_updated STRING,
# MAGIC   refreshed_at TIMESTAMP)

# COMMAND ----------

# MAGIC %sql
# MAGIC truncate table audit.dim_npi;

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into
# MAGIC   audit.dim_npi
# MAGIC select
# MAGIC   npi_id,
# MAGIC   first_name,
# MAGIC   last_name,
# MAGIC   position,
# MAGIC   organisation_name,
# MAGIC   last_updated,
# MAGIC   current_timestamp()
# MAGIC from
# MAGIC   audit.npi_extract
# MAGIC   where is_current_flag = true;

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from audit.dim_npi;