# let import pyspark as a module
import findspark
findspark.init('/opt/spark')

# packages
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType
from pyspark.sql.types import StringType
from pyspark.sql.types import IntegerType
from pyspark.sql.types import DoubleType
from pyspark.sql.types import BooleanType

# create spark session
spark = SparkSession.builder.master('local[1]').appName('schemas').getOrCreate()

# define datatypes schema
schema = StructType() \
         .add('RecordNumber', IntegerType()) \
         .add('Zipcode', IntegerType()) \
         .add('ZipCodeType', StringType()) \
         .add('City', StringType()) \
         .add('State', StringType()) \
         .add('LocationType', StringType()) \
         .add('Lat', DoubleType()) \
         .add('Long', DoubleType()) \
         .add('Xaxis', DoubleType()) \
         .add('Yaxis', DoubleType()) \
         .add('Zaxis', DoubleType()) \
         .add('WorldRegion', StringType()) \
         .add('LocationText', StringType()) \
         .add('Decommisioned', BooleanType())

# load csv file
df = spark.read.format('csv').schema(schema).load('./resources/zipcodes.csv')
df.printSchema()
df.show()
