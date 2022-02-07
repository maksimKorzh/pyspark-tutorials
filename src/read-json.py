# let import pyspark as a module
import findspark
findspark.init('/opt/spark')

# packages
from pyspark.sql import SparkSession

# init local spark session
spark = SparkSession.builder.master('local[1]').appName('JSON loader').getOrCreate()

# create data frame from JSON file
print('Common JSON file example: \n\n')
df1 = spark.read.json('./resources/zipcodes.json')
df1.printSchema()
df1.show()

# load multiline JSON
print('Multiline JSON file example: \n\n')
df2 = spark.read.option('multiline', 'true').json('./resources/multiline-zipcode.json')
df2.printSchema()
df2.show()

# load multiple JSON files
print('Multiple JSON files example: \n\n')
df3 = spark.read.json(['./resources/zipcode1.json', './resources/zipcode2.json'])
df3.printSchema()
df3.show()

# load all JSON files from a folder
print('Load all JSON files form a folder')
df4 = spark.read.json('./resources/*.json')
df4.printSchema()
df4.show()



















