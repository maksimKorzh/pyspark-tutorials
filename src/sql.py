# let import pyspark as a module
import findspark
findspark.init('/opt/spark')

# packages
from pyspark.sql import SparkSession

# init spark session
spark = SparkSession.builder.master('local[1]').appName('SQL').getOrCreate()

# dataset
data = [
    ("Robert", "M", 40000),
    ("James", "M", 50000),
    ("Michael", "M", 80000),
    ("Maria", "F", 44000),
    ("Jen", "F", 56000)
]

# schema
schema = ['Name', 'Gender', 'Salary']

# create a dataframe
df = spark.createDataFrame(data=data, schema=schema)
print('Original dataframe')
df.printSchema()
df.show()

# enable SQL queries
df.createOrReplaceTempView('TEMP')
print('Select all:')
spark.sql('SELECT * FROM TEMP').show()

# select the only column
print('Names:')
names = spark.sql('SELECT Name FROM TEMP')
names.printSchema()
names.show()

# select columns with specific data
females = spark.sql('SELECT * FROM TEMP WHERE Gender = "F"')
females.printSchema()
females.show()











