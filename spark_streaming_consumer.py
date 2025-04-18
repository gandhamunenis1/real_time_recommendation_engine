
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, IntegerType, TimestampType

spark = SparkSession.builder     .appName("ClickstreamConsumer")     .getOrCreate()

schema = StructType()     .add("user_id", IntegerType())     .add("product_id", IntegerType())     .add("event_type", StringType())     .add("timestamp", StringType())

df = spark.readStream     .format("kafka")     .option("kafka.bootstrap.servers", "localhost:9092")     .option("subscribe", "clickstream_topic")     .load()

parsed_df = df.selectExpr("CAST(value AS STRING)")     .select(from_json(col("value"), schema).alias("data"))     .select("data.*")

query = parsed_df.writeStream     .outputMode("append")     .format("console")     .start()

query.awaitTermination()
