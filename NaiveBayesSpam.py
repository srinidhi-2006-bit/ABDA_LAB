from pyspark.sql import SparkSession
from pyspark.sql.functions import concat_ws
from pyspark.ml.feature import Tokenizer, HashingTF, StringIndexer
from pyspark.ml.classification import NaiveBayes
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
spark = SparkSession.builder.appName("NaiveBayesSpam").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
df = spark.read.csv("Q14_email_spam.csv", header=True, inferSchema=True)
df = df.withColumn("text", concat_ws(" ", "subject", "message"))
tokenizer = Tokenizer(inputCol="text", outputCol="words")
df = tokenizer.transform(df)
hashing = HashingTF(inputCol="words", outputCol="features", numFeatures=1000)
df = hashing.transform(df)
indexer = StringIndexer(inputCol="label", outputCol="label_index")
df = indexer.fit(df).transform(df)
train_data, test_data = df.randomSplit([0.8, 0.2], seed=42)
nb = NaiveBayes(featuresCol="features", labelCol="label_index")
model = nb.fit(train_data)
predictions = model.transform(test_data)
print("Predictions:")
predictions.select("subject", "label", "prediction").show()
evaluator = MulticlassClassificationEvaluator(
labelCol="label_index", predictionCol="prediction", metricName="accuracy"
)
print("Classification Accuracy:", evaluator.evaluate(predictions))
spark.stop()
