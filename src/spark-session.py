# let import pyspark
import findspark
findspark.init('/opt/spark')

# packages
from pyspark.sql import SparkSession

# init spark session
spark = SparkSession.builder.master('local[1]').appName('myspark').getOrCreate()

# print session info
print('App name:', spark.sparkContext.appName)
print('Master:', spark.sparkContext.master)

