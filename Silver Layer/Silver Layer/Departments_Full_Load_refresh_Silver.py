# Databricks notebook source
# Databricks notebook source
from pyspark.sql import SparkSession, functions as f

#Reading Hospital A departments data 
df_hosa=spark.read.parquet("/mnt/bronze/hos-a/departments")

#Reading Hospital B departments data 
df_hosb=spark.read.parquet("/mnt/bronze/hos-b/departments")

# COMMAND ----------

df_hosa = df_hosa.withColumnRenamed('DepartmentID', 'DeptID')
df_hosa.show(10)

# COMMAND ----------

#union two departments dataframes
df_merged = df_hosa.unionByName(df_hosb)

# Create the dept_id column and rename deptid to src_dept_id
df_merged = df_merged.withColumn("SRC_Dept_id", f.col("deptid")) \
                     .withColumn("Dept_id", f.concat(f.col("deptid"),f.lit('-'), f.col("datasource"))) \
                     .drop("deptid")

df_merged.createOrReplaceTempView("df_merged")

# COMMAND ----------

df_merged.show(10)

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM df_merged WHERE Name = "Emergency";

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS audit.departments (
# MAGIC   Dept_Id string,
# MAGIC   SRC_Dept_Id string,
# MAGIC   Name string,
# MAGIC   datasource string,
# MAGIC   is_quarantined boolean
# MAGIC )
# MAGIC USING DELTA;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM audit.departments;

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO audit.departments
# MAGIC SELECT 
# MAGIC   Dept_Id,
# MAGIC   SRC_Dept_Id,
# MAGIC   Name,
# MAGIC   Datasource,
# MAGIC   CASE 
# MAGIC           WHEN SRC_Dept_Id IS NULL OR Name IS NULL THEN TRUE
# MAGIC           ELSE FALSE
# MAGIC   END AS is_quarantined
# MAGIC FROM df_merged

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from audit.departments WHERE Name = "Emergency";

# COMMAND ----------

