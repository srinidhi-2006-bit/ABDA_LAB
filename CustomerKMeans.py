from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler, StandardScaler
from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator
spark = SparkSession.builder.appName("CustomerKMeans").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
df = spark.read.csv("Q15_customer_segmentation.csv", header=True, inferSchema=True)
assembler = VectorAssembler(
inputCols=["age", "annual_income", "spending_score", "purchase_frequency"],
outputCol="features"
)
df = assembler.transform(df)
scaler = StandardScaler(
inputCol="features", outputCol="scaled_features",
withMean=True, withStd=True
)
df = scaler.fit(df).transform(df)
kmeans = KMeans(
k=3, seed=42, featuresCol="scaled_features", predictionCol="cluster"
)
model = kmeans.fit(df)
predictions = model.transform(df)
print("Cluster Assignments:")
predictions.select(
"customer_id", "age", "annual_income", "spending_score",
"purchase_frequency", "cluster"
).show(100)
evaluator = ClusteringEvaluator(
featuresCol="scaled_features", predictionCol="cluster",
metricName="silhouette"
)
print("Silhouette Score:", evaluator.evaluate(predictions))
spark.stop()
