# Databricks notebook source
# Databricks notebook source
storageAccountName = "healthcareadlsgen2"
#storageAccountAccessKey = dbutils.secrets.get(scope="healthcare-key-vault", key='healthcare-adls-gen2-access-key')
storageAccountAccessKey = "<adls-account-key>"
mountPoints=["gold","silver","bronze","landing","configs"]

for mountPoint in mountPoints:
    if not any(mount.mountPoint == f"/mnt/{mountPoint}" for mount in dbutils.fs.mounts()):
        try:
            dbutils.fs.mount(
                source = "wasbs://{}@{}.blob.core.windows.net".format(mountPoint, storageAccountName),
                mount_point = f"/mnt/{mountPoint}",
                extra_configs = {'fs.azure.account.key.' + storageAccountName + '.blob.core.windows.net': storageAccountAccessKey}
            )
            print(f"{mountPoint} mount succeeded!")
        except Exception as e:
            print("mount exception", e)

dbutils.fs.mounts()

# COMMAND ----------

