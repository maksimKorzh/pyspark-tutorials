# let import pyspark as a module
import findspark
findspark.init('/opt/spark')

# packages
from pyspark.sql import SparkSession

# create spark session
spark = SparkSession.builder.master('local[1]').appName('read-csv').getOrCreate()

# create data frame from CSV data
df = spark.read.csv('./resources/simple-zipcodes.csv')
df.printSchema()
df.show()
