import sys
import numpy as np

import pyspark.sql.functions as f
from pyspark.sql import SparkSession
from pyspark.context import SparkContext


spark = SparkSession.builder.appName('jdbc_use_case').getOrCreate()

place = '/path/example'
table = 'table_name'
user = 'User'
password = 'Pass'

query = f"""
	SELECT * FROM {table}
	"""

df = spark.read().format('jdbc') \
			.option('url', 'jdbc:teradata://TERADATA/CHARSET=UTF16, TMODE=ANSI') \
			.option('user', user) \
			.option('password', password) \
			.option('dbtable', f'({query}) emp') \
			.option('driver', 'com.teradata.jdbc.TeraDriver') \
			.load()

df = df.select([f.col(x).alias(x.lower()) for x in df.columns])

df.write.format('delta').mode('overwrite').save(place)

spark.stop()
