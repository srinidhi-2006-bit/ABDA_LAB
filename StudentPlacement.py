from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler, StringIndexer
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
spark = SparkSession.builder.appName("StudentPlacement").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
df = spark.read.csv("Q13_student_placement.csv", header=True, inferSchema=True)
indexer = StringIndexer(inputCol="placed", outputCol="label")
df = indexer.fit(df).transform(df)
assembler = VectorAssembler(
inputCols=["cgpa", "no_of_internships", "projects", "aptitude_score", "communication_score"],
outputCol="features"
)
df = assembler.transform(df)
train_data, test_data = df.randomSplit([0.8, 0.2], seed=42)
rf = RandomForestClassifier(
featuresCol="features", labelCol="label", numTrees=10, seed=42
)
model = rf.fit(train_data)
predictions = model.transform(test_data)
print("Predictions:")
predictions.select(
"sid", "cgpa", "no_of_internships", "projects", "placed", "prediction"
).show()
evaluator = MulticlassClassificationEvaluator(
labelCol="label", predictionCol="prediction", metricName="accuracy"
)
print("Accuracy:", evaluator.evaluate(predictions))
spark.stop()
