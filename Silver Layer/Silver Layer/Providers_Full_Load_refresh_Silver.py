# Databricks notebook source
# Databricks notebook source
from pyspark.sql import SparkSession, functions as f

#Reading Hospital A departments data 
df_hosa=spark.read.parquet("/mnt/bronze/hos-a/providers")

#Reading Hospital B departments data 
df_hosb=spark.read.parquet("/mnt/bronze/hos-b/providers")

df_hosa = df_hosa.withColumnRenamed("DepartmentID","DeptID");

#union two departments dataframes
df_merged = df_hosa.unionByName(df_hosb)
display(df_merged)

df_merged.createOrReplaceTempView("providers")

# COMMAND ----------

# MAGIC %sql
# MAGIC  CREATE TABLE IF NOT EXISTS audit.providers (
# MAGIC     ProviderID string,
# MAGIC     FirstName string,
# MAGIC     LastName string,
# MAGIC     Specialization string,
# MAGIC     DeptID string,
# MAGIC     NPI long,
# MAGIC     datasource string,
# MAGIC     is_quarantined boolean
# MAGIC )
# MAGIC USING DELTA;

# COMMAND ----------

# MAGIC %sql
# MAGIC truncate table audit.providers;

# COMMAND ----------

# MAGIC %sql 
# MAGIC  INSERT INTO audit.providers
# MAGIC  select 
# MAGIC  distinct
# MAGIC  ProviderID,
# MAGIC  FirstName,
# MAGIC  LastName,
# MAGIC  Specialization,
# MAGIC  DeptID,
# MAGIC  cast(NPI as INT) NPI,
# MAGIC  datasource,
# MAGIC      CASE 
# MAGIC          WHEN ProviderID IS NULL OR DeptID IS NULL THEN TRUE
# MAGIC          ELSE FALSE
# MAGIC      END AS is_quarantined
# MAGIC from providers;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM providers;

# COMMAND ----------

