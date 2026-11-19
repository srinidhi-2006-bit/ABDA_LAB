from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler, StandardScaler, PCA
spark = SparkSession.builder.appName("CustomerPCA").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
df = spark.read.csv("Q12_customer_behaviour.csv", header=True, inferSchema=True)
assembler = VectorAssembler(
inputCols=[
"annual_income", "purchase_frequency", "average_order_value",
"website_visits", "discount_usage", "customer_spend"
],
outputCol="features"
)
df = assembler.transform(df)
scaler = StandardScaler(
inputCol="features", outputCol="scaled_features",
withMean=True, withStd=True
)
df = scaler.fit(df).transform(df)
pca = PCA(k=2, inputCol="scaled_features", outputCol="pca_features")
model = pca.fit(df)
result = model.transform(df)
print("PCA Result:")
result.select("customer_id", "pca_features").show()
print("Explained Variance:")
print(model.explainedVariance)
spark.stop()
