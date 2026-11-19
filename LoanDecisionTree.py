from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler, StringIndexer
from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
spark = SparkSession.builder.appName("LoanDecisionTree").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
df = spark.read.csv("Q11_loan_approval.csv", header=True, inferSchema=True)
indexer = StringIndexer(inputCol="loan_status", outputCol="label")
df = indexer.fit(df).transform(df)
assembler = VectorAssembler(
inputCols=["age", "annual_income", "credit_score", "loan_amount", "years_of_employment"],
outputCol="features"
)
df = assembler.transform(df)
train_data, test_data = df.randomSplit([0.8, 0.2], seed=42)
dt = DecisionTreeClassifier(featuresCol="features", labelCol="label", seed=42)
model = dt.fit(train_data)
predictions = model.transform(test_data)
print("Predictions:")
predictions.select("applicant_id", "loan_status", "prediction").show()
evaluator = MulticlassClassificationEvaluator(
labelCol="label", predictionCol="prediction", metricName="accuracy"
)
print("Accuracy:", evaluator.evaluate(predictions))
spark.stop()
